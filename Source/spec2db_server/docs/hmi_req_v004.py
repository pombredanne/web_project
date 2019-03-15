# -*- coding: UTF-8 -*-


class HMIReqV004():
    def __init__(self):
        self.doc_type = 'HMIREQ'
        self.version = '0.04'
        self.doc_format_dict = {
            'represent_req': {
                'xlsname': 'H/U要件定義書から転記->NEDL代表要件',
                'xlspos': [(1, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'arl_id': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->ARLID',
                'xlspos': [(2, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'major_category': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->大分類',
                'xlspos': [(3, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'medium_category': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->中分類',
                'xlspos': [(4, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'small_category': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->小分類',
                'xlspos': [(5, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'detail': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->詳細',
                'xlspos': [(6, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'basic_req': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->基本要件',
                'xlspos': [(7, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'req': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->要件',
                'xlspos': [(8, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'status': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->状態',
                'xlspos': [(9, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'trigger': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->トリガ',
                'xlspos': [(10, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'action': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->動作',
                'xlspos': [(11, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'remark': {
                'xlsname': 'H/U要件定義書から転記->ARLから転記->備考',
                'xlspos': [(12, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hmi_spec_no': {
                'xlsname': 'H/U要件定義書から転記->HMI仕様書->仕様書番号',
                'xlspos': [(13, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hmi_version': {
                'xlsname': 'H/U要件定義書から転記->HMI仕様書->バージョン',
                'xlspos': [(14, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hmi_file_name': {
                'xlsname': 'H/U要件定義書から転記->HMI仕様書->ファイル名',
                'xlspos': [(15, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hmi_chapter': {
                'xlsname': 'H/U要件定義書から転記->HMI仕様書->章',
                'xlspos': [(16, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hmi_page': {
                'xlsname': 'H/U要件定義書から転記->HMI仕様書->Page',
                'xlspos': [(17, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hmi_screen_id': {
                'xlsname': 'H/U要件定義書から転記->HMI仕様書->画面ID',
                'xlspos': [(18, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'func_spec_no': {
                'xlsname': 'H/U要件定義書から転記->機能仕様書->仕様書番号',
                'xlspos': [(19, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'func_version': {
                'xlsname': 'H/U要件定義書から転記->機能仕様書->バージョン',
                'xlspos': [(20, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'func_file_name': {
                'xlsname': 'H/U要件定義書から転記->機能仕様書->ファイル名',
                'xlspos': [(21, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'func_chapter': {
                'xlsname': 'H/U要件定義書から転記->機能仕様書->章',
                'xlspos': [(22, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'func_page': {
                'xlsname': 'H/U要件定義書から転記->機能仕様書->Page',
                'xlspos': [(23, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hu_id': {
                'xlsname': 'H/U要件定義書から転記->H/U要件定義ID',
                'xlspos': [(24, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'unique_id': {
                'xlsname': 'H/U要件定義書から転記->ユニークID',
                'xlspos': [(25, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'amp': {
                'xlsname': 'H/U要件定義書から転記->オプション項目->AMP',
                'xlspos': [(26, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'dsrc': {
                'xlsname': 'H/U要件定義書から転記->オプション項目->DSRC',
                'xlspos': [(27, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'dcm': {
                'xlsname': 'H/U要件定義書から転記->オプション項目->DCM',
                'xlspos': [(28, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'rse': {
                'xlsname': 'H/U要件定義書から転記->オプション項目->RSE',
                'xlspos': [(29, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'touch_pad': {
                'xlsname': 'H/U要件定義書から転記->オプション項目->TouchPad',
                'xlspos': [(30, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'separate_disp': {
                'xlsname': 'H/U要件定義書から転記->オプション項目->SeparateDisp',
                'xlspos': [(31, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'system_conf': {
                'xlsname': 'H/U要件定義書から転記->システム構成',
                'xlspos': [(32, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'rel_requirement': {
                'xlsname': 'H/U要件定義書から転記->関連基本要件',
                'xlspos': [(33, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'exception': {
                'xlsname': 'H/U要件定義書から転記->除外',
                'xlspos': [(34, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'dcu_status': {
                'xlsname': 'H/U要件定義書から転記->H/U->DCU->状態',
                'xlspos': [(35, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'dcu_trigger': {
                'xlsname': 'H/U要件定義書から転記->H/U->DCU->トリガー',
                'xlspos': [(36, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'dcu_action': {
                'xlsname': 'H/U要件定義書から転記->H/U->DCU->動作',
                'xlspos': [(37, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'meu_status': {
                'xlsname': 'H/U要件定義書から転記->H/U->MEU->状態',
                'xlspos': [(38, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'meu_trigger': {
                'xlsname': 'H/U要件定義書から転記->H/U->MEU->トリガー',
                'xlspos': [(39, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'meu_action': {
                'xlsname': 'H/U要件定義書から転記->H/U->MEU->動作',
                'xlspos': [(40, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hu_category_id': {
                'xlsname': 'H/U要件定義書から転記->H/U分類ID',
                'xlspos': [(41, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'deal_flow': {
                'xlsname': '設計内容紐付け->処理フロー',
                'xlspos': [(42, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hmi_ds_screen_id': {
                'xlsname': '設計内容紐付け->HMI設計->画面ID',
                'xlspos': [(43, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hmi_ds_no': {
                'xlsname': '設計内容紐付け->HMI設計->部品番号',
                'xlspos': [(44, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'hmi_ds_remark': {
                'xlsname': '設計内容紐付け->HMI設計->備考',
                'xlspos': [(45, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'apl_ds_if_no': {
                'xlsname': '設計内容紐付け->アプリ設計->I/F番号',
                'xlspos': [(46, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'apl_ds_service': {
                'xlsname': '設計内容紐付け->アプリ設計->Service I/F',
                'xlspos': [(47, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'apl_ds_exception': {
                'xlsname': '設計内容紐付け->アプリ設計->除外対象',
                'xlspos': [(48, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'apl_ds_obj': {
                'xlsname': '設計内容紐付け->アプリ設計->対象アプリ',
                'xlspos': [(49, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'apl_ds_step': {
                'xlsname': '設計内容紐付け->アプリ設計->開発Step',
                'xlspos': [(50, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'apl_ds_remark': {
                'xlsname': '設計内容紐付け->アプリ設計->備考',
                'xlspos': [(51, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'sys_ds_name': {
                'xlsname': '設計内容紐付け->システム設計書名',
                'xlspos': [(52, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'decompose_id': {
                'xlsname': '設計内容紐付け->分解ID',
                'xlspos': [(53, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'decompose_content': {
                'xlsname': '設計内容紐付け->分解内容',
                'xlspos': [(54, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'operation': {
                'xlsname': '設計内容紐付け->操作',
                'xlspos': [(55, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'dest_name': {
                'xlsname': '設計内容紐付け->テスト\n項目',
                'xlspos': [(56, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'testcase_num': {
                'xlsname': '設計内容紐付け->テストケース件数',
                'xlspos': [(57, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'sys_remark': {
                'xlsname': '設計内容紐付け->備考',
                'xlspos': [(58, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'apl_status': {
                'xlsname': 'アプリ作成状態',
                'xlspos': [(59, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'sys_test_status': {
                'xlsname': 'システムテスト作成状態',
                'xlspos': [(60, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'sp29': {
                'xlsname': 'SP29',
                'xlspos': [(62, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'sp30': {
                'xlsname': 'SP30',
                'xlspos': [(63, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'sp31': {
                'xlsname': 'SP31',
                'xlspos': [(64, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'iauto_complete': {
                'xlsname': 'iAuto担当（SP29）',
                'xlspos': [(65, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'step': {
                'xlsname': 'Step',
                'xlspos': [(66, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'definition_id': {
                'xlsname': 'tagl要件定義ID',
                'xlspos': [(67, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'ana_unique_id': {
                'xlsname': 'uniqueID',
                'xlspos': [(68, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'seq_diagram_file': {
                'xlsname': '時序図文件',
                'xlspos': [(69, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'seq_diagram_no': {
                'xlsname': '時序図番号',
                'xlspos': [(70, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'application': {
                'xlsname': 'Application',
                'xlspos': [(71, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'ana_exception': {
                'xlsname': 'TAGL除外',
                'xlspos': [(72, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'is_represent_req': {
                'xlsname': '是否代表要件',
                'xlspos': [(73, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'parent_rep_req': {
                'xlsname': '親代表要件',
                'xlspos': [(74, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'new_date': {
                'xlsname': '新建日期',
                'xlspos': [(75, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'is_dalian': {
                'xlsname': 'APL是否为大连对应',
                'xlspos': [(76, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'charger': {
                'xlsname': '负责人',
                'xlspos': [(77, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'author': {
                'xlsname': '担当',
                'xlspos': [(78, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'apl_schedule': {
                'xlsname': 'APL日程',
                'xlspos': [(79, 5)],
                'datatype': 'DATETIME',
                'needcheck': True,
            },
            'it_schedule': {
                'xlsname': '结合日程',
                'xlspos': [(80, 5)],
                'datatype': 'DATETIME',
                'needcheck': True,
            },
            'apl_progress': {
                'xlsname': 'APL进度',
                'xlspos': [(81, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'it_progress': {
                'xlsname': '结合测试结果',
                'xlspos': [(82, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'it_release_ver': {
                'xlsname': '结合测试Release版本',
                'xlspos': [(83, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'it_file_name': {
                'xlsname': '结合测试书名称',
                'xlspos': [(84, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'it_nos': {
                'xlsname': '结合测试书番号',
                'xlspos': [(85, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'dev_status': {
                'xlsname': '开发状态',
                'xlspos': [(86, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'dev_status_detail': {
                'xlsname': '开发状态详细',
                'xlspos': [(87, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'dev_remark': {
                'xlsname': '备考',
                'xlspos': [(88, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'external_qa': {
                'xlsname': '外部QA番号',
                'xlspos': [(89, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'external_qa_status': {
                'xlsname': '外部QA状态',
                'xlspos': [(90, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'internal_qa': {
                'xlsname': '内部QA番号',
                'xlspos': [(91, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'internal_qa_status': {
                'xlsname': '内部QA状态',
                'xlspos': [(92, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'bug_no': {
                'xlsname': 'Bug番号',
                'xlspos': [(93, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'bug_status': {
                'xlsname': 'Bug状态',
                'xlspos': [(94, 5)],
                'datatype': 'STR',
                'needcheck': True,
            },
            'ng_num': {
                'xlsname': 'NG次数',
                'xlspos': [(95, 5)],
                'datatype': 'STR',
                'needcheck': False,
            },
        }
        self.xls_sheet_name = '要件详细'
        self.start_data_row = 6
        self.id_col = "hu_id"


if __name__ == '__main__':
    print len(HMIReqV004().doc_format_dict.keys())
    print len(set(HMIReqV004().doc_format_dict.keys()))