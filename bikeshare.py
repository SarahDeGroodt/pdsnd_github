import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # create list for each filter
    cities = ['chicago', 'new york', 'washington']
    data_filters = ['month', 'day', 'both', 'none']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    print('\nHello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). Use a while loop to handle invalid inputs.
    while True:
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n> ').strip().lower()
        if city in cities:
            break
        else:
            print('\nInvalid input!\nPlease type "chicago" or "new york" or "washington".')

    # get user input for filtering the data by month, day or no filtering at all. Use a while loop to handle invalid inputs.
    while True:
        data_filter = input('\nWould you like to filter the data by month, day, both, or not at all?\nPlease type "month" to filter by month, "day" to filter by day, "both" to filter by month and day, or "none" for no time filter.\n> ').strip().lower()
        if data_filter in data_filters:
            break
        else:
            print('\nInvalid input!\nPlease type "month" or "day" or "both" or "none".')

    # in case the user choses to filter on month: get user input for month (all, january, february, ... , june). Use a while loop to handle invalid inputs.
    if data_filter == 'month' or data_filter == 'both':
        while True:
            month = input('\nWhich month? All months, January, February, March, April, May or June?\nPlease type "all" to include all months, "january" to filter on data for January only etc.\n> ').strip().lower()
            if month in months:
                break
            else:
                print('\nInvalid input!\nPlease type "all" or "january" or "february" or "march" or "april" or "may" or "june".')
    else:
        month = 'all'

    # in case the user choses to filter on day: get user input for day of week (all, monday, tuesday, ... sunday). Use a while loop to handle invalid inputs.
    if data_filter == 'day' or data_filter == 'both':
        while True:
            day = input('\nWhich day? All days, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\nPlease type "all" to include all days, "monday" to filter on data for Mondays only etc.\n> ').strip().lower()
            if day in days:
                break
            else:
                print('\nInvalid input!\nPlease type "all" or "monday" or "tuesday" or "wednesday" or "thursday" or "friday" or "saturday" or "sunday".')
    else:
        day = 'all'

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating the first statistic...\nThe most frequent times of travel:\n')
    start_time = time.time()

    # display the most common month
    most_month = df['month'].mode()[0]
    print('The most common month is: ', most_month)

    # display the most common day of week
    most_day = df['day_of_week'].mode()[0]
    print('\nThe most common day of week is: ', most_day)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    # display the most common start hour
    print('\nThe most popular start hour is: ', popular_hour)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the second statistic...\nThe most popular stations and trip:\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is: ', end_station)

    # display most frequent combination of start station and end station trip
    popular_trip = 'from "' + df['Start Station'] + '" to "' + df['End Station'] + '"'
    print('\nThe most popular trip is', popular_trip.mode()[0])


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating the third statistic...\nThe trip duration:\n')
    start_time = time.time()

    # calculate total travel time in seconds
    total_time = df['Trip Duration'].sum()
    print('Total travel time is: ', total_time, ' seconds')

    # calculate mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\nMean travel time is:', mean_time, ' seconds')

    ##print('\nTotal Duration:', ' , Count:', ' , Avg Duration:', ' ,Filter:'\n')
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating the fourth and final statistic...\nUser stats:\n')
    start_time = time.time()

    # display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('\nNo gender data available.')

    # display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        min_birthyear = df['Birth Year'].min()
        max_birthyear = df['Birth Year'].max()
        most_common_birthyear = df['Birth Year'].mode()[0]
        print('\nThe earliest birth year is: ', int(min_birthyear))
        print('\nThe most recent birth year is: ', int(max_birthyear))
        print('\nThe most common birth year is: ', int(most_common_birthyear))
    else:
        print('\nNo birth year data available.')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def row_details(df):
    """Prompts user if he/she wants to see 5 rows of raw data."""

    raw_data = input('\nDo you want to see the first 5 rows of raw data?\nPlease type "yes" or "no".\n> ').strip().lower()
    if raw_data == 'yes':
        # display 5 rows of raw data + repeat until users says "no"
        for i, (_, row) in enumerate(df.iterrows()):
            print('\nRow', i)
            print(row)
            print()

            if i % 5 == 4:
                yes_no = input('\nDo you want to see the next 5 rows of raw data?\nPlease type "yes" or "no".\n> ').strip().lower()
                if yes_no == 'no':
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_details(df)

        restart = input('\nWould you like to restart?\nPlease type "yes" or "no".\n> ').strip().lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
