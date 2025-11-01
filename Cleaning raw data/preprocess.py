# This is project 1  preprocessing file

import spacy, re,pandas as pd ,emoji

df=pd.read_csv("messy.csv")
# print(df.head())


# converting emojis to text 
df['cleaned']=df['text'].apply(emoji.demojize)
# print(df.head)


# regex cleaning to make sentence clear 
def regex_cleaning(text):
    text=re.sub(r'www\S+|http\S+',"",text)
    text=re.sub(r'@\w+|#\w+' ,"",text)
    text=text.lower().strip()
    return text

# --------------------------------------------------
# def cleaning(col):                                    |
#     return [regex_cleaning(row) for row in col]       |
# cleaned_sentences=cleaning(df['cleaned'])             |
# ----------------------------------------------------

# instead of using above code do below one.
df['cleaned']=df['cleaned'].apply(regex_cleaning)


# stopwording to remove extra words 
def stop_wording(text):
    model = spacy.load('en_core_web_sm')
    model_data=model(text)   
    clean_row=[words.text for words in model_data if not words.is_stop and not words.is_punct]
    return clean_row

df['cleaned']=df['cleaned'].apply(stop_wording)
# print(df['cleaned'])


# df.to_csv('cleaned.csv',index=False)
