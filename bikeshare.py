import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    NEED TO REWORD THE WAY QUESTIONS ARE BEING ASKED
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input("Which city data do you want to explore? Choose Chicago, New York City or Washington. ").title()
        if city not in CITY_DATA:
            print("Invalid city. Please choose among Chicago, New York City and Washington. ")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)

    months=['January','February','March','April','May','June','All']
    while True:
        month = input("Type the month to filter data by. Choose between January and June. If you want all months, type all. ").title()
        if month not in months and month!= 'all':
            print("Invalid month. Try again. ")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    week_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
    while True:
        day = input("Type the day to filter data by. If you want all days of the week, type all. ").title()
        if day not in week_days:
            print("Invalid day. Try again. ")
            continue
        else:
            break
    
    
    print('-'*40, city, month, day)
    return city, month, day
    


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    ADD AN OPTION TO SEE 5 LINES AT A TIME    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.day_name

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']   
        month = months.index(month) +1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_name'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()
    print("Most common month is: ", most_common_month)
    

    # TO DO: display the most common day of week
    df['day']=df['Start Time'].dt.day
    most_common_day=df['day'].mode()
    print("Most common day is: ", most_common_day)


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_start=df['hour'].mode()
    print("Most common start time is: ", most_common_start)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
     """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()
    print("Most popular start station is ", popular_start_station)
    


    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()
    print("Most popular end station is ",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station'] + ' to ' + df['End Station']
    popular_combination=df['combination'].mode()
    print("Most popular start station - end station combination is ",popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    ADD THE OPTION TO READ 5 LINES AT A TIME """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total travel time is ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("Average travel time is ",mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type=df['User Type'].value_counts()
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("Gender: There are" , gender)
    else:
        print("There is no gender information in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print("Oldest user was born in " , earliest)
        recent = df['Birth_Year'].max()
        print("Youngest user was born in " , recent)
        common_birth = df['Birth Year'].mode()[0]
        print("Most users were born in " , common_birth)
    else:
        print("There is no birth year information in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
