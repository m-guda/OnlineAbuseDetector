from textblob import TextBlob
import matplotlib.pyplot as plt
import sys,tweepy

def percentage(part, whole):
     return 100 * float(part) / float(whole)

# authenticating     
consumerKey = 'M2hFmNS7eecskq76HvhDpbQCe'
consumerSecret = 'BZk7g4yK3cmhVR4vD1qSf78fYvc19mvWf0Zx0GGOoSrPHDyPUu'
accessToken = '975700728508493825-lPX5xMP8L9Koqfb7u3DcZklmgVQyZLU'
accessTokenSecret = 'vI9X2kFlK7VafFuo4UboUwPLhNUDiWWMcHXKUlWInuIgW'
auth = tweepy.OAuthHandler(consumer_key = consumerKey, consumer_secret = consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# input for term to be searched and how many tweets to search
searchTerm = input("idiot")
NoOfTerms = int(input("100"))

# searching for tweets
tweets = tweepy.Cursor(api.search, q=searchTerm).items(NoOfTerms)

# creating some variables to store info
positive = 0
negative = 0
neutral = 0
polarity = 0

# iterating through tweets fetched
for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1

# finding average of how people are reacting
positive = percentage(positive, NoOfTerms)
negative = percentage(negative, NoOfTerms)
neutral =  percentage(neutral, NoOfTerms)
polarity = percentage(polarity, NoOfTerms)


positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " Tweets.")

if (polarity == 0):
    print("Neutral")
elif (polarity < 0.00):
    print("Negative")
elif (polarity > 0.00):
    print("Positive")

labels = ['Positive [' + str(positive) + '%]','Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors =colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(NoOfTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()

