#Improving documentation Part 4 Turn 1: Commit number:1(Refactoring Branch)


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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
        if city.lower() == 'chicago':
            city = 'chicago'
            break
        if city.lower() == 'new york':
            city = 'new york city'
            break
        if city.lower() == 'washington':
            city = 'washington'
            break
        else:
            print('Your input was invalid. Please try one of the following:'
                  'Chicago, New York, or Washington.')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to filter the data by? if no month is prefered: type \'all\' \n> Eg:(all, january, february, march, april, may, june)[june is the last month for the data set] ').lower()
        if month.lower() == 'january':
            month = 'january'
            break
        if month.lower() == 'february':
            month = 'february'
            break
        if month.lower() == 'march':
            month = 'march'
            break
        if month.lower() == 'april':
            month = 'april'
            break
        if month.lower() == 'may':
            month = 'may'
            break
        if month.lower() == 'june':
            month = 'june'
            break
        if month.lower() == 'all':
            month = 'all'
            break
        else:
            print('Your input was invalid. Please try one of the following:'
                  'All, January, February, March, April... etc.')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day would you like to filter the data by? if no month is prefered: type \'all\' \n> Eg:(all, Monday, Tuesday, Wednesday..etc.) ').lower()
        if day.lower() == 'monday':
            day = 'monday'
            break
        if day.lower() == 'tuesday':
            day = 'tuesday'
            break
        if day.lower() == 'wednesday':
            day = 'wednesday'
            break
        if day.lower() == 'thursday':
            day = 'thursday'
            break
        if day.lower() == 'friday':
            day = 'friday'
            break
        if day.lower() == 'saturday':
            day = 'saturday'
            break
        if day.lower() == 'sunday':
            day = 'sunday'
            break
        if day.lower() == 'all':
            day = 'all'
            break
        else:
            print('Your input was invalid. Please try one of the following:'
                  'All, Monday, Tuesday, Wednesday etc.')

    print('-'*40)
    print("City You Picked:",city)
    print("The month you'd like to filter data by:",month)
    print("The day you'd like to filter data by:",day)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        dataFrame - Pandas DataFrame containing city data filtered by month and day
    """
    # load data into pandas datafraome
    dataFrame = pd.read_csv(CITY_DATA[city])

    # start-time is converted to date-time
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
    #https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
    dataFrame['Start Time'] = pd.to_datetime(dataFrame['Start Time'])
    dataFrame['month'] = dataFrame['Start Time'].dt.month
    dataFrame['day_of_week'] = dataFrame['Start Time'].dt.weekday_name
    dataFrame['hour'] = dataFrame['Start Time'].dt.hour

    #filter by month or day
    #https://stackoverflow.com/questions/25873772/how-to-filter-a-dataframe-of-dates-by-a-particular-month-day
    #https://stackoverflow.com/questions/48546091/how-to-filter-a-pandas-datetimeindex-by-day-of-week-and-hour-in-the-day
    if day != 'all':
        dataFrame = dataFrame[ dataFrame['day_of_week'] == day.title()]

    if month != 'all':
        MonthOptionList = ['all','january', 'february', 'march', 'april', 'may', 'june']
        month =  MonthOptionList.index(month) #get the number value of month (we used list instead or creating another set of if statments)
        dataFrame = dataFrame[ dataFrame['month'] == month ]

    return dataFrame


def time_stats(dataFrame):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    startTime = time.time()
    #http://www.cs.ucc.ie/~hoare/Slides3.pdf
        #page 13-14
    # TO DO: display the most common month
    mostCommonMonth = dataFrame['month'].value_counts().idxmax()
    print("The most common month is :", mostCommonMonth)

    # TO DO: display the most common day of week
    mostCommonDayOfWeek = dataFrame['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", mostCommonDayOfWeek)

    # TO DO: display the most common start hour
    mostCommonStartHour = dataFrame['hour'].value_counts().idxmax()
    print("The most common start hour is :", mostCommonStartHour)

    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def station_stats(dataFrame):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    startTime = time.time()

    # TO DO: display most commonly used start station
    mostCommonlyUsedStartStation = dataFrame['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", mostCommonlyUsedStartStation)


    # TO DO: display most commonly used end station
    mostCommonlyUsedEndStation = dataFrame['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", mostCommonlyUsedEndStation)

    # TO DO: display most frequent combination of start station and end station trip
    mostFrequentCombinationOfStartAndEndStation = dataFrame[['Start Station', 'End Station']].mode().loc[0]
    print("most frequent combination of start station and end station trip is: {}, {}" .format(mostFrequentCombinationOfStartAndEndStation[0], mostFrequentCombinationOfStartAndEndStation[1]))

    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def trip_duration_stats(dataFrame):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    startTime = time.time()

    # TO DO: display total travel time
    totalTravelTime = dataFrame['Trip Duration'].sum()
    print("Total travel time :", totalTravelTime)

    # TO DO: display mean travel time
    meanTravelTime = dataFrame['Trip Duration'].mean()
    print("Mean travel time :", meanTravelTime)


    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def user_stats(dataFrame):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    startTime = time.time()

    # TO DO: Display counts of user types
    countsOfUserTypes = dataFrame['User Type'].value_counts()
    print("Counts of user types:\n")
    print(countsOfUserTypes)

    # TO DO: Display counts of gender
    if 'Gender' in dataFrame.columns:
        countsOfGender = dataFrame['Gender'].value_counts()
        print("Counts of Gender:\n")
        print(countsOfGender)
    else:
        print("the Gender data is not present for this city. The column is missing! :( \n")



    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in dataFrame.columns:
        birthYear = dataFrame['Birth Year']
        mostCommonYearOfBirth = birthYear.value_counts().idxmax()
        print("The most common year of birth:", mostCommonYearOfBirth)
        mostRecentYearOfBirth = birthYear.max()
        print("The most recent year of birth:", mostRecentYearOfBirth)
        earliestYearOfBirth = birthYear.min()
        print("The moost earliest year of birth:", earliestYearOfBirth)
    else:
        print("the Birth Year data is not present for this city. The column is missing! :( \n")

    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)

def display_data(dataFrame):
    '''display data: 10 rows shown if user says yes
       else just stop display data loop
    Args:
        dataFrame: dataframe of bikeshare data
    Returns:
        If (yes), then 10 rows of data
        if (no), stop
        else [enter valid input]
    '''
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
    lineNumber = 0

    while True:
        displayData = input('\nWould you like to view individual trip data? type \'yes\' or \'no\'.\n').lower()
        if displayData == 'yes':
            print(dataFrame.iloc[lineNumber:lineNumber+5])
            lineNumber += 5
        if displayData == 'no':
            break
        if displayData != 'no' and displayData!='yes':
            print("\nPlease enter valid input and try again!")


def main():
    while True:
        city, month, day = get_filters()
        dataFrame = load_data(city, month, day)

        time_stats(dataFrame)
        station_stats(dataFrame)
        trip_duration_stats(dataFrame)
        user_stats(dataFrame)
        display_data(dataFrame)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
