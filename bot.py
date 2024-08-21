import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Your Twitter API v2 credentials from the .env file
bearer_token = os.getenv('BEARER_TOKEN')

def create_tweet(bearer_token, tweet_text):
    url = "https://api.twitter.com/2/tweets"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    payload = {"text": tweet_text}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 201:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")

    print("Tweet posted successfully!")

# Calculate the days left
game_day = datetime(2024, 10, 23)  # Example game date
today = datetime.now()
days_left = (game_day - today).days

# Create the tweet
tweet = f"The Pacers play basketball in {days_left} days"

# Post the tweet
create_tweet(bearer_token, tweet)
