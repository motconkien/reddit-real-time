#function called functions from etl

from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, extract_posts, transform_posts, load_file
import pandas as pd

def reddit_pipeline(file_name,subreddit,time_filter='day',limit=None):
    print(f"Client ID: {CLIENT_ID!r}")
    print(f"Secret: {SECRET!r}")


    #connect to Reddit
    instance = connect_reddit(CLIENT_ID, SECRET, 'DE_real_time_data')

    #extraction
    posts = extract_posts(instance,subreddit,time_filter,limit)
    
    #tranformation
    posts_df = pd.DataFrame(posts)
    posts_df = transform_posts(posts_df)

    #loading to folder 
    file_path = f"{OUTPUT_PATH}/{file_name}.csv"
    load_file(posts_df,file_path)
    return file_path