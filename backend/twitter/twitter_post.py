import os
from dotenv import load_dotenv
import tweepy

load_dotenv()


def post_tweet(tweet_content):
    # Get credentials from environment variables
    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    # Initialize the client with OAuth 1.0a credentials
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # Post the tweet using Client.create_tweet()
    try:
        response = client.create_tweet(text=tweet_content)
        print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
        return True
    except Exception as e:
        print(f"Error posting tweet: {str(e)}")
        raise


if __name__ == "__main__":
    post_tweet("This is a test tweet.")
