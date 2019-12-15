"""create initial schema

Revision ID: f67d98a989e7
Revises: 
Create Date: 2019-12-15 04:41:28.145666

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f67d98a989e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'markers',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('provider_and_id', sa.BigInteger(), nullable=True),
        sa.Column('provider_code', sa.Integer(), nullable=False),
        sa.Column('provider_code_hebrew', sa.Text(), nullable=True),
        sa.Column('file_type_police', sa.Integer(), nullable=True),
        sa.Column('accident_type', sa.Integer(), nullable=True),
        sa.Column('accident_type_hebrew', sa.Text(), nullable=True),
        sa.Column('accident_severity', sa.Integer(), nullable=True),
        sa.Column('accident_severity_hebrew', sa.Text(), nullable=True),
        sa.Column('accident_timestamp', sa.Text(), nullable=True),
        sa.Column('location_accuracy', sa.Text(), nullable=True),
        sa.Column('location_accuracy_hebrew', sa.Text(), nullable=True),
        sa.Column('road_type', sa.Integer(), nullable=True),
        sa.Column('road_type_hebrew', sa.Text(), nullable=True),
        sa.Column('road_shape', sa.Integer(), nullable=True),
        sa.Column('road_shape_hebrew', sa.Text(), nullable=True),
        sa.Column('day_type', sa.Integer(), nullable=True),
        sa.Column('day_type_hebrew', sa.Text(), nullable=True),
        sa.Column('police_unit', sa.Integer(), nullable=True),
        sa.Column('police_unit_hebrew', sa.Text(), nullable=True),
        sa.Column('one_lane', sa.Integer(), nullable=True),
        sa.Column('one_lane_hebrew', sa.Text(), nullable=True),
        sa.Column('multi_lane', sa.Integer(), nullable=True),
        sa.Column('multi_lane_hebrew', sa.Text(), nullable=True),
        sa.Column('speed_limit', sa.Integer(), nullable=True),
        sa.Column('speed_limit_hebrew', sa.Text(), nullable=True),
        sa.Column('road_intactness', sa.Integer(), nullable=True),
        sa.Column('road_intactness_hebrew', sa.Text(), nullable=True),
        sa.Column('road_width', sa.Integer(), nullable=True),
        sa.Column('road_width_hebrew', sa.Text(), nullable=True),
        sa.Column('road_sign', sa.Integer(), nullable=True),
        sa.Column('road_sign_hebrew', sa.Text(), nullable=True),
        sa.Column('road_light', sa.Integer(), nullable=True),
        sa.Column('road_light_hebrew', sa.Text(), nullable=True),
        sa.Column('road_control', sa.Integer(), nullable=True),
        sa.Column('road_control_hebrew', sa.Text(), nullable=True),
        sa.Column('weather', sa.Integer(), nullable=True),
        sa.Column('weather_hebrew', sa.Text(), nullable=True),
        sa.Column('road_surface', sa.Integer(), nullable=True),
        sa.Column('road_surface_hebrew', sa.Text(), nullable=True),
        sa.Column('road_object', sa.Integer(), nullable=True),
        sa.Column('road_object_hebrew', sa.Text(), nullable=True),
        sa.Column('object_distance', sa.Integer(), nullable=True),
        sa.Column('object_distance_hebrew', sa.Text(), nullable=True),
        sa.Column('didnt_cross', sa.Integer(), nullable=True),
        sa.Column('didnt_cross_hebrew', sa.Text(), nullable=True),
        sa.Column('cross_mode', sa.Integer(), nullable=True),
        sa.Column('cross_mode_hebrew', sa.Text(), nullable=True),
        sa.Column('cross_location', sa.Integer(), nullable=True),
        sa.Column('cross_location_hebrew', sa.Text(), nullable=True),
        sa.Column('cross_direction', sa.Integer(), nullable=True),
        sa.Column('cross_direction_hebrew', sa.Text(), nullable=True),
        sa.Column('road1', sa.Integer(), nullable=True),
        sa.Column('road2', sa.Integer(), nullable=True),
        sa.Column('km', sa.Float(), nullable=True),
        sa.Column('km_raw', sa.Float(), nullable=True),
        sa.Column('km_accurate', sa.Text(), nullable=True),
        sa.Column('yishuv_symbol', sa.Integer(), nullable=True),
        sa.Column('yishuv_name', sa.Text(), nullable=True),
        sa.Column('geo_area', sa.Integer(), nullable=True),
        sa.Column('geo_area_hebrew', sa.Text(), nullable=True),
        sa.Column('day_night', sa.Integer(), nullable=True),
        sa.Column('day_night_hebrew', sa.Text(), nullable=True),
        sa.Column('day_in_week', sa.Integer(), nullable=True),
        sa.Column('day_in_week_hebrew', sa.Text(), nullable=True),
        sa.Column('traffic_light', sa.Integer(), nullable=True),
        sa.Column('traffic_light_hebrew', sa.Text(), nullable=True),
        sa.Column('region', sa.Integer(), nullable=True),
        sa.Column('region_hebrew', sa.Text(), nullable=True),
        sa.Column('district', sa.Integer(), nullable=True),
        sa.Column('district_hebrew', sa.Text(), nullable=True),
        sa.Column('natural_area', sa.Integer(), nullable=True),
        sa.Column('natural_area_hebrew', sa.Text(), nullable=True),
        sa.Column('municipal_status', sa.Integer(), nullable=True),
        sa.Column('municipal_status_hebrew', sa.Text(), nullable=True),
        sa.Column('yishuv_shape', sa.Integer(), nullable=True),
        sa.Column('yishuv_shape_hebrew', sa.Text(), nullable=True),
        sa.Column('street1', sa.Integer(), nullable=True),
        sa.Column('street1_hebrew', sa.Text(), nullable=True),
        sa.Column('street2', sa.Integer(), nullable=True),
        sa.Column('street2_hebrew', sa.Text(), nullable=True),
        sa.Column('house_number', sa.Integer(), nullable=True),
        sa.Column('non_urban_intersection', sa.Integer(), nullable=True),
        sa.Column('non_urban_intersection_hebrew', sa.Text(), nullable=True),
        sa.Column('non_urban_intersection_by_junction_number', sa.Text(), nullable=True),
        sa.Column('urban_intersection', sa.Integer(), nullable=True),
        sa.Column('accident_year', sa.Integer(), nullable=True),
        sa.Column('accident_month', sa.Integer(), nullable=True),
        sa.Column('accident_day', sa.Integer(), nullable=True),
        sa.Column('accident_hour_raw', sa.Integer(), nullable=True),
        sa.Column('accident_hour_raw_hebrew', sa.Text(), nullable=True),
        sa.Column('accident_hour', sa.Integer(), nullable=True),
        sa.Column('accident_minute', sa.Integer(), nullable=True),
        sa.Column('geom', sa.Text(), nullable=True),
        sa.Column('longitude', postgresql.DOUBLE_PRECISION(precision=53), nullable=True),
        sa.Column('latitude', postgresql.DOUBLE_PRECISION(precision=53), nullable=True),
        sa.Column('x', sa.Float(), nullable=True),
        sa.Column('y', sa.Float(), nullable=True),
    )

def downgrade():
    op.drop_table('markers')
