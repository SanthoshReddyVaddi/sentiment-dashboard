import tweepy

# Replace these with your Twitter Developer credentials
API_KEY = "xoZB6oZ4wCenb5UQNrbWO2GCi"
API_SECRET = "DBaLs36IQAnKFtcL3dI11d5StFHxXB5vpVIqylEtrs5Lkn3OhF"
ACCESS_TOKEN = "1945185419718746113-J93VZ41JRhysprnwXfzKDAI0zratE5"
ACCESS_SECRET = "AyWYkdzZnDEM6e21onFC3xMKhgB5dw0FTxWjIR3G8HSQ1"

# Authenticate
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Test connection
print(api.verify_credentials())
print("API connection successful!")

# Simple search example
for tweet in tweepy.Cursor(api.search_tweets, q="Python", lang="en", tweet_mode="extended").items(5):
    print(tweet.created_at, "-", tweet.user.screen_name, ":", tweet.full_text)
