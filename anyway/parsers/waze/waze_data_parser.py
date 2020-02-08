from google.cloud import storage
import pandas as pd
from pandas.io.json import json_normalize
import json
from waze.waze_db_functions import insert_waze_alerts, insert_waze_traffic_jams

def list_blobs(bucket_name):
    """
    Lists all the blobs in the bucket.
    """
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    return blobs


def parse_waze_alerts_data(waze_alerts):
    """
    parse waze alert json into a Dataframe.
    param waze_alerts: waze raw alert json data
    return: parsed Dataframe
    """

    waze_df = json_normalize(waze_alerts)
    waze_df['created_at'] = pd.to_datetime(waze_df['pubMillis'], unit='ms')
    waze_df.rename({'location.x': 'latitude', 'location.y': 'lonitude'}, axis=1, inplace=True)
    waze_df['geometry'] = waze_df.apply(lambda row: 'POINT({} {})'.format(row['lonitude'], row['latitude']), axis=1)
    waze_df.drop(['country', 'pubMillis', 'reportDescription'], axis=1, inplace=True)

    return waze_df


def parse_waze_traffic_jams_data(waze_jams):
    """
    parse waze traffic jams json into a Dataframe.
    param waze_jams: waze raw traffic jams json data
    return: parsed Dataframe
    """

    waze_df = json_normalize(waze_jams)
    waze_df['created_at'] = pd.to_datetime(waze_df['pubMillis'], unit='ms')
    waze_df['geometry'] = waze_df['line'].apply(lambda l: 'LINESTRING({})'.format(','.join(['{} {}'.format(nz['x'], nz['y']) for nz in l])))
    waze_df.drop(['country', 'pubMillis'], axis=1, inplace=True)

    return waze_df


def waze_parser(bucket_name):
    waze_alerts = []
    waze_traffic_jams = []
    for waze_file in list_blobs(bucket_name):
        waze_data = waze_file.download_as_string()
        waze_json = json.loads(waze_data)
        waze_alerts.append(parse_waze_alerts_data(waze_json['alerts']))
        waze_traffic_jams.append(parse_waze_traffic_jams_data(waze_json['jams']))

    waze_alerts_df = pd.concat(waze_alerts, ignore_index=True, sort=False)
    waze_traffic_jams_df = pd.concat(waze_traffic_jams, ignore_index=True, sort=False)
    insert_waze_alerts(waze_alerts_df)
    insert_waze_traffic_jams(waze_traffic_jams_df)


BUCKET_NAME = 'anyway-hasadna.appspot.com'
waze_parser(BUCKET_NAME)
