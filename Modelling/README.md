
# 🧠 Stage  — Text Vectorization and Model Training

This stage is all about **converting our cleaned text data into numerical vectors** and then **training ML models** to predict the sentiment (positive, negative, or neutral).
Basically, we move from text → numbers → learning → testing.

---

## 🧩 What We Did

### 1️⃣ Load Cleaned Data

We already have a cleaned file (`cleaned.csv`) which contain:

* `id` — unique number for each feedback
* `text` — original feedback
* `cleaned` — preprocessed text (after removing stopwords, punctuation, etc.)
* `sentiment` — target label (positive / negative / neutral)

We load it using **pandas**:

```python
df = pd.read_csv('cleaned.csv')
```

---

### 2️⃣ Convert Text into Vectors

We used **TF-IDF (Term Frequency – Inverse Document Frequency)** to represent each feedback as a numeric vector.
This helps machine understand which words are important in each feedback.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vector = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X = vector.fit_transform(df['cleaned'])
```

* `max_features=5000` → take top 5000 important words/phrases
* `ngram_range=(1,2)` → use both single words and pairs of words (bi-grams)

Then we make it **dense** (from sparse matrix to normal array) so that Naive Bayes can handle it:

```python
idf_value = X.toarray()
```

---

### 3️⃣ Train-Test Split

We divided the dataset into training and testing parts:

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(idf_value, y, test_size=0.3, random_state=404)
```

* 70% data → training
* 30% data → testing

This helps us **check real performance** of model on unseen data.

---

### 4️⃣ Model Training

We trained two models for comparison:

* **Naive Bayes (GaussianNB)**
* **Logistic Regression**

```python
NB.fit(X_train, y_train)
LG.fit(X_train, y_train)
```

---

### 5️⃣ Predictions & Validation

After training, both models predict the sentiment on test data:

```python
NB_pred = NB.predict(X_test)
LG_pred = LG.predict(X_test)
```

We then check their accuracy and F1-score using `classification_report`.

---

## 📊 Results

| Model                   | Accuracy | Highlights                                         |
| ----------------------- | -------- | -------------------------------------------------- |
| **Naive Bayes**         | 86%      | Works okay, but not perfect with neutral feedbacks |
| **Logistic Regression** | **94%**  | Very stable, balanced between all classes          |

**NB Classification Report**

```
precision    recall  f1-score   support
negative       1.00      0.85      0.92
neutral        0.42      1.00      0.59
positive       0.91      0.84      0.87
accuracy       0.86
```

**LR Classification Report**

```
precision    recall  f1-score   support
negative       0.99      0.95      0.97
neutral        0.67      0.80      0.73
positive       0.95      0.97      0.96
accuracy       0.94
```

---

## 🧾 Observations

* TF-IDF gives better control over feature importance.
* Logistic Regression handled the **neutral** class better than Naive Bayes.
* Neutral samples are still less in dataset → we may need balancing later.
* Accuracy improved a lot after using **bigrams** and removing noisy words.
