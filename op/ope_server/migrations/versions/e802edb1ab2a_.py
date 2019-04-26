"""empty message

Revision ID: e802edb1ab2a
Revises: 
Create Date: 2019-04-23 19:21:11.676000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e802edb1ab2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('journals',
    sa.Column('journalized_id', sa.INTEGER(), nullable=False),
    sa.Column('journalized_type', sa.String(length=30), nullable=True),
    sa.Column('user_id', sa.String(length=30), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('journalized_id'),
    schema='public'
    )
    op.create_table('projects',
    sa.Column('proj_id', sa.Integer(), nullable=False),
    sa.Column('proj_name', sa.String(length=1024), nullable=True),
    sa.Column('describe', sa.String(length=1024), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('proj_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_projects_proj_name'), 'projects', ['proj_name'], unique=False, schema='public')
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_emp_id', sa.String(length=100), nullable=True),
    sa.Column('user_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_users_user_name'), 'users', ['user_name'], unique=False, schema='public')
    op.create_table('conditions',
    sa.Column('condition_id', sa.Integer(), nullable=False),
    sa.Column('proj_id', sa.Integer(), nullable=True),
    sa.Column('condition', sa.String(length=1024), nullable=True),
    sa.Column('view_model', sa.String(length=1024), nullable=True),
    sa.ForeignKeyConstraint(['proj_id'], ['public.projects.proj_id'], ),
    sa.PrimaryKeyConstraint('condition_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_conditions_proj_id'), 'conditions', ['proj_id'], unique=False, schema='public')
    op.create_table('displays',
    sa.Column('display_id', sa.Integer(), nullable=False),
    sa.Column('proj_id', sa.Integer(), nullable=True),
    sa.Column('display', sa.String(length=256), nullable=True),
    sa.Column('fun_of_model', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['proj_id'], ['public.projects.proj_id'], ),
    sa.PrimaryKeyConstraint('display_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_displays_proj_id'), 'displays', ['proj_id'], unique=False, schema='public')
    op.create_table('events',
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('proj_id', sa.Integer(), nullable=True),
    sa.Column('event', sa.String(length=256), nullable=True),
    sa.Column('trigger', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['proj_id'], ['public.projects.proj_id'], ),
    sa.PrimaryKeyConstraint('event_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_events_proj_id'), 'events', ['proj_id'], unique=False, schema='public')
    op.create_table('journal_briefs',
    sa.Column('j_brief_id', sa.INTEGER(), nullable=False),
    sa.Column('journalized_id', sa.INTEGER(), nullable=True),
    sa.Column('key_id', sa.INTEGER(), nullable=True),
    sa.Column('table_name', sa.String(length=100), nullable=True),
    sa.Column('action', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['journalized_id'], ['public.journals.journalized_id'], ),
    sa.PrimaryKeyConstraint('j_brief_id'),
    schema='public'
    )
    op.create_table('ope_types',
    sa.Column('ope_id', sa.Integer(), nullable=False),
    sa.Column('proj_id', sa.Integer(), nullable=True),
    sa.Column('ope_type', sa.String(length=256), nullable=True),
    sa.Column('ope_event', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['proj_id'], ['public.projects.proj_id'], ),
    sa.PrimaryKeyConstraint('ope_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_ope_types_proj_id'), 'ope_types', ['proj_id'], unique=False, schema='public')
    op.create_table('properties',
    sa.Column('property_id', sa.Integer(), nullable=False),
    sa.Column('proj_id', sa.Integer(), nullable=True),
    sa.Column('property_type', sa.String(length=256), nullable=True),
    sa.Column('property', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['proj_id'], ['public.projects.proj_id'], ),
    sa.PrimaryKeyConstraint('property_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_properties_proj_id'), 'properties', ['proj_id'], unique=False, schema='public')
    op.create_table('screen',
    sa.Column('screen_gid', sa.Integer(), nullable=False),
    sa.Column('proj_id', sa.Integer(), nullable=True),
    sa.Column('screen_uuid', sa.String(length=100), nullable=True),
    sa.Column('screen_id', sa.String(length=100), nullable=True),
    sa.Column('screen_name', sa.String(length=50), nullable=True),
    sa.Column('outline', sa.String(length=1024), nullable=True),
    sa.Column('screen_disp_rect', sa.String(length=1024), nullable=True),
    sa.Column('screen_disp_pic', sa.String(length=1024), nullable=True),
    sa.Column('image_dir', sa.String(length=256), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('locked', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['proj_id'], ['public.projects.proj_id'], ),
    sa.PrimaryKeyConstraint('screen_gid'),
    schema='public'
    )
    op.create_index(op.f('ix_public_screen_locked'), 'screen', ['locked'], unique=False, schema='public')
    op.create_index(op.f('ix_public_screen_proj_id'), 'screen', ['proj_id'], unique=False, schema='public')
    op.create_table('available_model',
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.Column('screen_id', sa.Integer(), nullable=True),
    sa.Column('model_info', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['screen_id'], ['public.screen.screen_gid'], ),
    sa.PrimaryKeyConstraint('model_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_available_model_screen_id'), 'available_model', ['screen_id'], unique=False, schema='public')
    op.create_table('chapter1',
    sa.Column('chapter1_id', sa.Integer(), nullable=False),
    sa.Column('screen_gid', sa.Integer(), nullable=True),
    sa.Column('display_chapter', sa.String(length=10), nullable=True),
    sa.Column('display_state_no', sa.String(length=10), nullable=True),
    sa.Column('parts_number', sa.String(length=256), nullable=True),
    sa.Column('display_sub_chapter', sa.String(length=10), nullable=True),
    sa.Column('parts_name', sa.String(length=256), nullable=True),
    sa.Column('display_content', sa.String(length=256), nullable=True),
    sa.Column('display_formula', sa.String(length=256), nullable=True),
    sa.Column('display_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('display_action', sa.Integer(), nullable=True),
    sa.Column('display_condition', sa.Integer(), nullable=True),
    sa.Column('display_property', sa.Integer(), nullable=True),
    sa.Column('data_range', sa.String(length=256), nullable=True),
    sa.Column('display_remark', sa.String(length=256), nullable=True),
    sa.Column('display_uuid', sa.String(length=256), nullable=True),
    sa.Column('display_parts_type', sa.String(length=256), nullable=True),
    sa.Column('display_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('string_id', sa.String(length=256), nullable=True),
    sa.Column('display_default_value', sa.String(length=256), nullable=True),
    sa.Column('display_states', sa.String(length=256), nullable=True),
    sa.Column('visible', sa.String(length=256), nullable=True),
    sa.Column('has_disp_info', sa.String(length=10), nullable=True),
    sa.Column('parts_id', sa.String(length=256), nullable=True),
    sa.Column('display_rect', sa.String(length=1024), nullable=True),
    sa.ForeignKeyConstraint(['display_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['display_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['display_property'], ['public.properties.property_id'], ),
    sa.ForeignKeyConstraint(['screen_gid'], ['public.screen.screen_gid'], ),
    sa.PrimaryKeyConstraint('chapter1_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_chapter1_display_action'), 'chapter1', ['display_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter1_display_condition'), 'chapter1', ['display_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter1_display_property'), 'chapter1', ['display_property'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter1_has_disp_info'), 'chapter1', ['has_disp_info'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter1_screen_gid'), 'chapter1', ['screen_gid'], unique=False, schema='public')
    op.create_table('chapter2',
    sa.Column('chapter2_id', sa.Integer(), nullable=False),
    sa.Column('screen_gid', sa.Integer(), nullable=True),
    sa.Column('active_chapter', sa.String(length=10), nullable=True),
    sa.Column('active_sub_chapter', sa.String(length=10), nullable=True),
    sa.Column('active_state_no', sa.String(length=10), nullable=True),
    sa.Column('active_no', sa.String(length=10), nullable=True),
    sa.Column('active_btn_name', sa.String(length=256), nullable=True),
    sa.Column('active_formula', sa.String(length=256), nullable=True),
    sa.Column('active_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('active_condition', sa.Integer(), nullable=True),
    sa.Column('active_action', sa.Integer(), nullable=True),
    sa.Column('active_property', sa.Integer(), nullable=True),
    sa.Column('active_during_driving', sa.String(length=256), nullable=True),
    sa.Column('active_remark', sa.String(length=256), nullable=True),
    sa.Column('active_uuid', sa.String(length=256), nullable=True),
    sa.Column('active_parts_type', sa.String(length=256), nullable=True),
    sa.Column('active_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('active_default_value', sa.String(length=256), nullable=True),
    sa.Column('active_states', sa.String(length=256), nullable=True),
    sa.Column('has_disp_info', sa.String(length=10), nullable=True),
    sa.Column('active', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['active_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['active_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['active_property'], ['public.properties.property_id'], ),
    sa.ForeignKeyConstraint(['screen_gid'], ['public.screen.screen_gid'], ),
    sa.PrimaryKeyConstraint('chapter2_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_chapter2_active_action'), 'chapter2', ['active_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter2_active_condition'), 'chapter2', ['active_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter2_active_property'), 'chapter2', ['active_property'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter2_has_disp_info'), 'chapter2', ['has_disp_info'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter2_screen_gid'), 'chapter2', ['screen_gid'], unique=False, schema='public')
    op.create_table('chapter3',
    sa.Column('chapter3_id', sa.Integer(), nullable=False),
    sa.Column('screen_gid', sa.Integer(), nullable=True),
    sa.Column('action_chapter', sa.String(length=10), nullable=True),
    sa.Column('action_sub_chapter', sa.String(length=10), nullable=True),
    sa.Column('action_state_no', sa.String(length=10), nullable=True),
    sa.Column('action_no', sa.String(length=10), nullable=True),
    sa.Column('action_btn_name', sa.String(length=256), nullable=True),
    sa.Column('action_ope', sa.Integer(), nullable=True),
    sa.Column('action_formula', sa.String(length=256), nullable=True),
    sa.Column('action_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('action_condition', sa.Integer(), nullable=True),
    sa.Column('action_action', sa.Integer(), nullable=True),
    sa.Column('action_trans', sa.String(length=256), nullable=True),
    sa.Column('action_sound', sa.String(length=256), nullable=True),
    sa.Column('action_remark', sa.String(length=256), nullable=True),
    sa.Column('action_uuid', sa.String(length=256), nullable=True),
    sa.Column('action_parts_type', sa.String(length=256), nullable=True),
    sa.Column('action_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('action_observer', sa.String(length=256), nullable=True),
    sa.Column('action_reply', sa.String(length=256), nullable=True),
    sa.Column('action_trans_type', sa.String(length=256), nullable=True),
    sa.Column('action_trans_id', sa.String(length=256), nullable=True),
    sa.Column('active_states', sa.String(length=256), nullable=True),
    sa.Column('has_action_info', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['action_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['action_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['action_ope'], ['public.ope_types.ope_id'], ),
    sa.ForeignKeyConstraint(['screen_gid'], ['public.screen.screen_gid'], ),
    sa.PrimaryKeyConstraint('chapter3_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_chapter3_action_action'), 'chapter3', ['action_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter3_action_condition'), 'chapter3', ['action_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter3_action_ope'), 'chapter3', ['action_ope'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter3_has_action_info'), 'chapter3', ['has_action_info'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter3_screen_gid'), 'chapter3', ['screen_gid'], unique=False, schema='public')
    op.create_table('chapter4',
    sa.Column('chapter4_id', sa.Integer(), nullable=False),
    sa.Column('screen_gid', sa.Integer(), nullable=True),
    sa.Column('hk_chapter', sa.String(length=10), nullable=True),
    sa.Column('hk_sub_chapter', sa.String(length=10), nullable=True),
    sa.Column('hk_state_no', sa.String(length=10), nullable=True),
    sa.Column('hk_no', sa.String(length=10), nullable=True),
    sa.Column('hk_name', sa.String(length=256), nullable=True),
    sa.Column('hk_dev_name', sa.String(length=256), nullable=True),
    sa.Column('hk_ope', sa.Integer(), nullable=True),
    sa.Column('hk_formula', sa.String(length=256), nullable=True),
    sa.Column('hk_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('hk_condition', sa.Integer(), nullable=True),
    sa.Column('hk_action', sa.Integer(), nullable=True),
    sa.Column('hk_trans', sa.String(length=256), nullable=True),
    sa.Column('hk_sound', sa.String(length=256), nullable=True),
    sa.Column('hk_during_driving', sa.String(length=256), nullable=True),
    sa.Column('hk_remark', sa.String(length=256), nullable=True),
    sa.Column('hk_uuid', sa.String(length=256), nullable=True),
    sa.Column('hk_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('hk_observer', sa.String(length=256), nullable=True),
    sa.Column('hk_reply', sa.String(length=256), nullable=True),
    sa.Column('hk_trans_type', sa.String(length=256), nullable=True),
    sa.Column('hk_trans_id', sa.String(length=256), nullable=True),
    sa.Column('hk_dev_type', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['hk_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['hk_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['hk_ope'], ['public.ope_types.ope_id'], ),
    sa.ForeignKeyConstraint(['screen_gid'], ['public.screen.screen_gid'], ),
    sa.PrimaryKeyConstraint('chapter4_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_chapter4_hk_action'), 'chapter4', ['hk_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter4_hk_condition'), 'chapter4', ['hk_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter4_hk_ope'), 'chapter4', ['hk_ope'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter4_screen_gid'), 'chapter4', ['screen_gid'], unique=False, schema='public')
    op.create_table('chapter5',
    sa.Column('chapter5_id', sa.Integer(), nullable=False),
    sa.Column('screen_gid', sa.Integer(), nullable=True),
    sa.Column('init_chapter', sa.String(length=10), nullable=True),
    sa.Column('init_no', sa.String(length=10), nullable=True),
    sa.Column('init_state_no', sa.String(length=10), nullable=True),
    sa.Column('init_status', sa.String(length=256), nullable=True),
    sa.Column('init_formula', sa.String(length=256), nullable=True),
    sa.Column('init_condition', sa.Integer(), nullable=True),
    sa.Column('init_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('init_action', sa.Integer(), nullable=True),
    sa.Column('init_trans', sa.String(length=1024), nullable=True),
    sa.Column('init_remark', sa.String(length=1024), nullable=True),
    sa.Column('init_uuid', sa.String(length=256), nullable=True),
    sa.Column('init_event', sa.String(length=256), nullable=True),
    sa.Column('init_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('init_observer', sa.String(length=1024), nullable=True),
    sa.Column('init_reply', sa.String(length=1024), nullable=True),
    sa.Column('init_trans_type', sa.String(length=256), nullable=True),
    sa.Column('init_trans_id', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['init_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['init_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['screen_gid'], ['public.screen.screen_gid'], ),
    sa.PrimaryKeyConstraint('chapter5_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_chapter5_init_action'), 'chapter5', ['init_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter5_init_condition'), 'chapter5', ['init_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter5_screen_gid'), 'chapter5', ['screen_gid'], unique=False, schema='public')
    op.create_table('chapter6',
    sa.Column('chapter6_id', sa.Integer(), nullable=False),
    sa.Column('screen_gid', sa.Integer(), nullable=True),
    sa.Column('status_change_chapter', sa.String(length=10), nullable=True),
    sa.Column('status_change_sub_chapter', sa.String(length=10), nullable=True),
    sa.Column('status_change_no', sa.String(length=10), nullable=True),
    sa.Column('status_change_state_no', sa.String(length=10), nullable=True),
    sa.Column('status_change_name', sa.String(length=256), nullable=True),
    sa.Column('status_change_f_formula', sa.String(length=256), nullable=True),
    sa.Column('status_change_f_condition', sa.Integer(), nullable=True),
    sa.Column('status_change_f_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('status_change_f_action', sa.Integer(), nullable=True),
    sa.Column('status_change_b_formula', sa.String(length=1024), nullable=True),
    sa.Column('status_change_b_condition', sa.Integer(), nullable=True),
    sa.Column('status_change_b_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('status_change_b_action', sa.Integer(), nullable=True),
    sa.Column('status_change_i_formula', sa.String(length=1024), nullable=True),
    sa.Column('status_change_i_condition', sa.Integer(), nullable=True),
    sa.Column('status_change_i_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('status_change_i_action', sa.Integer(), nullable=True),
    sa.Column('status_change_uuid', sa.String(length=256), nullable=True),
    sa.Column('status_change_event', sa.String(length=256), nullable=True),
    sa.Column('status_change_f_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('status_change_f_observer', sa.String(length=1024), nullable=True),
    sa.Column('status_change_f_reply', sa.String(length=1024), nullable=True),
    sa.Column('status_change_b_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('status_change_b_observer', sa.String(length=1024), nullable=True),
    sa.Column('status_change_b_reply', sa.String(length=1024), nullable=True),
    sa.Column('status_change_i_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('status_change_i_observer', sa.String(length=1024), nullable=True),
    sa.Column('status_change_i_reply', sa.String(length=1024), nullable=True),
    sa.Column('status_change_b_trans', sa.String(length=256), nullable=True),
    sa.Column('status_change_f_trans', sa.String(length=256), nullable=True),
    sa.Column('status_change_i_trans', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['screen_gid'], ['public.screen.screen_gid'], ),
    sa.ForeignKeyConstraint(['status_change_b_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['status_change_b_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['status_change_f_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['status_change_f_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['status_change_i_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['status_change_i_condition'], ['public.conditions.condition_id'], ),
    sa.PrimaryKeyConstraint('chapter6_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_chapter6_screen_gid'), 'chapter6', ['screen_gid'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter6_status_change_b_action'), 'chapter6', ['status_change_b_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter6_status_change_b_condition'), 'chapter6', ['status_change_b_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter6_status_change_f_action'), 'chapter6', ['status_change_f_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter6_status_change_f_condition'), 'chapter6', ['status_change_f_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter6_status_change_i_action'), 'chapter6', ['status_change_i_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter6_status_change_i_condition'), 'chapter6', ['status_change_i_condition'], unique=False, schema='public')
    op.create_table('chapter7',
    sa.Column('chapter7_id', sa.Integer(), nullable=False),
    sa.Column('screen_gid', sa.Integer(), nullable=True),
    sa.Column('transition_chapter', sa.String(length=10), nullable=True),
    sa.Column('transition_sub_chapter', sa.String(length=10), nullable=True),
    sa.Column('transition_no', sa.String(length=10), nullable=True),
    sa.Column('transition_state_no', sa.String(length=10), nullable=True),
    sa.Column('transition_name', sa.String(length=256), nullable=True),
    sa.Column('transition_f_formula', sa.String(length=256), nullable=True),
    sa.Column('transition_f_condition', sa.Integer(), nullable=True),
    sa.Column('transition_f_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('transition_f_action', sa.Integer(), nullable=True),
    sa.Column('transition_b_formula', sa.String(length=1024), nullable=True),
    sa.Column('transition_b_condition', sa.Integer(), nullable=True),
    sa.Column('transition_b_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('transition_b_action', sa.Integer(), nullable=True),
    sa.Column('transition_i_formula', sa.String(length=1024), nullable=True),
    sa.Column('transition_i_condition', sa.Integer(), nullable=True),
    sa.Column('transition_i_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('transition_i_action', sa.Integer(), nullable=True),
    sa.Column('transition_uuid', sa.String(length=256), nullable=True),
    sa.Column('transition_event', sa.String(length=256), nullable=True),
    sa.Column('transition_b_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('transition_b_observer', sa.String(length=1024), nullable=True),
    sa.Column('transition_b_reply', sa.String(length=1024), nullable=True),
    sa.Column('transition_f_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('transition_f_observer', sa.String(length=1024), nullable=True),
    sa.Column('transition_f_reply', sa.String(length=1024), nullable=True),
    sa.Column('transition_i_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('transition_i_observer', sa.String(length=1024), nullable=True),
    sa.Column('transition_i_reply', sa.String(length=1024), nullable=True),
    sa.Column('transition_b_trans', sa.String(length=256), nullable=True),
    sa.Column('transition_f_trans', sa.String(length=256), nullable=True),
    sa.Column('transition_i_trans', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['screen_gid'], ['public.screen.screen_gid'], ),
    sa.ForeignKeyConstraint(['transition_b_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['transition_b_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['transition_f_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['transition_f_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['transition_i_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['transition_i_condition'], ['public.conditions.condition_id'], ),
    sa.PrimaryKeyConstraint('chapter7_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_chapter7_screen_gid'), 'chapter7', ['screen_gid'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter7_transition_b_action'), 'chapter7', ['transition_b_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter7_transition_b_condition'), 'chapter7', ['transition_b_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter7_transition_f_action'), 'chapter7', ['transition_f_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter7_transition_f_condition'), 'chapter7', ['transition_f_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter7_transition_i_action'), 'chapter7', ['transition_i_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter7_transition_i_condition'), 'chapter7', ['transition_i_condition'], unique=False, schema='public')
    op.create_table('chapter8',
    sa.Column('chapter8_id', sa.Integer(), nullable=False),
    sa.Column('screen_gid', sa.Integer(), nullable=True),
    sa.Column('trig_chapter', sa.String(length=10), nullable=True),
    sa.Column('trig_sub_chapter', sa.String(length=10), nullable=True),
    sa.Column('trig_state_no', sa.String(length=10), nullable=True),
    sa.Column('trig_no', sa.String(length=10), nullable=True),
    sa.Column('trig_name', sa.String(length=256), nullable=True),
    sa.Column('trig_formula', sa.String(length=256), nullable=True),
    sa.Column('trig_condition', sa.Integer(), nullable=True),
    sa.Column('trig_condition_branch', sa.String(length=256), nullable=True),
    sa.Column('trig_action', sa.Integer(), nullable=True),
    sa.Column('trig_trans', sa.String(length=256), nullable=True),
    sa.Column('trig_sound', sa.String(length=256), nullable=True),
    sa.Column('trig_timer', sa.String(length=256), nullable=True),
    sa.Column('trig_remark', sa.String(length=1024), nullable=True),
    sa.Column('trig_uuid', sa.String(length=256), nullable=True),
    sa.Column('trig_trig', sa.Integer(), nullable=True),
    sa.Column('trig_event', sa.String(length=256), nullable=True),
    sa.Column('trig_condition_model_branch', sa.String(length=256), nullable=True),
    sa.Column('trig_observer', sa.String(length=1024), nullable=True),
    sa.Column('trig_reply', sa.String(length=1024), nullable=True),
    sa.Column('trig_trans_type', sa.String(length=256), nullable=True),
    sa.Column('trig_trans_id', sa.String(length=256), nullable=True),
    sa.Column('trig_signal', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['screen_gid'], ['public.screen.screen_gid'], ),
    sa.ForeignKeyConstraint(['trig_action'], ['public.displays.display_id'], ),
    sa.ForeignKeyConstraint(['trig_condition'], ['public.conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['trig_trig'], ['public.events.event_id'], ),
    sa.PrimaryKeyConstraint('chapter8_id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_chapter8_screen_gid'), 'chapter8', ['screen_gid'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter8_trig_action'), 'chapter8', ['trig_action'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter8_trig_condition'), 'chapter8', ['trig_condition'], unique=False, schema='public')
    op.create_index(op.f('ix_public_chapter8_trig_trig'), 'chapter8', ['trig_trig'], unique=False, schema='public')
    op.create_table('journal_details',
    sa.Column('j_detail_id', sa.INTEGER(), nullable=False),
    sa.Column('j_brief_id', sa.INTEGER(), nullable=True),
    sa.Column('column_name', sa.String(length=100), nullable=True),
    sa.Column('val', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['j_brief_id'], ['public.journal_briefs.j_brief_id'], ),
    sa.PrimaryKeyConstraint('j_detail_id'),
    schema='public'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journal_details', schema='public')
    op.drop_index(op.f('ix_public_chapter8_trig_trig'), table_name='chapter8', schema='public')
    op.drop_index(op.f('ix_public_chapter8_trig_condition'), table_name='chapter8', schema='public')
    op.drop_index(op.f('ix_public_chapter8_trig_action'), table_name='chapter8', schema='public')
    op.drop_index(op.f('ix_public_chapter8_screen_gid'), table_name='chapter8', schema='public')
    op.drop_table('chapter8', schema='public')
    op.drop_index(op.f('ix_public_chapter7_transition_i_condition'), table_name='chapter7', schema='public')
    op.drop_index(op.f('ix_public_chapter7_transition_i_action'), table_name='chapter7', schema='public')
    op.drop_index(op.f('ix_public_chapter7_transition_f_condition'), table_name='chapter7', schema='public')
    op.drop_index(op.f('ix_public_chapter7_transition_f_action'), table_name='chapter7', schema='public')
    op.drop_index(op.f('ix_public_chapter7_transition_b_condition'), table_name='chapter7', schema='public')
    op.drop_index(op.f('ix_public_chapter7_transition_b_action'), table_name='chapter7', schema='public')
    op.drop_index(op.f('ix_public_chapter7_screen_gid'), table_name='chapter7', schema='public')
    op.drop_table('chapter7', schema='public')
    op.drop_index(op.f('ix_public_chapter6_status_change_i_condition'), table_name='chapter6', schema='public')
    op.drop_index(op.f('ix_public_chapter6_status_change_i_action'), table_name='chapter6', schema='public')
    op.drop_index(op.f('ix_public_chapter6_status_change_f_condition'), table_name='chapter6', schema='public')
    op.drop_index(op.f('ix_public_chapter6_status_change_f_action'), table_name='chapter6', schema='public')
    op.drop_index(op.f('ix_public_chapter6_status_change_b_condition'), table_name='chapter6', schema='public')
    op.drop_index(op.f('ix_public_chapter6_status_change_b_action'), table_name='chapter6', schema='public')
    op.drop_index(op.f('ix_public_chapter6_screen_gid'), table_name='chapter6', schema='public')
    op.drop_table('chapter6', schema='public')
    op.drop_index(op.f('ix_public_chapter5_screen_gid'), table_name='chapter5', schema='public')
    op.drop_index(op.f('ix_public_chapter5_init_condition'), table_name='chapter5', schema='public')
    op.drop_index(op.f('ix_public_chapter5_init_action'), table_name='chapter5', schema='public')
    op.drop_table('chapter5', schema='public')
    op.drop_index(op.f('ix_public_chapter4_screen_gid'), table_name='chapter4', schema='public')
    op.drop_index(op.f('ix_public_chapter4_hk_ope'), table_name='chapter4', schema='public')
    op.drop_index(op.f('ix_public_chapter4_hk_condition'), table_name='chapter4', schema='public')
    op.drop_index(op.f('ix_public_chapter4_hk_action'), table_name='chapter4', schema='public')
    op.drop_table('chapter4', schema='public')
    op.drop_index(op.f('ix_public_chapter3_screen_gid'), table_name='chapter3', schema='public')
    op.drop_index(op.f('ix_public_chapter3_has_action_info'), table_name='chapter3', schema='public')
    op.drop_index(op.f('ix_public_chapter3_action_ope'), table_name='chapter3', schema='public')
    op.drop_index(op.f('ix_public_chapter3_action_condition'), table_name='chapter3', schema='public')
    op.drop_index(op.f('ix_public_chapter3_action_action'), table_name='chapter3', schema='public')
    op.drop_table('chapter3', schema='public')
    op.drop_index(op.f('ix_public_chapter2_screen_gid'), table_name='chapter2', schema='public')
    op.drop_index(op.f('ix_public_chapter2_has_disp_info'), table_name='chapter2', schema='public')
    op.drop_index(op.f('ix_public_chapter2_active_property'), table_name='chapter2', schema='public')
    op.drop_index(op.f('ix_public_chapter2_active_condition'), table_name='chapter2', schema='public')
    op.drop_index(op.f('ix_public_chapter2_active_action'), table_name='chapter2', schema='public')
    op.drop_table('chapter2', schema='public')
    op.drop_index(op.f('ix_public_chapter1_screen_gid'), table_name='chapter1', schema='public')
    op.drop_index(op.f('ix_public_chapter1_has_disp_info'), table_name='chapter1', schema='public')
    op.drop_index(op.f('ix_public_chapter1_display_property'), table_name='chapter1', schema='public')
    op.drop_index(op.f('ix_public_chapter1_display_condition'), table_name='chapter1', schema='public')
    op.drop_index(op.f('ix_public_chapter1_display_action'), table_name='chapter1', schema='public')
    op.drop_table('chapter1', schema='public')
    op.drop_index(op.f('ix_public_available_model_screen_id'), table_name='available_model', schema='public')
    op.drop_table('available_model', schema='public')
    op.drop_index(op.f('ix_public_screen_proj_id'), table_name='screen', schema='public')
    op.drop_index(op.f('ix_public_screen_locked'), table_name='screen', schema='public')
    op.drop_table('screen', schema='public')
    op.drop_index(op.f('ix_public_properties_proj_id'), table_name='properties', schema='public')
    op.drop_table('properties', schema='public')
    op.drop_index(op.f('ix_public_ope_types_proj_id'), table_name='ope_types', schema='public')
    op.drop_table('ope_types', schema='public')
    op.drop_table('journal_briefs', schema='public')
    op.drop_index(op.f('ix_public_events_proj_id'), table_name='events', schema='public')
    op.drop_table('events', schema='public')
    op.drop_index(op.f('ix_public_displays_proj_id'), table_name='displays', schema='public')
    op.drop_table('displays', schema='public')
    op.drop_index(op.f('ix_public_conditions_proj_id'), table_name='conditions', schema='public')
    op.drop_table('conditions', schema='public')
    op.drop_index(op.f('ix_public_users_user_name'), table_name='users', schema='public')
    op.drop_table('users', schema='public')
    op.drop_index(op.f('ix_public_projects_proj_name'), table_name='projects', schema='public')
    op.drop_table('projects', schema='public')
    op.drop_table('journals', schema='public')
    # ### end Alembic commands ###
