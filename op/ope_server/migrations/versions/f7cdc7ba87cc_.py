"""empty message

Revision ID: f7cdc7ba87cc
Revises: a75788f6a2ef
Create Date: 2019-04-24 15:51:39.649200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7cdc7ba87cc'
down_revision = 'a75788f6a2ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('available_model_screen_id_fkey', 'available_model', type_='foreignkey')
    op.create_foreign_key(None, 'available_model', 'screen', ['screen_id'], ['screen_gid'], source_schema='public', referent_schema='public')
    op.drop_constraint('chapter1_display_property_fkey', 'chapter1', type_='foreignkey')
    op.drop_constraint('chapter1_screen_gid_fkey', 'chapter1', type_='foreignkey')
    op.drop_constraint('chapter1_display_action_fkey', 'chapter1', type_='foreignkey')
    op.drop_constraint('chapter1_display_condition_fkey', 'chapter1', type_='foreignkey')
    op.create_foreign_key(None, 'chapter1', 'conditions', ['display_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter1', 'displays', ['display_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter1', 'properties', ['display_property'], ['property_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter1', 'screen', ['screen_gid'], ['screen_gid'], source_schema='public', referent_schema='public')
    op.drop_constraint('chapter2_active_condition_fkey', 'chapter2', type_='foreignkey')
    op.drop_constraint('chapter2_screen_gid_fkey', 'chapter2', type_='foreignkey')
    op.drop_constraint('chapter2_active_property_fkey', 'chapter2', type_='foreignkey')
    op.drop_constraint('chapter2_active_action_fkey', 'chapter2', type_='foreignkey')
    op.create_foreign_key(None, 'chapter2', 'conditions', ['active_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter2', 'screen', ['screen_gid'], ['screen_gid'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter2', 'properties', ['active_property'], ['property_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter2', 'displays', ['active_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('chapter3_action_ope_fkey', 'chapter3', type_='foreignkey')
    op.drop_constraint('chapter3_screen_gid_fkey', 'chapter3', type_='foreignkey')
    op.drop_constraint('chapter3_action_action_fkey', 'chapter3', type_='foreignkey')
    op.drop_constraint('chapter3_action_condition_fkey', 'chapter3', type_='foreignkey')
    op.create_foreign_key(None, 'chapter3', 'conditions', ['action_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter3', 'ope_types', ['action_ope'], ['ope_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter3', 'screen', ['screen_gid'], ['screen_gid'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter3', 'displays', ['action_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('chapter4_screen_gid_fkey', 'chapter4', type_='foreignkey')
    op.drop_constraint('chapter4_hk_action_fkey', 'chapter4', type_='foreignkey')
    op.drop_constraint('chapter4_hk_condition_fkey', 'chapter4', type_='foreignkey')
    op.drop_constraint('chapter4_hk_ope_fkey', 'chapter4', type_='foreignkey')
    op.create_foreign_key(None, 'chapter4', 'conditions', ['hk_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter4', 'displays', ['hk_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter4', 'ope_types', ['hk_ope'], ['ope_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter4', 'screen', ['screen_gid'], ['screen_gid'], source_schema='public', referent_schema='public')
    op.drop_constraint('chapter5_init_action_fkey', 'chapter5', type_='foreignkey')
    op.drop_constraint('chapter5_screen_gid_fkey', 'chapter5', type_='foreignkey')
    op.drop_constraint('chapter5_init_condition_fkey', 'chapter5', type_='foreignkey')
    op.create_foreign_key(None, 'chapter5', 'displays', ['init_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter5', 'screen', ['screen_gid'], ['screen_gid'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter5', 'conditions', ['init_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('chapter6_status_change_f_action_fkey', 'chapter6', type_='foreignkey')
    op.drop_constraint('chapter6_screen_gid_fkey', 'chapter6', type_='foreignkey')
    op.drop_constraint('chapter6_status_change_i_action_fkey', 'chapter6', type_='foreignkey')
    op.drop_constraint('chapter6_status_change_b_action_fkey', 'chapter6', type_='foreignkey')
    op.drop_constraint('chapter6_status_change_f_condition_fkey', 'chapter6', type_='foreignkey')
    op.drop_constraint('chapter6_status_change_i_condition_fkey', 'chapter6', type_='foreignkey')
    op.drop_constraint('chapter6_status_change_b_condition_fkey', 'chapter6', type_='foreignkey')
    op.create_foreign_key(None, 'chapter6', 'conditions', ['status_change_i_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter6', 'conditions', ['status_change_b_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter6', 'displays', ['status_change_f_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter6', 'screen', ['screen_gid'], ['screen_gid'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter6', 'displays', ['status_change_i_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter6', 'displays', ['status_change_b_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter6', 'conditions', ['status_change_f_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('chapter7_transition_b_condition_fkey', 'chapter7', type_='foreignkey')
    op.drop_constraint('chapter7_transition_i_condition_fkey', 'chapter7', type_='foreignkey')
    op.drop_constraint('chapter7_transition_f_condition_fkey', 'chapter7', type_='foreignkey')
    op.drop_constraint('chapter7_transition_i_action_fkey', 'chapter7', type_='foreignkey')
    op.drop_constraint('chapter7_transition_b_action_fkey', 'chapter7', type_='foreignkey')
    op.drop_constraint('chapter7_transition_f_action_fkey', 'chapter7', type_='foreignkey')
    op.drop_constraint('chapter7_screen_gid_fkey', 'chapter7', type_='foreignkey')
    op.create_foreign_key(None, 'chapter7', 'displays', ['transition_i_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter7', 'conditions', ['transition_f_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter7', 'displays', ['transition_f_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter7', 'conditions', ['transition_b_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter7', 'conditions', ['transition_i_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter7', 'displays', ['transition_b_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter7', 'screen', ['screen_gid'], ['screen_gid'], source_schema='public', referent_schema='public')
    op.drop_constraint('chapter8_screen_gid_fkey', 'chapter8', type_='foreignkey')
    op.drop_constraint('chapter8_trig_condition_fkey', 'chapter8', type_='foreignkey')
    op.drop_constraint('chapter8_trig_trig_fkey', 'chapter8', type_='foreignkey')
    op.drop_constraint('chapter8_trig_action_fkey', 'chapter8', type_='foreignkey')
    op.create_foreign_key(None, 'chapter8', 'displays', ['trig_action'], ['display_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter8', 'screen', ['screen_gid'], ['screen_gid'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter8', 'conditions', ['trig_condition'], ['condition_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'chapter8', 'events', ['trig_trig'], ['event_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('conditions_proj_id_fkey', 'conditions', type_='foreignkey')
    op.create_foreign_key(None, 'conditions', 'projects', ['proj_id'], ['proj_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('displays_proj_id_fkey', 'displays', type_='foreignkey')
    op.create_foreign_key(None, 'displays', 'projects', ['proj_id'], ['proj_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('events_proj_id_fkey', 'events', type_='foreignkey')
    op.create_foreign_key(None, 'events', 'projects', ['proj_id'], ['proj_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('journal_briefs_journalized_id_fkey', 'journal_briefs', type_='foreignkey')
    op.create_foreign_key(None, 'journal_briefs', 'journals', ['journalized_id'], ['journalized_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('journal_details_j_brief_id_fkey', 'journal_details', type_='foreignkey')
    op.create_foreign_key(None, 'journal_details', 'journal_briefs', ['j_brief_id'], ['j_brief_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('ope_types_proj_id_fkey', 'ope_types', type_='foreignkey')
    op.create_foreign_key(None, 'ope_types', 'projects', ['proj_id'], ['proj_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('properties_proj_id_fkey', 'properties', type_='foreignkey')
    op.create_foreign_key(None, 'properties', 'projects', ['proj_id'], ['proj_id'], source_schema='public', referent_schema='public')
    op.drop_constraint('screen_proj_id_fkey', 'screen', type_='foreignkey')
    op.drop_constraint('screen_update_user_fkey', 'screen', type_='foreignkey')
    op.create_foreign_key(None, 'screen', 'projects', ['proj_id'], ['proj_id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'screen', 'users', ['update_user'], ['user_id'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'screen', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'screen', schema='public', type_='foreignkey')
    op.create_foreign_key('screen_update_user_fkey', 'screen', 'users', ['update_user'], ['user_id'])
    op.create_foreign_key('screen_proj_id_fkey', 'screen', 'projects', ['proj_id'], ['proj_id'])
    op.drop_constraint(None, 'properties', schema='public', type_='foreignkey')
    op.create_foreign_key('properties_proj_id_fkey', 'properties', 'projects', ['proj_id'], ['proj_id'])
    op.drop_constraint(None, 'ope_types', schema='public', type_='foreignkey')
    op.create_foreign_key('ope_types_proj_id_fkey', 'ope_types', 'projects', ['proj_id'], ['proj_id'])
    op.drop_constraint(None, 'journal_details', schema='public', type_='foreignkey')
    op.create_foreign_key('journal_details_j_brief_id_fkey', 'journal_details', 'journal_briefs', ['j_brief_id'], ['j_brief_id'])
    op.drop_constraint(None, 'journal_briefs', schema='public', type_='foreignkey')
    op.create_foreign_key('journal_briefs_journalized_id_fkey', 'journal_briefs', 'journals', ['journalized_id'], ['journalized_id'])
    op.drop_constraint(None, 'events', schema='public', type_='foreignkey')
    op.create_foreign_key('events_proj_id_fkey', 'events', 'projects', ['proj_id'], ['proj_id'])
    op.drop_constraint(None, 'displays', schema='public', type_='foreignkey')
    op.create_foreign_key('displays_proj_id_fkey', 'displays', 'projects', ['proj_id'], ['proj_id'])
    op.drop_constraint(None, 'conditions', schema='public', type_='foreignkey')
    op.create_foreign_key('conditions_proj_id_fkey', 'conditions', 'projects', ['proj_id'], ['proj_id'])
    op.drop_constraint(None, 'chapter8', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter8', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter8', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter8', schema='public', type_='foreignkey')
    op.create_foreign_key('chapter8_trig_action_fkey', 'chapter8', 'displays', ['trig_action'], ['display_id'])
    op.create_foreign_key('chapter8_trig_trig_fkey', 'chapter8', 'events', ['trig_trig'], ['event_id'])
    op.create_foreign_key('chapter8_trig_condition_fkey', 'chapter8', 'conditions', ['trig_condition'], ['condition_id'])
    op.create_foreign_key('chapter8_screen_gid_fkey', 'chapter8', 'screen', ['screen_gid'], ['screen_gid'])
    op.drop_constraint(None, 'chapter7', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter7', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter7', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter7', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter7', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter7', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter7', schema='public', type_='foreignkey')
    op.create_foreign_key('chapter7_screen_gid_fkey', 'chapter7', 'screen', ['screen_gid'], ['screen_gid'])
    op.create_foreign_key('chapter7_transition_f_action_fkey', 'chapter7', 'displays', ['transition_f_action'], ['display_id'])
    op.create_foreign_key('chapter7_transition_b_action_fkey', 'chapter7', 'displays', ['transition_b_action'], ['display_id'])
    op.create_foreign_key('chapter7_transition_i_action_fkey', 'chapter7', 'displays', ['transition_i_action'], ['display_id'])
    op.create_foreign_key('chapter7_transition_f_condition_fkey', 'chapter7', 'conditions', ['transition_f_condition'], ['condition_id'])
    op.create_foreign_key('chapter7_transition_i_condition_fkey', 'chapter7', 'conditions', ['transition_i_condition'], ['condition_id'])
    op.create_foreign_key('chapter7_transition_b_condition_fkey', 'chapter7', 'conditions', ['transition_b_condition'], ['condition_id'])
    op.drop_constraint(None, 'chapter6', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter6', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter6', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter6', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter6', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter6', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter6', schema='public', type_='foreignkey')
    op.create_foreign_key('chapter6_status_change_b_condition_fkey', 'chapter6', 'conditions', ['status_change_b_condition'], ['condition_id'])
    op.create_foreign_key('chapter6_status_change_i_condition_fkey', 'chapter6', 'conditions', ['status_change_i_condition'], ['condition_id'])
    op.create_foreign_key('chapter6_status_change_f_condition_fkey', 'chapter6', 'conditions', ['status_change_f_condition'], ['condition_id'])
    op.create_foreign_key('chapter6_status_change_b_action_fkey', 'chapter6', 'displays', ['status_change_b_action'], ['display_id'])
    op.create_foreign_key('chapter6_status_change_i_action_fkey', 'chapter6', 'displays', ['status_change_i_action'], ['display_id'])
    op.create_foreign_key('chapter6_screen_gid_fkey', 'chapter6', 'screen', ['screen_gid'], ['screen_gid'])
    op.create_foreign_key('chapter6_status_change_f_action_fkey', 'chapter6', 'displays', ['status_change_f_action'], ['display_id'])
    op.drop_constraint(None, 'chapter5', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter5', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter5', schema='public', type_='foreignkey')
    op.create_foreign_key('chapter5_init_condition_fkey', 'chapter5', 'conditions', ['init_condition'], ['condition_id'])
    op.create_foreign_key('chapter5_screen_gid_fkey', 'chapter5', 'screen', ['screen_gid'], ['screen_gid'])
    op.create_foreign_key('chapter5_init_action_fkey', 'chapter5', 'displays', ['init_action'], ['display_id'])
    op.drop_constraint(None, 'chapter4', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter4', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter4', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter4', schema='public', type_='foreignkey')
    op.create_foreign_key('chapter4_hk_ope_fkey', 'chapter4', 'ope_types', ['hk_ope'], ['ope_id'])
    op.create_foreign_key('chapter4_hk_condition_fkey', 'chapter4', 'conditions', ['hk_condition'], ['condition_id'])
    op.create_foreign_key('chapter4_hk_action_fkey', 'chapter4', 'displays', ['hk_action'], ['display_id'])
    op.create_foreign_key('chapter4_screen_gid_fkey', 'chapter4', 'screen', ['screen_gid'], ['screen_gid'])
    op.drop_constraint(None, 'chapter3', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter3', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter3', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter3', schema='public', type_='foreignkey')
    op.create_foreign_key('chapter3_action_condition_fkey', 'chapter3', 'conditions', ['action_condition'], ['condition_id'])
    op.create_foreign_key('chapter3_action_action_fkey', 'chapter3', 'displays', ['action_action'], ['display_id'])
    op.create_foreign_key('chapter3_screen_gid_fkey', 'chapter3', 'screen', ['screen_gid'], ['screen_gid'])
    op.create_foreign_key('chapter3_action_ope_fkey', 'chapter3', 'ope_types', ['action_ope'], ['ope_id'])
    op.drop_constraint(None, 'chapter2', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter2', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter2', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter2', schema='public', type_='foreignkey')
    op.create_foreign_key('chapter2_active_action_fkey', 'chapter2', 'displays', ['active_action'], ['display_id'])
    op.create_foreign_key('chapter2_active_property_fkey', 'chapter2', 'properties', ['active_property'], ['property_id'])
    op.create_foreign_key('chapter2_screen_gid_fkey', 'chapter2', 'screen', ['screen_gid'], ['screen_gid'])
    op.create_foreign_key('chapter2_active_condition_fkey', 'chapter2', 'conditions', ['active_condition'], ['condition_id'])
    op.drop_constraint(None, 'chapter1', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter1', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter1', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'chapter1', schema='public', type_='foreignkey')
    op.create_foreign_key('chapter1_display_condition_fkey', 'chapter1', 'conditions', ['display_condition'], ['condition_id'])
    op.create_foreign_key('chapter1_display_action_fkey', 'chapter1', 'displays', ['display_action'], ['display_id'])
    op.create_foreign_key('chapter1_screen_gid_fkey', 'chapter1', 'screen', ['screen_gid'], ['screen_gid'])
    op.create_foreign_key('chapter1_display_property_fkey', 'chapter1', 'properties', ['display_property'], ['property_id'])
    op.drop_constraint(None, 'available_model', schema='public', type_='foreignkey')
    op.create_foreign_key('available_model_screen_id_fkey', 'available_model', 'screen', ['screen_id'], ['screen_gid'])
    # ### end Alembic commands ###
