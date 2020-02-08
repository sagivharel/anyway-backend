from anyway import db
from flask_sqlalchemy import SQLAlchemy
from anyway.apis.common.models import WazeAlert, WazeTrafficJams

def insert_waze_alerts(waze_alerts_df):
    """
    insert new waze alerts to db
    :param waze_alerts_df: DataFrame contains waze alerts
    """
    waze_alerts = [
        {
            'city': alert['city'],
            'confidence': alert['confidence'],
            'created_at': alert['created_at'],
            'lontitude': alert['lontitude'],
            'latitude': alert['latitude'],
            'magvar': alert['magvar'],
            'type': alert['nThumbsUp'],
            'report_rating': alert['reportRating'],
            'reliability': alert['reliability'],
            'alert_type': alert['type'],
            'alert_subtype': alert['subtype'],
            'uuid': alert['uuid'],
            'street': alert['street'],
            'road_type': alert['roadType'],
            'geom': alert['geometry']
        } for i, alert in waze_alerts_df.iterrows()]

    db.session.bulk_insert_mappings(WazeAlert, waze_alerts)
    db.session.commit()


def insert_waze_traffic_jams(waze_traffic_jams_df):
    """
    insert new waze traffic jams to db
    :param waze_traffic_jams_df: DataFrame contains waze traffic jams
    """
    waze_traffic_jams = [
        {
            'level': jam['level'],
            'line': jam['line'],
            'speed_kmh': jam['speedKMH'],
            'turn_type': jam['turnType'],
            'length': jam['length'],
            'type': jam['type'],
            'uuid': jam['uuid'],
            'speed': jam['speed'],
            'segments': jam['segments'],
            'road_type': jam['roadType'],
            'delay': jam['delay'],
            'street': jam['street'],
            'city': jam['city'],
            'end_node': jam['endNode'],
            'blocking_alert_uuid': jam['blockingAlertUuid'],
            'start_node': jam['startNode'],
            'created_at': jam['created_at'],
            'geom': jam['geometry']
        } for i, jam in waze_traffic_jams_df.iterrows()]

    db.session.bulk_insert_mappings(WazeTrafficJams, waze_traffic_jams)
    db.session.commit()