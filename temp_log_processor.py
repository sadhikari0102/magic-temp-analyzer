from data_point import DataPoint
from typing import List, Tuple, Dict
from bisect import bisect_left


class FluctuationPoint:
    def __init__(self, fluctuation, last_temp):
        self._fluctuation = fluctuation
        self._last_temp = last_temp

    @property
    def fluctuation(self):
        return self._fluctuation

    @fluctuation.setter
    def fluctuation(self, value):
        self._fluctuation = value

    @property
    def last_temp(self):
        return self._last_temp

    @last_temp.setter
    def last_temp(self, value):
        self._last_temp = value


class TempLogProcessor:

    def __init__(self):
        self._dataset: List[DataPoint] = []
        self._min_temp = float('inf')
        self._min_temp_station_date = None
        self._last_station_temp: Dict[str, FluctuationPoint] = dict()
        self._max_fluctuation = float('-inf')
        self._max_fluctuation_station = None
        self._date_indexes = None

    def process_datapoint(self, datarow):
        data_point = DataPoint(datarow)
        # calculate minimum temp on the go as the points are processed
        if data_point.temp < self._min_temp:
            self._min_temp = data_point.temp
            self._min_temp_station_date = (data_point.station_id, data_point.date, data_point.temp)
        # calculate maximum cumulative fluctuation among stations on the go
        if data_point.station_id in self._last_station_temp:
            last_fluctuation_point = self._last_station_temp[data_point.station_id]
            last_fluctuation_point.fluctuation += abs(last_fluctuation_point.last_temp - data_point.temp)
            last_fluctuation_point.last_temp = data_point.temp
            if last_fluctuation_point.fluctuation > self._max_fluctuation:
                self._max_fluctuation = last_fluctuation_point.fluctuation
                self._max_fluctuation_station = data_point.station_id
        else:
            self._last_station_temp[data_point.station_id] = FluctuationPoint(0, data_point.temp)
        # save points for future calculations
        self._dataset.append(data_point)

    def get_lowest_temp(self) -> Tuple[int, float, float]:
        return self._min_temp_station_date

    def get_maximum_fluctuation(self) -> int:
        return self._max_fluctuation_station

    def get_maximum_fluctuation_for_date_range(self, start_date: float, end_date: float):
        if self._date_indexes is None:
            # sort dataset by date anmd save the date indexes for faster lookups for subsequent queries
            self._dataset.sort(key=lambda point: point.date)
            self._date_indexes = [point.date for point in self._dataset]
        # find earliest index greater than or equal to start date using binary search
        current_index = bisect_left(self._date_indexes, start_date)
        print(f'start index {current_index}')
        local_last_temp: Dict[str, FluctuationPoint] = dict()
        max_fluct = float('-inf')
        max_fluct_station = None
        # start iterating from the current index till the date becomes out of search range
        while len(self._dataset) > current_index and self._dataset[current_index].date <= end_date:
            # calculate cumulative fluctuations for each station and maintain range maxima
            current_point = self._dataset[current_index]
            if current_point.station_id in local_last_temp:
                last_fluctuation_point = local_last_temp[current_point.station_id]
                last_fluctuation_point.fluctuation += abs(last_fluctuation_point.last_temp - current_point.temp)
                last_fluctuation_point.last_temp = current_point.temp
                if last_fluctuation_point.fluctuation > max_fluct:
                    max_fluct = last_fluctuation_point.fluctuation
                    max_fluct_station = current_point.station_id
            else:
                local_last_temp[current_point.station_id] = FluctuationPoint(0, current_point.temp)
            current_index += 1
        print(local_last_temp)
        return max_fluct_station
