#include functions for etl

from datetime import datetime
import pandas as pd 
from pandas import DataFrame
#function to convert datetime 
def convert_datetime(time): 
    return datetime.utcfromtimestamp(time).isoformat()

#function to leverage engagement
def engagement_level(num_comments, score):
    if num_comments > 100 and score > 500:
        engagement_level = "high"
    elif num_comments > 20:
        engagement_level = 'medium'
    else:
        engagement_level = 'low'
    return engagement_level

#function to leverage length of text
def length_text_level(selftext):
    length = len(selftext)
    if length == 0:
        length_category = 'empty'
    elif length < 300:
        length_category = 'short'
    else:
        length_category = 'long'
    return length_category

#solve mising values
def fill_missing_values(df:DataFrame) -> DataFrame:
    for col in df.columns:
        if df[col].isnull().any():
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col].fillna(df[col].mean(),inplace=True)
            else:
                df[col].fillna(df[col].mode().iloc[0], inplace=True)
    return df
