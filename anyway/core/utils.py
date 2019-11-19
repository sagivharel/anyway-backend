import six

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
