# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import module2 as m2
# import data_description_package_sa-0.1 as ddp

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌃F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = m2.load_csv_pandas('Australia Weather Data/Weather Test Data.csv')
    m2.display_pandas_head(df)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
