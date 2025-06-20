#extract, transform and load used in reddit_pipeline
from praw import Reddit
import sys
import traceback
import pandas as pd 
from datetime import datetime
from utils.utils import *


#flow: connect -> extract_posts -> transform
def connect_reddit(client_id,secret,agent):
    try:
        reddit = Reddit(
            client_id=client_id,
            client_secret=secret,
            user_agent=agent
        )
        print("Connected to Reddit")
        return reddit
    except Exception as e:
        print("Exception occurred:")
        traceback.print_exc()
        sys.exit(1)

def extract_posts(instance,subreddit,time_filter,limit):
    subreddit=instance.subreddit(subreddit)
    posts = subreddit.top(time_filter,limit)
    list_keys = ["id",'title','selftext',
                 'author','created_utc','subreddit',
                 'num_comments','score','upvote_ratio',
                 'url','is_self','over_18','stickied',
                 'spoiler', 'permalink', 'num_crossposts']

    posts_list=[]
    
    #quick look
    for post in posts:
        post_data={}
        for key in list_keys:
            value = getattr(post,key,None)
            #because author values is redditor values, have to use str to get value
            if key in ("author","subreddit"):
                post_data[key] = str(value) if value else None
            else:
                post_data[key]=value
        posts_list.append(post_data)

    return posts_list

def transform_posts(post_df):
    #convert timestamp
    post_df['created_utc'] = post_df['created_utc'].apply(lambda x:convert_datetime(x) if pd.notnull(x) else x)

    #create columns to category interaction with post 
    post_df['engagement_level'] = post_df.apply(lambda row: engagement_level(row['num_comments'], row['score']), axis=1)

    #selftext is long or short, can filter the text which came up much (later)
    post_df['length_category'] = post_df['selftext'].map(lambda x:length_text_level(x))

    #fill missing value
    post_df = fill_missing_values(post_df)

    #drop selftext
    post_df.drop('selftext',axis=1,inplace=True)

    return post_df

def load_file(post_df:DataFrame,file_path:str):
    post_df.to_csv(file_path, index=False)
    
    