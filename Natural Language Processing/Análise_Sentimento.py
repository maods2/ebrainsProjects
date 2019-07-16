# Aplicação genérica para pesquisar tweets com um conteúdo 
# desejado, retornando um vetor de tweets e log em seguida
# anlisando o sentimento deles.


import tweepy
from textblob import TextBlob


# In[11]:


# Chaves de acesso fornecidas pelo twitter

consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

# Autenticando o acesso
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)


# In[12]:


# Pesquisa de tweets que tenham o termo "shallow now"
public_tweets = api.search('shallow now')

# Percorre vetor onde tweets foram armazenados
for tweet in public_tweets:
    print(tweet.text)
    
# Analisa o sentimento do tweet
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")


# In[13]:


public_tweets

