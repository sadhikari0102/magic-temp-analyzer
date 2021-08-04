class DataPoint:
    def __init__(self, data_row):
        self._station_id = int(data_row["station_id"])
        self._date = float(data_row["date"])
        self._temp = float(data_row["temperature_c"])

    @property
    def station_id(self):
        return self._station_id

    @property
    def date(self):
        return self._date

    @property
    def temp(self):
        return self._temp
