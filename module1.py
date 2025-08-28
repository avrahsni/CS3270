import csv
import pandas as pd

data = []
def load_csv(file_name):
    with open(file_name, mode = 'r') as file:
        content = csv.reader(file)
        add_to_weather_data(content)


def load_csv_pandas(file_name):
    df = pd.read_csv(file_name)
    return df
    #add_to_weather_data(content)

def add_to_weather_data(content):
    for lines in content:
        data.append(lines)



if __name__ == '__main__':
    file_name = "Australia Weather Data/Weather Training Data.csv"
    # load_csv(file_name)
    # print("CSV Method: ", len(data))
    data.clear()
    df = load_csv_pandas(file_name)
    print("Pandas Method: ", len(df))
    print(df.describe())
