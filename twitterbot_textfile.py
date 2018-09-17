# Importing Tweepy library to interact with the Twitter API
import tweepy

# Importing module time to automate Tweets in a time-based way
from time import sleep

# Importing Twitter credentials from credentials.py
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Open text file verne.txt for reading
my_file = open('favorite_quotes.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
# 365 lines to quote once a day for the whole year
file_lines = my_file.readlines()

# Close file
my_file.close()

def tweet():
    # Create a for loop to iterate over file_lines
    for line in file_lines:
        try:
            print(line)

            # Add if statement to ensure that blank lines are skipped
            if line != '\n':
                api.update_status(line)
                # Add sleep method to only tweet once a day
                sleep(86400)
            # Add an else statement with pass to conclude the conditional statement
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)
tweet()
