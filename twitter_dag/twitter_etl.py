import pandas as pd

def run_twitter_etl():
    data = pd.read_csv('/home/venkat/airflow/twitter_dag/cleandata.csv')

    data['user'] = 'Elon Musk'

    data = data.rename(columns={'Tweets': 'text', 'Likes': 'favorite_count', 'Retweets': 'retweet_count', 'Date': 'created_at'})
    data = data.drop('Cleaned_Tweets', axis=1)
    data = data[['user', 'text', 'favorite_count', 'retweet_count', 'created_at']]

    data.to_csv('/home/venkat/airflow/twitter_dag/elon_musk_tweets.csv')

