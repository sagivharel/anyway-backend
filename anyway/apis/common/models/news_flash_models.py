from anyway.core.database import NewsFlashBase
from sqlalchemy import Column, BigInteger, Integer, String, Boolean, Float, ForeignKey, DateTime, Text, Index, desc, \
    sql, Table, \
    ForeignKeyConstraint, func, and_, TIMESTAMP


class NewsFlash(NewsFlashBase):
    __tablename__ = "news_flash"
    id = Column(BigInteger(), primary_key=True)
    accident = Column(Boolean(), nullable=True)
    author = Column(Text(), nullable=True)
    date = Column(TIMESTAMP(), nullable=True)
    description = Column(Text(), nullable=True)
    lat = Column(Float(), nullable=True)
    link = Column(Text(), nullable=True)
    lon = Column(Float(), nullable=True)
    road1 = Column(Float(), nullable=True)
    road2 = Column(Float(), nullable=True)
    resolution = Column(Text(), nullable=True)
    title = Column(Text(), nullable=True)
    source = Column(Text(), nullable=True)
    location = Column(Text(), nullable=True)
    tweet_id = Column(BigInteger(), nullable=True)
    region_hebrew = Column(Text(), nullable=True)
    district_hebrew = Column(Text(), nullable=True)
    yishuv_name = Column(Text(), nullable=True)
    street1_hebrew = Column(Text(), nullable=True)
    street2_hebrew  = Column(Text(), nullable=True)
    non_urban_intersection_hebrew = Column(Text(), nullable=True)
    road_segment_name = Column(Text(), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "accident": self.accident,
            "author": self.author,
            "date": self.date,
            "description": self.description,
            "lat": self.lat,
            "link": self.link,
            "lon": self.lon,
            "road1": self.road1,
            "road2": self.road2,
            "resolution": self.resolution,
            "title": self.title,
            "source": self.source,
            "location": self.location,
            "tweet_id": self.tweet_id,
            "region_hebrew": self.region_hebrew,
            "district_hebrew": self.district_hebrew,
            "yishuv_name": self.yishuv_name,
            "street1_hebrew": self.street1_hebrew,
            "street2_hebrew": self.street2_hebrew,
            "non_urban_intersection_hebrew": self.non_urban_intersection_hebrew,
            "road_segment_name": self.road_segment_name,
        }

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
