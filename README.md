>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
bikeshare.py created September 16th 2022.
README.md file created January 14th 2023.

### Project Title
Explore US Bikeshare Data

### Description
A Python script has been created to explore data related to bike share systems for three major cities in the US: Chicago, New York City and Washington.

The Python script imports the data of these three cities and takes in raw input to create an interactive experience in the terminal hat answers questions about the dataset.

The experience is interactive because depending on a user's input, the answers to the questions will change. There are four questions that will change the answers:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If the filter month is chosen:) Which month - January, February, March, April, May, or June?
4. (If the filter day is chosen:) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

Based on the user’s answer on above four questions, code has been written to provide information on the following topics:

1. Popular times of travel (i.e., occurs most often in the start time)
    - most common month
    - most common day of week
    - most common hour of day
2. Popular stations and trip
    - most common start station
    - most common end station
    - most common trip from start to end (i.e., most frequent combination of start station and end station)
3. Trip duration
    - total travel time
    - average travel time
4. User info
    - counts of each user type
    - counts of each gender (only available for NYC and Chicago)
    - earliest, most recent, most common year of birth (only available for NYC and Chicago)


### Files used
Files used in this project are:
- a Python script called bikeshare.py
- three city dataset files called chicago.csv, new_york_city.csv and washington.csv


### Credits
Resource references used for writing the script in the file bikeshare.py:
- Udacity - Data Analyst Nanodegree Program: Input from lessons in the "Introduction to Python" course.
- https://stackoverflow.com/questions/50498557/input-prompt-within-a-while-true-loop
- https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-respons
- https://stackoverflow.com/questions/60339049/weekday-name-from-a-pandas-dataframe-date-object
- https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe
- https://www.mytecbits.com/internet/python/seconds-to-days-hours-minutes
- https://stackoverflow.com/questions/41286569/get-total-of-pandas-column
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html
- https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
- https://stackoverflow.com/questions/7837722/what-is-the-most-efficient-way-to-loop-through-dataframes-with-pandas
- https://stackoverflow.com/questions/1016814/what-should-i-do-with-unexpected-indent-in-python
- http://net-informations.com/python/err/eol.htm#:~:text=An%20EOL%20(%20End%20of%20Line,the%20end%20of%20the%20line%20.
- https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week
