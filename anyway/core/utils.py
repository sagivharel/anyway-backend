from pyproj import Transformer
import logging
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Utils():

    @staticmethod
    def batch_iterator(iterable, batch_size):
        iterator = iter(iterable)
        iteration_stopped = False

        while True:
            batch = []
            for _ in range(batch_size):
                try:
                    batch.append(next(iterator))
                except StopIteration:
                    iteration_stopped = True
                    break

            yield batch
            if iteration_stopped:
                break

    @staticmethod
    def decode_hebrew(s, encoding="cp1255"):
        if six.PY3:
            return s
        else:
            return s.decode(encoding)

    @staticmethod
    def time_delta(since):
        delta = relativedelta(datetime.now(), since)
        attrs = ['years', 'months', 'days', 'hours', 'minutes', 'seconds']
        return " ".join('%d %s' % (getattr(delta, attr),
                                   getattr(delta, attr) > 1 and attr or attr[:-1])
                        for attr in attrs if getattr(delta, attr))

    @staticmethod
    def truncate_tables(db, tables):
        logging.info("Deleting tables: " + ", ".join('.'.join([table.metadata.schema,table.__name__]) for table in tables))
        for table in tables:
            db.session.query(table).delete()
            db.session.commit()

    @staticmethod
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        try:
            xrange
        except NameError:
            xrange = range
        for i in xrange(0, len(l), n):
            yield l[i:i + n]

    class ItmToWGS84(object):
        def __init__(self):
            # initializing WGS84 (epsg: 4326) and Israeli TM Grid (epsg: 2039) projections.
            # for more info: https://epsg.io/<epsg_num>/
            self.transformer = Transformer.from_proj(2039, 4326, always_xy=True)

        def convert(self, x, y):
            """
            converts ITM to WGS84 coordinates
            :type x: float
            :type y: float
            :rtype: tuple
            :return: (longitude,latitude)
            """
            longitude, latitude = self.transformer.transform(x, y)
            return longitude, latitude

