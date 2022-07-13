import time
from datetime import datetime, timedelta

import pandas as pd
 
CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


def city_l():
    c = ''
    while c.lower() not in ['chicago', 'new york', 'washington']:
        c = input('Hello! Let\'s explore some US bikeshare data!\n'
        'Would you like to see data for Chicago, New York, or'
         ' Washington?\n')
        if c.lower() == 'chicago':
            return 'chicago.csv'
        elif c.lower() == 'new york city':
            return 'new_york_city.csv'
        elif c.lower() == 'washington':
            return 'washington.csv'
        else:
            print('error')

    # get user input for month (all, january, february, ... , june)


def month_l():

    month = ''
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month.lower() not in months.keys():
        month = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n')
        if month.lower() not in months.keys():
                print('error')
                month1 = months[month.lower()]
        return ('2017-{}'.format(month1, '2017-{}'.format(month1 + 1)))

    # get user input for day of week (all, monday, tuesday, ... sunday)


def day_l():

    tmonth = month_l()[0]
    month = int(tmonth[5:])
    datav = False
    while datav == False:
           integer = False
           day = input('\nWhich day? Please type your response as an integer.\n')
    while integer == False:
       try:

                integert = True
                day = int(day)
       except ValueError:
                print('error')
                day = input(
                    '\nWhich day? Please type your response as an integer.\n')
    try:
        stdate = datetime(2017, month, day)
        datav = True
    except ValueError as e:
        print(str(e).capitalize())
        enddata = datetime + timedelta(days=1)
    return (str(stdate), str(enddata))


def load_data(dis):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


def vaild(dis):
        if dis.lower() in ['yes', 'no']:
            return True
        else:
            return False


t = 5
h = 0

cin_vaild = False
while cin_vaild == False:
        dis = input('\nWould you like to view data? '
                        '\'yes\' or \'no\'.\n')
        cin_vaild = vaild(dis)
        if cin_vaild == True:
            break
        else:
            print("error")
        if dis.lower() == 'yes':
            print(CITY_DATA[CITY_DATA.columns[0:-1]].iloc[h:t])
        disallot=''
        while disallot.lower() != 'no':
            cin_vaild_2=False
            while cin_vaild_2 == False:
                disallot=input('\nWould you like to view'
                                     ' \'yes\' or \'no\'.\n')
                cin_vaild_2=vaild(disallot)
                if cin_vaild_2 == True:
                    break
                else:
                    print("error")
            if disallot.lower() == 'yes':
                h=h+5
                t=t+5
                print(CITY_DATA[CITY_DATA.columns[0:-1]].iloc[h:t])
            elif disallot.lower() == 'no':
                break




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time=time.time()

    # display the most common month
def most_month(df):

    xmonths=['January', 'February', 'March', 'April', 'May', 'June']
    x=int(df['start_time'].dt.month.mode())
    most_month=xmonths[x - 1]
    print('The most month is {}.'.format(most_month))


    # display the most common day of week
def most_day(df):

    week_in_data=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    x=int(df['start_time'].dt.dayofweek.mode())
    most_day=week_in_data[x]
    print('The most popular day of week for start time is {}.'.format(most_day))


    # display the most common start hour
def popular_hour(df):

    most_hour=int(df['start_time'].dt.hour.mode())
    if most_hour == 0:
        most_hread=12
        ap='am'

    elif 1 <= most_hour < 13:
        ap='am'
        most_hread=most_hour
    elif 13 <= most_hour < 24:
        most_hread=most_hour - 12
        ap='pm'

    print('The most popular hour of day for start time is {}{}.'.format(most_hread, ap))

    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


 
    # print('\nCalculating The Most Popular Stations and Trip...\n')
    # start_time = time.time()
def station_stats_trip(df):

    most_trip=df['journey'].mode().to_string(x=False)
    print('The most popular trip is {}.'.format(most_trip))

def station_stats_stations(df):


    # display most commonly used start station

    most_start=df['start_station'].mode().to_string(x=False)
    print('The most popular start station is {}.'.format(most_start))
    # display most commonly used end station
    most_end=df['end_station'].mode().to_string(x=False)
    print('The most popular end station is {}.'.format(most_end))


    # display most frequent combination of start station and end station trip





def trip_duration_stats(df):

         # display total travel time
    total_trip=df['trip_duration_stats'].sum()
    m, s=divmod(total_trip, 60)
    h, m=divmod(m, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(h, m, s))
              # display mean travel time
    average_trip=round(df['trip_duration_stats'].mean())
    min, sec=divmod(average_trip, 60)
    if min > 60:
        ho, min=divmod(min, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(ho, min, sec))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(min, sec))





    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


 


    # Display counts of user types
def users_type(df):

    c=df.query('user_type == "Customer"').user_type.count()
    s=df.query('user_type == "Subscriber"').user_type.count()

    print('There are {} Subscribers and {} Customers.'.format(s, c))

    # Display counts of gender
def gender_counter(df):

    fc=df.query('gender == "Male"').gender.count()
    mc=df.query('gender == "Male"').gender.count()

    print('There are {} male users and {} female users.'.format(mc, fc))

    # Display earliest, most recent, and most common year of birth

def birth_most(df):
    rece=int(df['birth_most'].max())
    mode=int(df['birth_most'].mode())
    earl=int(df['birth_most'].min())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most birth year is {}.'.format(rece, rece, earl))

    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


def main():

    city=city_l()
    print('Loading data...')
    df=pd.read_csv(city, parse_dates=['Start Time', 'End Time'])

    lab_1=[]
    for col in df.columns:
        lab_1.append(col.replace(' ', '_').lower())
    df.columns=lab_1

    pd.set_option('max_colwidth', 100)

    df['journey']=df['start_station'].str.cat(df['end_station'], sep=' to ')


    time=time_stats()
    if time == 'none':
        df_1=df
    elif time == 'month' or time == 'day':
        if time == 'month':
            fil_low, fil_upp=month_l()
        elif time == 'day':
            fil_low, fil_upp=day_l()
        print('Filtering data...')
        df_1=df[(df['start_time'] >= fil_low) & (df['start_time'] < fil_upp)]
    print('\nCalculating the first statistic...')

    if time == 'none':
        start_time=time.time()

        most_month(df_1)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    if time == 'none' or time == 'month':
        start_time=time.time()

        most_day(df_1)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time=time.time()

    popular_hour(df_1)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time=time.time()

    station_stats_trip(df_1)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time=time.time()

    station_stats_stations(df_1)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time=time.time()

    trip_duration_stats(df_1)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time=time.time()

    users_type(df_1)
    print("That took %s seconds." % (time.time() - start_time))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\nCalculating the next statistic...")
        start_time=time.time()

        gender_counter(df_1)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time=time.time()


        birth_most(df_1)
        print("That took %s seconds." % (time.time() - start_time))

    load_data(df_1)

    rest=input('\nWould you like to restart?\'yes\' or \'no\'\n')
    while rest.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        rest=input('\nWould you like to restart?\'yes\' or \'no\'.\n')
    if rest.lower() == 'yes':
        main()

if __name__ == "__main__":
	main()
