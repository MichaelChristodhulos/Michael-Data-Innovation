import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
path=''
city=''

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!'.title())
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city=input('please choose one of These cities ( '.title() + ','.join(CITY_DATA.keys()).title() + ' ) :- ')
    file = CITY_DATA.get(city.strip().lower())
    while file is None :
        city = input('please valid value choose one of These cities ( '.title() + ','.join(CITY_DATA.keys()).title() + ' ) :-  ')
        file = CITY_DATA.get(city.strip().lower())


    print('you choose '.title()+file+' city'.title())

    # get user input for month (all, january, february, ... , june)
    month_index=None
    while month_index is None :
        try:
            months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
            month = input('please choose one of the following month or all for all month :- '.title() + ' , '.join(months).title()+' :- ').strip().lower()
            month_index = months.index(month)
        except ValueError:
            print('Please Enter valid value choose one of the following value '.title()+ ' , '.join(months).title()+ ' :- ')
        else:
            print('you choose valid Value you choose '.title()+month.title()+' ')



    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_index = None
    while day_index is None :
        try:
            days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
            day = input('please choose one of the following days or all for all days :- '.title() + ' , '.join(days).title()+' :- ').strip().lower()
            day_index = days.index(day.strip().lower())
        except ValueError:
            print('Please Enter valid value choose one of the following value '.title()+ ' , '.join(days).title()+' :- ')
        else:
            print('you choose valid Value you choose '.title()+day.title()+' ')

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
    df=None
    file = CITY_DATA.get(city.lower())
    if file is not None:
        try:
            # df = pd.read_csv('D:/udicity/chicago_3.csv')
            df = pd.read_csv(path + file)
        except FileNotFoundError:
            print('file not found'.title())
        else:
            print('File loaded for '.title()+city+' city '.title())
    else:
        print('please choose one of These cities ('.title() + ','.join(CITY_DATA.keys()).title() + ')')



    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # df['day_of_week'] =df['Start Time'].dt.weekday_name deprecated
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months.index(month.lower())+ 1
        df = df[df.month == month_index]
        print('Data filtered by '.title()+month+' Month')
    else :
        print('Data about all Six Months '.title())


    df['day_of_week'] = df['Start Time'].dt.day_name()
    if day != 'all':
        df = df[df.day_of_week == day.title()]
        print('Data filtered by '.title() + day.title() + ' Day')
    else:
        print('Data about all Week days '.title())

    # print(df)
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df = pd.DataFrame(df)
    # display the most common month
    # month_mode = df['month'].value_counts().mode()[0]
    month_mode=df['month'].value_counts().max()
    # print(month_mode)
    month_name=calendar.month_name[df['month'].value_counts().index.values[0]]
    # print(month_name)

    print('the most common month is :- '.title()+str(month_name).title()+' Month Has '+str(month_mode).title()+' Value')


    # display the most common day of week
    # day_mode = df['day_of_week'].value_counts().mode()[0]
    day_mode = df['day_of_week'].value_counts().max()
    # day_name = calendar.day_name[df['day_of_week'].value_counts().index.values[0]]
    day_name = df['day_of_week'].value_counts().index.values[0]
    print('the most common day is :- '.title()+str(day_name).title()+' Day Has '+str(day_mode).title()+' Value')


    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Hour'] = pd.to_datetime(df['Start Time'],format='%m/%d/%Y %H:%M').dt.hour
    # hour_mode=df['Hour'].value_counts().mode()[0]
    hour_mode = df['Hour'].value_counts().max()
    hour_name = df['Hour'].value_counts().index.values[0]
    print('the most common Hour is :- '.title() + str(hour_name).title() + ' Hour Has ' + str(hour_mode).title() + ' Value')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    start_Station_mode = df['Start Station'].value_counts().max()
    start_Station_name = df['Start Station'].value_counts().index.values[0]
    print('the most common Start Station is :- '.title() + str(start_Station_name).title() + ' Station Has ' + str(start_Station_mode).title() + ' Value')

    # display most commonly used end station
    end_Station_mode = df['End Station'].value_counts().max()
    end_Station_name = df['End Station'].value_counts().index.values[0]
    print('the most common End Station is :- '.title() + str(end_Station_name).title() + ' Station Has ' + str(end_Station_mode).title() + ' Value')

    # display most frequent combination of start station and end station trip
    # most_trips=df[['Start Station', 'End Station']].value_counts().max()
    # most_start_station = df[['Start Station', 'End Station']].value_counts().index.values[0][0]
    # most_end_station = df[['Start Station', 'End Station']].value_counts().index.values[0][1]
    df['Start-End-Station']=df['Start Station']+' - '+df['End Station']
    most_trips = df['Start-End-Station'].value_counts().index.values[0]
    most_trips_number=df['Start-End-Station'].value_counts().max()
    print('most frequent combination start to end station is: - '.title()+str(most_trips) +' Has '+str(most_trips_number)+
          ' trips')
    # print(most_trips,most_start_station,most_end_station)
    # print('most frequent combination start from '.title()+str(most_start_station)+' station and end to '.title()+
    #        str(most_end_station)+' Station with trips number '.title()+str(most_trips))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    sum_trip_duration=sum(df['Trip Duration'].values)
    print('total travel time :- '.title()+str(sum_trip_duration))

    # display mean travel time
    average_trip_duration = df['Trip Duration'].values.mean()
    print('travel time average :- '.title() + str(average_trip_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_by_user_type = df['User Type'].value_counts()
    print('counts Per user types'.title())
    print(count_by_user_type)

    # Display counts of gender
    if 'Gender' not in df.head(0):
        print('this city has no data about gender ')
    else:
        count_by_user_type = df['Gender'].value_counts()
        print('counts Per Gender types'.title())
        print(count_by_user_type)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.head(0):
        print('this city has no data about year of birth'.title())
    else:
        # x = df['Birth Year'].isnull().sum().sum()
        # print('nan values ',x)
        # x = df['Birth Year'].fillna(0)

        birth_year_values=df['Birth Year'].value_counts()
#         print(birth_year_values)
#         print()
        earliest_year=birth_year_values.index.min()
        most_recent_year = birth_year_values.index.max()
        most_common_recent_year_values = max(birth_year_values.values)
        most_common_year        = birth_year_values.sort_values(ascending=False).index[0]
        print('earliest Birth year is :- '.title()+str(earliest_year))
        print('most recent Birth year is :- '.title() + str(most_recent_year))
        print('most common Birth year is :- '.title() + str(most_common_year)+' with trips number :- '.title()+str(most_common_recent_year_values))
        # print(earliest_year,most_recent_year,most_common_year,most_common_recent_year_values)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def disply_row_data(df):
    """Displays row data 5 by 5 in case user ask for more 5 data  ."""
    df['month'] = pd.to_datetime(df['month'])
    df['month']=df['month'].dt.month_name

    print('dataframe length',len(df.index))
    display=input('do you want to display row data enter n for no and y for yes '.title()).strip().lower()
    while display !='n' and display !='y' :
        display = input('please enter n for no and y for yes '.title()).strip().lower()

    print(df.head(0))

    for i in range(0,len(df.index),5):
        if (len(df.index)-i)>=5:
            print(df.iloc[[i, i + 1, i + 2, i + 3, i + 4]])
        else:
            print('last data inside data frame '.title())
            print(df[i:len(df.index)])
            break

        display=None
        while display != 'n' and display != 'y':
            display = input('for more 5 rows please enter y or n for exit '.title()).strip().lower()
        if display=='n':
            break



    return None



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disply_row_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

# city, month, day = get_filters()
# df = load_data(city, month , day)
# time_stats(df)
# station_stats(df)
# trip_duration_stats(df)
# user_stats(df)
# disply_row_data(df)






