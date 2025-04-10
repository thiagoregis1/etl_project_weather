from datetime import datetime

class Utils:
    @staticmethod
    def unix_to_datetime(timestamp):
        if timestamp:
            return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return None

    @staticmethod
    def filter_columns(data, columns_selected):
        return {key: str(data[key]) for key in columns_selected if key in data and data[key] is not None}

    @staticmethod
    def rename_columns(data, rename_map):
        return {rename_map.get(key, key): value for key, value in data.items()}