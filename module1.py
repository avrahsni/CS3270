import csv
import pandas as pd

data = []
def load_csv(file_name):
    """
    Loads the csv data from the file and passes it to the function "add_to_weather_data()"
    :param file_name:
    :return:
    """
    with open(file_name, mode = 'r') as file:
        content = csv.reader(file)
        add_to_weather_data(content)


def load_csv_pandas(file_name):
    """
    Creates a pandas dataframe from the inputted csv file and returns it
    :param file_name:
    :return:
    """
    df = pd.read_csv(file_name)
    return df
    #add_to_weather_data(content)

def add_to_weather_data(content):
    """
    Adds each line of the input to the variable called "data"
    :param content:
    :return:
    """
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
