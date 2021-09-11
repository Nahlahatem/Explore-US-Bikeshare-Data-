import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city=input('\nplease Enter the city:')
        city=city.lower()
        if city=='chicago'or city=='new york city'or city=='washington':
            break
        else:
           print('\nThe city is not true please try again')
           continue 
        
        

    # TO DO: get user input for month (all, january, february, ... , june)
    print(' \nplease Enter the month ')
    while True :
        month=input()
        month=month.lower()
        if month=='all'or month=='january'or month=='february' or month=='march'or month=='april'or month=='may'or month=='june'or month=='july'or month=='january'or month=='august'or month=='september'or month=='november'or month=='december' :
           break
        else:
            print('\nThe month is not true please try again')
            continue
    
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\n please Enter the day ')
    while True :
        day=input()
        day=day.lower()
        if day=='all'or day=='monday'or day=='tuesday'or day=='wednesday'or day=='thursday'or day=='friday'or day=='saturday'or day=='sunday':
            break
        else:
           print('\nThe day is not true please try again')
           continue 

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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] =df['Start Time'].dt.month
    popular_month=df['month'].mode()[0]
    print('\nThe most common month: ',popular_month)


    # TO DO: display the most common day of week
    df['day of week'] =df['Start Time'].dt.weekday_name
    popular_day=df['day of week'].mode()[0]
    print('\nThe most common day of week: ',popular_day)

    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('\nThe most common start hour: ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('\n The most popular commonly used start station: ',popular_start_station)

    # TO DO: display most commonly used end station
    popular_End_station=df['End Station'].mode()[0]
    print('\n The most popular commonly used end station: ',popular_End_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End station']  = df['Start Station']+ " " + df['End Station']
    popular_startEnd_station = df['Start End station'].mode()[0]
    print('\n The most popular commonly used start and end station: ',popular_startEnd_station)

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=float(df['Trip Duration'].sum())
    totalTime_day=timedelta(seconds=total_time)
    totalTime_minSec=str(totalTime_day).split(",")[1].split(":")
    print("Total travel time:{} ({} days{} hours {} minutes {:4.2f} secs)".format(totalTime_day,totalTime_day.days,totalTime_minSec[0],totalTime_minSec[1],float(totalTime_minSec[2])))


    # TO DO: display mean travel time
    mean_Time = df['Trip Duration'].mean()
    print('\nMean travel time:{:8.2f} secs '.format(mean_Time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

    
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    if city!='washington':
        print('\nCalculating User Stats...\n')
        start_time = time.time()

    # TO DO: Display counts of user types
        counts_user_types=df['User Type'].value_counts()
        print('\nCounts of user types:',counts_user_types)
    

    # TO DO: Display counts of gender
        counts_gender=df['Gender'].value_counts()
        print('\nCounts of gender: ',counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        popular_yearofBirth=df['Birth Year'].mode()[0]
        print('\nMost common year of birth',popular_yearofBirth)
        recent_yearofBirth=df['Birth Year'].max()
        print('\nMost recent year of birth',recent_yearofBirth)
        
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df):
    i = 0
    raw = input("\nWould you like to print 5 rows data? Enter 'yes' or 'no' \n").lower() 
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        data= df.iloc[i:i+5]  
        if data.empty :
            print("No more data to display")
            break          
        else: 
            print(data)
            raw =  input("\nWould you like to print 5 rows data? Enter 'yes' or 'no'\n").lower() 
            i += 5          
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
