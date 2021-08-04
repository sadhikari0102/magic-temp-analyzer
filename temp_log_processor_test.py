from temp_log_processor import TempLogProcessor


INPUT = [
    [100,2001.1,100],
    [100,2001.2,50],
    [100,2001.3,0],
    [100,2001.4,250],
    [101,2001.1,0],
    [101,2001.2,100],
    [101,2001.4,150],
    [102,2001.1,-150],
    [102,2001.3,50],
    [102,2001.5,60],
    [102,2001.7,65],
    [102,2001.8,77],
    [103,2001.1,100],
    [103,2001.2,0],
    [103,2002.3,200],
    [103,2002.4,0],
    [103,2002.5,-10],
    [103,2002.6,250],
    [103,2002.10,10]
]
temp_processor = None

def _initialize_processor():
    global temp_processor
    temp_processor = TempLogProcessor()
    for row in INPUT:
        temp_processor.process_datapoint({"station_id": row[0], "date": row[1], "temperature_c": row[2]})


def start_tests():
    _initialize_processor()
    assert(temp_processor.get_lowest_temp() == (102, 2001.1, -150))
    assert(temp_processor.get_lowest_temp() == (102, 2001.1, -150))
    assert(temp_processor.get_maximum_fluctuation() == 103)
    assert(temp_processor.get_maximum_fluctuation_for_date_range(2000, 2001) is None)
    assert(temp_processor.get_maximum_fluctuation_for_date_range(2000, 2002) == 100)
    assert(temp_processor.get_maximum_fluctuation_for_date_range(2001, 2002) == 100)
    assert(temp_processor.get_maximum_fluctuation_for_date_range(2001, 2003) == 103)

if __name__ == "__main__":
    start_tests()
