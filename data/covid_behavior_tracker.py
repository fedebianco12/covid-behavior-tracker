import datetime
import time
import pandas as pd
import numpy as np

COUNTRY_DATA = { 'australia' : 'australia.csv','brazil' : 'brazil.csv',
                'canada' : 'canada.csv', 'china' : 'china.csv',
                'france' : 'france.csv', 'germany' : 'germany.csv',
                'india' : 'india.csv', 'italy' : 'italy.csv', 'japan' : 'japan.csv',
                'saudi arabia' : 'saudi-arabia.csv', 'singapore' : 'singapore.csv',
                'south korea' : 'south-korea.csv', 'spain' : 'spain.csv',
                'sweden' : 'sweden.csv', 'uk' : 'united-kingdom.csv',
                'united kingdom' : 'united-kingdom.csv',
                'mexico': 'mexico.csv',
                'united states' : 'united-states.csv',
                'usa': 'united-states.csv' }

def get_filters():
    """
    Asks user to specify a country to analyze.

    Returns:
        (str) country - name of the country to analyze
    """
    print('Hello! Explore some country data.')
    # get user input for country
    while True:
        countries = ( 'australia' 'brazil', 'canada', 'china','france', 'germany',
                    'india', 'italy', 'japan', 'saudi arabia', 'singapore',
                    'south korea', 'spain','sweden', 'uk', 'united kingdom',
                    'mexico','united states','usa' )
        country =  input("Select country: ")
        if country.lower() not in countries:
            print("Try again. Please write the country name (Canada, Mexico, USA)")
        else:
            print("Thank you. You selected {}.".format(country.title()))
            break

    print('-'*40)
    return country

def load_data(country):
    """
    Loads data for the specified country.

    Args:
        (str) country - name of the country to analyze
    Returns:
        df - Pandas DataFrame containing country data
    """

    # load data file into a dataframe
    df = pd.read_csv(COUNTRY_DATA[country])

    return df

def avoid_shops(df):
    """Displays statistics on how many people avoided shops:
    Options: Always, frequently, not at all, rarely, sometimes."""

    print('\nCalculating shop avoidance behavior...\n  Have you avoided going to shops in the past 7 days?\n')

    avoid_counts = df['i12_health_16'].value_counts()
    print("Value counts:\n{}\n.".format(avoid_counts))

    avoid_describe = df['i12_health_16'].describe()
    print(avoid_describe)

    return avoid_counts

    print('-'*40)

def excel_write(avoid_counts):
    """Writes python script output to XLSX file \'output\' in directory"""

    writer = pd.ExcelWriter('output.xlsx', engine = 'xlsxwriter')
    avoid_counts.to_excel(writer, sheet_name='Sheet1')
    writer.save()

def main():
    while True:
        country = get_filters()
        df = load_data(country)

        avoid_shops(df)
        excel_write(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
