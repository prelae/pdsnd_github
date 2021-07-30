import time
import pandas as pd
import numpy as np

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
    city_1 = ""
    day_1 = ""
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs as well as capitalized or uncapitalized text
    city_1 = input("Enter the name of the city (Enter 'chicago\', 'new york city\' or 'washington\') ")
    city_lower = city_1.lower()
    while True:
        if city_lower == "chicago" or city_lower == "new york city" or city_lower == "washington":
            break
        else:
            city_lower = input("Sorry, I didn't catch that. Enter chicago, new york city, or washington: ")
 
    # TO DO: get user input for month (all, january, february, ... , june)
    month_1 = ""
    month_1 = input("Enter the name of the month of any of the first 6 months or 'all\' ")
    month_lower = month_1.lower()
    while True:
        if month_lower == "all" or month_lower == "january" or month_lower == "february" or month_lower == "march" or month_lower == "april" or month_lower == "may" or month_lower == "june":
            break
        else:
            month_lower = input("Sorry, I didn't catch that. Enter any of the first 6 months or 'all\' ")
  
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday
    day_1 = input("Enter the name of the day or 'all\' ")
    day_lower = day_1.lower()
    day_capital = day_lower.capitalize()
    while True:
        if day_capital == "All" or day_capital == "Monday" or day_capital == "Tuesday" or day_capital == "Wednesday" or day_capital == "Thursday" or day_capital == "Friday" or day_capital == "Saturday" or day_capital == "Sunday":
            break
        else:
            day_capital = input("Sorry, I didn't catch that, enter the name of the day or 'all\' ")
    
    city = city_lower
    month = month_lower
    day = day_capital

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
# filter by month if applicable and then by day 
    if month != 'all':       
# use the index of the months list to get the corresponding int    
        months = ['january', 'february', 'march', 'april', 'may', 'june']    
        month = months.index(month) + 1
# filter by month to create the new dataframe      
        df = df[df['month'] == month]
    # filter by day of week if applicable after filtering by month
    if day != 'All':   
# filter by day of week to create the new dataframe  
        df = df[df['day_of_week'] == day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    #popular_hour1 = pd.to_datetime(popular_hour, format="%p")
    #popular_hour1 = strptime(popular_hour, format='%p')
    
    print('The most common month is', common_month) 
    print('The most common day is', common_day)
    print('The most common hour is', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    Start_Station = df['Start Station']
    End_Station = df['End Station']
    # TO DO: display most commonly used start station
    Common_Start_Station = Start_Station.mode()[0]
    # TO DO: display most commonly used end station
    Common_End_Station = End_Station.mode()[0]
    
    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + df['End Station']
    Combination_Stations = df['trip']
    Combination_Stations1 = Combination_Stations.mode()[0]
    
    print('The most common start station is', Common_Start_Station) 
    print('The most common end station is', Common_End_Station)
    print('The most common combination stations are', Combination_Stations1)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    Travel_Time = df['Trip Duration']
    Total_Travel_Time = Travel_Time.sum()
    # TO DO: display mean travel time
    Mean_Travel_Time = Travel_Time.mean()
    print('The total trip duration is:', Total_Travel_Time)
    
    print('The mean trip duration is:', Mean_Travel_Time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    # print value counts for each user type
    Unique_users = df['User Type'].unique()
    user_types = df['User Type'].value_counts()
    print('The two unique users are : ', Unique_users)
    print('The counts for each user are : ', user_types)
    # TO DO: Display counts of gender
    try:
        val = df['Gender']
        if val is not None:
            Unique_genders = df['Gender'].unique()
            gender_counts = df['Gender'].value_counts()
            print('The genders are : ',  Unique_genders)
            print('The counts for each gender are : ', gender_counts)
        else:
            print('Washington data does not contain Genders')
    except KeyError:
         print('Washington data does not contain Genders')
    #  DO: Display earliest, most recent, and most common year of birth
    Min_Birth = 0
    Max_Birth = 0
    Common_Birth = 0
    try:     
        val_1 = df['Birth Year']
        if val_1 is not None:
            Min_Birth = df['Birth Year'].min()
            Max_Birth = df['Birth Year'].max()
            Birth_year = df['Birth Year']
            Common_Birth = Birth_year.mode()[0]
            print('The earliest birthyear is : ', Min_Birth)
            print('The latest birthyear is : ', Max_Birth)
            print('The most common birthyear is : ', Common_Birth)
        else:
            print('Washington data does not contain Birth Years')
    except KeyError:
         print('Washington data does not contain Birth Years')
     
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
