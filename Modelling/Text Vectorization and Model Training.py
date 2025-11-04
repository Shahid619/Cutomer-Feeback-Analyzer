# this is file for converting cleaned text into vectors then train,test and Evaluate performance
# I used two classical algos (N-Baiyes , and L-Reg ) as dataset was small , and both model performed well Li_Reg > N-baiyes' 

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd , numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB 
from sklearn.linear_model import LogisticRegression


df=pd.read_csv('cleaned.csv')

# changing text to vectors 
vector=TfidfVectorizer(max_features=5000 ,ngram_range=(1,2))
X=vector.fit_transform(df['cleaned'])
y=df['sentiment']

# dense the sparse data
idf_value=X.toarray()

NB=GaussianNB()
LG=LogisticRegression()

X_train, X_test, y_train, y_test=train_test_split(idf_value,y,test_size=0.3,random_state=404)
NB.fit(X_train,y_train)
LG.fit(X_train,y_train)

NB_pred=NB.predict(X_test)
LG_pred=LG.predict(X_test)


print(f'NB classification report : {classification_report(y_test,NB_pred)}')

print(f'\nLR classification report : {classification_report(y_test,LG_pred)}')











# -------------------------------------------------- vectorization completed . below is debugging.

# print(df['cleaned'].head())
# print(f"shape of file : {X.shape} \n")

# let's see vocabs
vocabs=vector.get_feature_names_out()
# print(len(vocabs))
# print(vocabs[:10])


# print(f"{idf_value[0]}")


# print name with idf score 
doc0 = pd.DataFrame({
    'word': vocabs,
    'tfidf': idf_value[0]
}).sort_values(by='tfidf', ascending=False)

# print(doc0.head(10))


# let's visualize it 
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.barh(doc0.head(20)['word'][::-1], doc0.head(20)['tfidf'][::-1])
plt.title("Top 20 TF-IDF Words in Dataset")
plt.xlabel("Average TF-IDF Score")
plt.ylabel("Word / Phrase")
# plt.show()

# create new vectorize csv
