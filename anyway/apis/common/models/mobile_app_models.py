from anyway.core.database  import MobileAppBase
from sqlalchemy import Column, BigInteger, Integer, String, Boolean, Float, ForeignKey, DateTime, Text, Index, desc, \
    sql, Table, \
    ForeignKeyConstraint, func, and_, TIMESTAMP

class ReportProblem(MobileAppBase):
    __tablename__ = "report_problem"
    id = Column(BigInteger(), autoincrement=True, primary_key=True, index=True)
    latitude = Column(Float())
    longitude = Column(Float())
    problem_description = Column(Text())
    signs_on_the_road_not_clear = Column(Boolean())
    signs_problem = Column(Boolean())
    pothole = Column(Boolean())
    no_light = Column(Boolean())
    no_sign = Column(Boolean())
    crossing_missing = Column(Boolean())
    sidewalk_is_blocked = Column(Boolean())
    street_light_issue = Column(Boolean())
    road_hazard = Column(Boolean())
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone_number = Column(String(50))
    email = Column(String(100))
    send_to_municipality = Column(Boolean())
    image_data = Column(String())
    personal_id = Column(String(20))
