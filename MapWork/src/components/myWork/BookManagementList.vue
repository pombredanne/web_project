<template>
    <div class='Append-basic-temlate' id="book-manage">
        <div class="Append-basic-temlate-countent">
        
        </div>
        <div class="content-box">
            <div class="mid" v-loading="loading">
                <div class="mid-top" >
                    <div class="block-title">
                        <h2>{{input_title_name}}<i class="el-icon-question" title='请导入式样书' style="font-size:15px;height:20px;vertical-align:middle"></i></h2>
                    </div>
                    <div class="content-box-deep">
                        <div class="label-box">
                                <div class="label-box-text inline-black margin-right-input">
                                    <span>式样书类别</span>
                                </div>
                                <el-select :disabled="input_spec_type_flag" v-model="input_data.spec_type" placeholder="请选择式样书类别" @change="select_input" class="input-width">
                                    <el-option v-for="item in input_type_list" :key="item.fw_id" :label="item.spec_name" :value="item.spec_type" >
                                    </el-option>
                                </el-select>
                               
                                <div class="label-box-text  margin-right-input">
                                    <span class="inline-black margin-right-input">版本</span>
                                    <el-input  v-model="input_data.spec_ver"  placeholder="请填写式样书版本" class="input-width"></el-input>
                             
                                </div>
                                <div class="label-box-text inline-black margin-right-input">
                                    文件
                                </div>
                                <div class="label-box-text " style="display:inline-flex;width:60%" >
                                    <el-upload ref="upload" :disabled="upload_flag" action="${pageContext.request.contextPath}/lookup/editEvidence/123"  :http-request="uploadFile"
                                     :auto-upload="false" multiple :on-success='up_success' :before-upload='before_upload' :on-error="up_error" :on-change='up_chang_file' :data="input_data" >
                                        <el-button size="small" style="width:220px" type="primary" :disabled="upload_flag" @click="upload_click_fun" :title="title_alert">上传式样书文件</el-button>
                                        <span style="font-size:12px;color:red;word-wrap:break-word;display:inline-flex ">{{upload_remarks}}</span>
                                        <span style="font-size:12px;color:red;word-wrap:break-word;display:inline-flex ">
                                            <ul>
                                                <li v-for="item in upload_file_list">{{item.filename}}失败</li>
                                            </ul>
                                        </span>

                                    </el-upload>

                                </div>
                        </div>
                    </div>
                </div>
                <div style="clear: both;"></div>
                <div class="footer">
                    <el-button size="mini" type="primary" :disabled="upload_determine_flag" @click="determine()">&nbsp;&nbsp;确&nbsp;&nbsp;&nbsp;定&nbsp;&nbsp;</el-button>
                    <el-button size="mini" type="primary" @click="cancel()">&nbsp;&nbsp;退&nbsp;&nbsp;&nbsp;出&nbsp;&nbsp;</el-button>
                    <!-- <el-button size="mini" type="primary" disabled @click="save()">&nbsp;&nbsp;保&nbsp;&nbsp;&nbsp;存&nbsp;&nbsp;</el-button> -->
                </div>
            </div>
            <div class="right">
            </div>
            <div id="img-dialog-box">

            </div>
        </div>
    </div>
</template>
<script>
export default {
    data () {
        return {
            up_ip: this.Ip + "/DSDocInputBatch",
            upload_flag: true,
            title_alert: '只能上传pdf/excel文件',
            show_file_flag: false,
            input_type_list: [
                {
                    spec_name: "机能式样书",
                    spec_type: "FUNC"
                },
                {
                    spec_name: "要求式样书",
                    spec_type: "REQ"
                },
                {
                    spec_name: "操作式样书",
                    spec_type: "OPE"
                }
            ],
            input_data: {
                spec_type: '',
                spec_name: "",
                spec_num:'',
                spec_ver:'',
                proj_id: '',
                spec_id:0,
                replace:false,
            },
            select_input_spec_num:null,
            input_title_name:'式样书批量添加',
            show_file_list_name:'',
            input_spec_type_flag:false,
            input_spec_num_flag:false,
            input_spec_name_flag:false,
            input_spec_ver_flag:false,
            restaurants_spec_num:[],
            restaurants_spec_ver:[],
            spec_ver_list:[],
            state1:'',
            http_header:{},
            loading:false,
            upload_determine_flag:true,
            spec_name_alert_text:'',
            show_file_list_flag:true,
            files_list:[],
            formData:"",
            upload_remarks:"备注：以文件名为key,文件名相同情况下,版本也相同，文件就会被替换；版本不同则新增一版。",
            upload_file_list:[]
        }

    },
    computed: {
        four_data () {
            return this.input_data.spec_ver
        }
    },
    watch: {
        four_data (val) {
            if ( this.input_data.spec_ver !='') {
                this.upload_flag = false
            } else {
                this.upload_flag = true
            }
        },
    },
    created() {
        this.get_router_path_val_fun()        
    },
    destroyed() {
        if (sessionStorage.getItem('spec_name')) {
            sessionStorage.removeItem('spec_name')
        }
    },
    methods: {
        uploadFile(file){
            this.formData.append('file', file.file);
        },
        get_router_path_val_fun(){
            let route_data = JSON.parse(this.$route.query.data)
            this.input_data.proj_id = route_data.proj_id
            this.input_data.spec_type = route_data.input_type
        },
        select_input () {
            this.upload_flag = true
        },
        upload_click_fun () {
            this.$refs.upload.clearFiles()//清除上传文件列表
            this.upload_file_list = []
        },
        determine(){
            let datas = {
                "proj_id": this.proj_id,
                "model_id": '',
                accessToken: window.sessionStorage.getItem('accessToken'),
                "username": window.sessionStorage.getItem('Uall')
            };
            this.$axios.post(this.Ip + "/UserRoleCactus", datas).then(res => {
                if (res.data.result == "OK") {
                    var userPermissionData = res.data.content
                    if (this.getCatusPurviewManage(userPermissionData, '式样书添加') == true) {
                        // to do
                        this.formData = new FormData()
                        this.$refs.upload.submit();
                        this.formData.append('data',JSON.stringify(this.input_data));
                        this.upload_fun(this.formData)
                    } else {
                        this.$message({
                            type: "warning",
                            message: "您没有权限操作"
                        })
                    }
                } else {
                    // nothing to do
                    this.$message({
                        type: "warning",
                        message: res.data.error
                    })
                }
            })
            
        },
        upload_fun(formData){
            this.$axios.post(this.Ip + "/DSDocInputBatch",formData).then(res =>{
                if (res.data.result == 'OK') {
                    if (res.data.content.success.length !==0) {
                        this.up_success(res.data,'item', res.data.content.success)
                    }
                    for (let i = 0; i < res.data.content.error.length; i++) {
                        let item = res.data.content.error[i];
                        this.up_error(res.data,item,res.data.content.error)
                        this.upload_determine_flag = true
                        break
                    }
                } else {
                    this.$alert(res.data.error, '错误提示')
                    this.upload_determine_flag = true
                    this.loading=false
                }
            })
        },
        up_chang_file(file, fileList){
            this.show_file_list_flag=true//控制上传文件显示
            if (file) {
                this.upload_determine_flag = false
            }
        },
        before_upload (file) {
            // 检查上传文件类型
            if (this.proj_id == '') {
                this.$message({
                    type: 'warning',
                    message: 'please select project!'
                })
                return false
            }
            let file_type = file.type,
                regexp_sheet = RegExp(/.sheet/i),
                regexp_pdf = RegExp(/pdf/i),
                regexp_sheet_xlsm = RegExp(/.ms-excel/i);
            if (file_type.search(regexp_sheet) !== -1) {
                this.loading=true
                return true
            } else if (file_type.search(regexp_pdf) !== - 1) {
                this.loading=true
                return true
            } else if (file_type.search(regexp_sheet_xlsm) !== - 1) {
                this.loading=true
                return true
            } else {
                this.upload_determine_flag = true
                this.$alert("您上传的文件格式不支持", '提示')
                return false
            }
        },
        up_remove(file, fileList){
            // console.log(file, fileList,'up_remove')
            if (fileList.length == 0) {
                this.upload_determine_flag = true
                return
            }
            this.upload_determine_flag = false
        },
        up_success (response, file, fileList) {
            this.$message({
                type: 'success',
                message: '上传成功!',
                duration:0,
                showClose: true,
            })
            this.loading=false
            this.upload_flag = true
        },
        up_error(err, file, fileList){
            this.upload_file_list = fileList
            this.loading = false
            this.show_file_list_flag = false
            this.$message({
                type: 'error',
                message: 'error:'+ file.msg,
                duration:0,
                showClose: true,
            })
        },
        sort_spec_ver(property){//数组对象排序方法
            return function(obj1,obj2){
                var value1 = obj1[property];
                var value2 = obj2[property];
                return value2 - value1;     // 降序
            }
        },
        handleSelect_spec_ver(item){
            this.show_file_list_flag=false//版本输入框，一有改变就清空上传列表隐藏
        },
        cancel () {
            this.$router.push('/tagl/BookList');
        },
    }
}
</script>

<style scoped>
.label-box-text-p{
    padding: 0 0 0 180px;
    font-size: 12px;
    color: red
}
.input-width{
    width: 541px
}
.inline-black {
    display: inline-block;
    width: 150px
}
.margin-left {
    margin-left: 42px;
}

.margin-right-input {
    margin-right: 21px;
}
.go-doc-text {
    cursor: pointer;
}
.go-doc-text:hover {
    color: #42b983;
}
.Append-basic-temlate {
    margin: 0 auto;
    width: 100%;
    height: 100%;
    /*overflow-y: scroll;*/
}
.Append-basic-temlate-countent {
    max-width: 300px;
    width: 15%;
    height: 100%;
    padding: 20px;
    float: left;
}
.header {
    height: 400px;
    padding: 10%;
    clear: both;
}
.content-box {
    float: left;
    width: 84%;
    padding-left: 1%;
    height: 100%;
    background-color: #fff;
    border-left: 2px solid rgba(216,231,223,.5);
    overflow: scroll;
    overflow-x: hidden;
}
.mid {
    position: relative;
    width: 80%;
    height: 100%;
    float: left;
    padding-right: 20px;
    background-color: #fff;
    border-right: 2px solid rgba(216,231,223,.5);
    /* overflow: scroll; */
    overflow-x: hidden;
}
.mid-top {
    position: absolute;
    top: 0;
    bottom: 55px;
    width: 100%;
    padding-right: 20px;
    overflow-y: scroll;
}
.footer {
    position: absolute;
    bottom: 40px;
    right: 20px;
}
.block-title {
    margin: 40px 0 20px 0;
}
h2 {
    font-size: 22px;
    font-weight: bolder;
    background-color: #6bcca0;
    color: white;
    padding-left: 10px;
    line-height: 25px;
}
.content-box-deep {
    padding-left: 20px;
    color: #606266

}
.label-box {
    width: 100%;
    /* margin: 20px; */
    /* overflow: hidden; */
}
.label-box-text {
    margin-top: 20px;
    margin-bottom: 20px;
    font-size: 14px;
}
.upload-demo {
    margin-top: 10px;
}
.upload-demo-box {
    width: 260px;
    height: 100px;
    /*display: inline-block;*/
}
.add-box {
    /*line-height: 100px;*/
    height: 100px;
    width: 100px;
    padding-top: 20px;
    text-align: center;
    border: 1px double #ccc;
    cursor: pointer;
    font-size: 14px;
    /*margin:20px auto;*/
    margin-top: 20px;
}
.active {
    background: #fff;
}
.up-data-btn {
    width: 330px;
    height: 320px;
    /* margin-left: 20px; */
    /*margin-top:20px;*/
    display: block;
    background: #fff;
    outline: none;
    border: 1px dashed #ccc;
    color: #ccc;
    font-size: 15px;
}
.upload-demo-box {
    width: 330px;
    height: 350px;
    vertical-align: bottom;
    display: inline-block;
}
.Sequence-img {
    width: 100%;
    height: 100%;
}
.img-box {
    width: 350px;
    height: 330px;
    margin-top: 10px;
    padding-right: 20px;
    position: relative;
    display: inline-block;
}
.img-box:hover {
    cursor: pointer;
    border: 1px solid transparent;
    -moz-border-top-colors: red blue white white black;
    -moz-border-right-colors: red blue white white black;
    -moz-border-bottom-colors: red blue white white black;
    -moz-border-left-colors: red blue white white black;
}

.img_icon {
    position: absolute;
    right: 0px;
    top: 0;
    font-size: 24px;
    cursor: pointer;
}
.dialog_img {
    display: block;
    margin: 0 auto;
}
.dialog-title span {
    font-size: 20px;
    margin-right: 20px;
    cursor: pointer;
    color: #42b983;
}
.dialog-title {
    height: 30px;
    line-height: 30px;
    width: 170px;
    margin: 0 auto;
}
.dialogimg {
    display: block;
    margin: 0 auto;
}
.textarea-name {
    font-size: 12px;
    font-family: "\5FAE\8F6F\96C5\9ED1";
}
@media screen and (max-width: 1366px) {
    .up-data-btn {
        width: 230px;
        height: 240px;
        /* margin-left: 20px; */
        display: block;
        background: #fff;
        outline: none;
        border: 1px dashed #ccc;
        color: #ccc;
        font-size: 15px;
    }
    .upload-demo-box {
        width: 250px;
        height: 250px;
        vertical-align: bottom;
        display: inline-block;
    }
    .upload-demo {
        margin-top: 10px;
    }
    .img-box {
        width: 250px;
        height: 250px;
        margin-top: 10px;
        margin-right: 20px;
        position: relative;
        display: inline-block;
    }
}
@media screen and (max-width: 1334px) {
    .Append-basic-temlate-countent {
        max-width: 300px;
        min-width: 200px;
        width: 15%;
        height: 100%;
        padding: 20px;
        float: left;
    }
    .content-box {
        float: left;
        width: 80%;
        height: 100%;
        overflow-y: scroll;
        /*border: 1px solid red;*/
    }
}
@media screen and (max-width: 1024px) {
    .Append-basic-temlate {
        width: 1024px;
    }
    .header-top {
        display: none;
    }
    .Append-basic-temlate-countent {
        width: 180px;
        height: 100%;
        float: left;
    }
    .header {
        height: 100%;
        width: 180px;
        clear: both;
    }
    .content-box {
        float: left;
        width: 820px;
        height: 100%;
        overflow-y: scroll;
        /*border: 1px solid red;*/
    }
    .up-data-btn {
        width: 160px;
        height: 170px;
    }
    .upload-demo-box {
        width: 180px;
        height: 180px;
        vertical-align: bottom;
        display: inline-block;
    }
    .upload-demo {
        margin-top: 0;
    }
    .img-box {
        width: 180px;
        height: 170px;
        margin-top: 10px;
        margin-right: 10px;
        position: relative;
        display: inline-block;
    }
}
</style>
