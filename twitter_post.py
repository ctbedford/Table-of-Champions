import os
from dotenv import load_dotenv
import tweepy
from flask import Flask, request, render_template_string
import webbrowser
import threading

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Get credentials from environment variables
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')

# Initialize OAuth 1.0a handler
auth = tweepy.OAuthHandler(
    consumer_key, consumer_secret, callback='http://127.0.0.1:5000/callback')

# Global variables
access_token = None
access_token_secret = None
tweet_status = None


@app.route('/')
def home():
    auth_url = auth.get_authorization_url()
    return f'<a href="{auth_url}">Authenticate with Twitter</a>'


@app.route('/callback')
def callback():
    global access_token, access_token_secret
    verifier = request.args.get('oauth_verifier')
    access_token, access_token_secret = auth.get_access_token(verifier)
    return render_template_string("""
        <h1>Authentication Successful!</h1>
        <p>You can now post your tweet.</p>
        <form action="/post_tweet" method="post">
            <input type="submit" value="Post Tweet">
        </form>
    """)


@app.route('/post_tweet', methods=['POST'])
def post_tweet():
    global access_token, access_token_secret, tweet_status
    try:
        # Initialize the client with OAuth 1.0a credentials
        client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

        # Read the tweet from the file
        with open('twitter_post.txt', 'r') as f:
            tweet_text = f.read().strip()

        # Post the tweet using Client.create_tweet()
        response = client.create_tweet(text=tweet_text)
        tweet_status = f"Tweet posted successfully! Tweet ID: {
            response.data['id']}"
    except Exception as e:
        tweet_status = f"Error posting tweet: {str(e)}"

    return render_template_string("""
        <h1>Tweet Status</h1>
        <p>{{ status }}</p>
        <a href="https://twitter.com" target="_blank">View on Twitter</a>
    """, status=tweet_status)


def run_flask():
    app.run(port=5000)


if __name__ == '__main__':
    print("Starting the authentication process...")
    webbrowser.open('http://127.0.0.1:5000')

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Application terminated by user.")
