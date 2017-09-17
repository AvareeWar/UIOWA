# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

    
# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1733593110-HkSeAJ2IWbWykgupHZHYaZkCGEhUMM3E8l2x4qi'
ACCESS_SECRET = 'DKxpNYKFqj2pmUabow7jtMb3vkwP2N99GXjr1TM21q1f6'
CONSUMER_KEY = 'bQETXaB5RALb7kkZRuphNEsj0'
CONSUMER_SECRET = '7QSNB558sZDWlVCNK9fD9blDJ99wKLz5pabEVxgZBcpmDoGadO'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)
            
# Search for latest tweets about "#nlproc"
print twitter.search.tweets(q='#flooded')

#twitter.search.tweets(q='#nlproc', result_type='recent', lang='en', count=10)
