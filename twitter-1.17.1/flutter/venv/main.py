from flask import Flask, render_template, request
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


try:
    import json
except ImportError:
    import simplejson as json

app = Flask(__name__)

@app.route('/')
def index():
    # Variables that contains the user credentials to access Twitter API
    ACCESS_TOKEN = '1733593110-HkSeAJ2IWbWykgupHZHYaZkCGEhUMM3E8l2x4qi'
    ACCESS_SECRET = 'DKxpNYKFqj2pmUabow7jtMb3vkwP2N99GXjr1TM21q1f6'
    CONSUMER_KEY = 'bQETXaB5RALb7kkZRuphNEsj0'
    CONSUMER_SECRET = '7QSNB558sZDWlVCNK9fD9blDJ99wKLz5pabEVxgZBcpmDoGadO'
    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_stream = TwitterStream(auth=oauth)
    iterator = twitter_stream.statuses.sample()

    tweet_count = 1000
    for tweet in iterator:
        try:
            #print(json.dumps(tweet))
            if tweet_count <= 0:
                break
            if 'text' in tweet:  # only messages contains 'text' field is a tweet
                tweet_count -= 1
                print "text: " + tweet['text']  # content of the tweet
                print "location: " + tweet['user']['location']
                print "tweet: " + tweet['user']['name']  # name of the user, e.g. "Wei Xu"
                # print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"

                hashtags = []
                for hashtag in tweet['entities']['hashtags']:
                    hashtags.append(hashtag['text'])
                print "hashtags: ", hashtags

        except:
            print "cucked"
            # read in a line is not in JSON format (sometimes error occured)
            continue


    return render_template('index.html')


    '''# Import the necessary methods from "twitter" library
    from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

    # Variables that contains the user credentials to access Twitter API
    ACCESS_TOKEN = '1733593110-HkSeAJ2IWbWykgupHZHYaZkCGEhUMM3E8l2x4qi'
    ACCESS_SECRET = 'DKxpNYKFqj2pmUabow7jtMb3vkwP2N99GXjr1TM21q1f6'
    CONSUMER_KEY = 'bQETXaB5RALb7kkZRuphNEsj0'
    CONSUMER_SECRET = '7QSNB558sZDWlVCNK9fD9blDJ99wKLz5pabEVxgZBcpmDoGadO'
    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    # Initiate the connection to Twitter Streaming API
    twitter_stream = TwitterStream(auth=oauth)
    # Get a sample of the public data following through Twitter
    iterator = twitter_stream.statuses.sample()

    # Print each tweet in the stream to the screen
    # Here we set it to stop after getting 1000 tweets.
    # You don't have to set it to stop, but can continue running
    # the Twitter API to collect data for days or even longer.
    tweet_count = 100
    tweets = []

    for tweet in iterator:
        tweet_count -= 1
        # Twitter Python Tool wraps the data returned by Twitter
        # as a TwitterDictResponse object.
        # We convert it back to the JSON format to print/score
        tweets.append(json.dumps(tweet))

        # The command below will do pretty printing for JSON data, try it out
        # print json.dumps(tweet, indent=4)

        if tweet_count <= 0:
            break
    print 4
    ans = ""
    for i in tweets:
        ans = ans+str(tweets)
    return ans
    #return tweets
'''
