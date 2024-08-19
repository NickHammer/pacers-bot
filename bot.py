import tweepy
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Your Twitter API credentials from the .env file
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate with Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Calculate the days left
game_day = datetime(2024, 10, 23)  # Example game date
today = datetime.now()
days_left = (game_day - today).days

# Create the tweet
tweet = f"The Pacers play basketball in {days_left} days"
api.update_status(tweet)
