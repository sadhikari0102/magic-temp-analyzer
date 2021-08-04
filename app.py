from csv import DictReader
from temp_log_processor import TempLogProcessor


def start():
    filepath = input("Enter File path for data set:")
    temp_log_processor = TempLogProcessor()
    with open(filepath, 'r') as csvfile:
        filereader = DictReader(csvfile)
        print("Processing Data...")
        for row in filereader:
            # print(row)
            temp_log_processor.process_datapoint(row)
    print('Data Processed Successfully.')
    take_input = True
    while take_input:
        option = input("Choose a query type: \n 1. Get Minimum Temp \n 2. Get Maximum Fluctuation \n 3. Get Maximum Fluctuation for Date range \n")
        if option == '1':
            (station_id, date, temp) = temp_log_processor.get_lowest_temp()
            print(f'Minimum Temp of {temp} celcius was from station {station_id} on {date}')
        elif option == '2':
            station_id = temp_log_processor.get_maximum_fluctuation()
            print(f'Maximum fluctutaion was at station {station_id}')
        elif option == '3':
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")
            station_id = temp_log_processor.get_maximum_fluctuation_for_date_range(float(start_date), float(end_date))
            print(f'Maximum fluctutaion for given date range was at station {station_id}')
        else:
            print('Chosen option unavailable!')
        retry = input("Enter 'Y' to continue, anything else to exit")
        take_input = (retry == 'Y')


if __name__ == "__main__":
    start()
