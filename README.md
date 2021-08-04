# MAGIC Temperature Analyzer

This tool is a command line data processing script that takes a csv dataset file containing temperature data in form of (station_id,date,temperature_c) and processes it to perform desired calculations.

### Functions
1. Get minimum temperature, date recorded and the station that recorded it
2. Get station that experienced maximum cumulative fluctuation among all stations
3. Get station that experienced maximum cumulative fluctuation among all stations for a given date range

### Execution
- Start with cloning the repo and entering the root directory.
- Start the script using `python3 app.py`
- Follow the prompts and enter responses to receive desired output. First one asks for a filepath to the dataset and takes a while (~10s) to process the data

### Assumptions
#### Following assumptions are made to avoid extensive data validation to save time. Additional time can be spent to put more validations and error handling around bas data to ignore rows, or terminate processing as desired.
- Dataset is already sorted by station_id and date
- 'station_id' is expected to be an integer, 'date' a floating point number and 'temperature_c' a floating point number as well
