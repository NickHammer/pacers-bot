# import tweepy
# from datetime import datetime
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Your Twitter API credentials from the .env file
# api_key = os.getenv('API_KEY')
# api_secret_key = os.getenv('API_SECRET_KEY')
# access_token = os.getenv('ACCESS_TOKEN')
# access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# # Authenticate with Twitter using OAuth 1.0a User Context
# auth = tweepy.OAuthHandler(api_key, api_secret_key)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True)

# # Verify the credentials
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except tweepy.TweepyException as e:
#     print(f"Error during authentication: {e}")
#     exit()

# # Calculate the days left until the game
# game_day = datetime(2024, 10, 23)  # Example game date
# today = datetime.now()
# days_left = (game_day - today).days

# # Create the tweet
# tweet = f"The Pacers play basketball in {days_left} days"

# # Post the tweet and handle potential errors
# try:
#     api.update_status(tweet)
#     print("Tweet posted successfully!")
# except tweepy.TweepyException as e:
#     print(f"Error posting tweet: {e}")
import tweepy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Verify authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except tweepy.TweepyException as e:
    print(f"Error during authentication: {e}")
    exit()

# Post a simple tweet
tweet = "PAcurs"
try:
    api.update_status(tweet)
    print("Tweet posted successfully!")
except tweepy.TweepyException as e:
    print(f"Error posting tweet: {e}")
