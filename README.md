# Cutomer-Feeback-Analyzer
this project is a real-world NLP challenge

  # Starting

## Stage1 : 
  Data tested has been generated using AI for testing purpose.

## 🧹 Stage 2: Preprocessing — Cleaning the Customer Feedbacks

### 📘 Purpose

In this stage I clean all the feedback text before sending it to NLP model.
Main goal is to make text clear, simple, and ready for analysis.
Because raw feedback has too much noise — emojis, hashtags, links, Urdu+English mix, and random characters — all this confuse model.

---

### ⚙️ What this stage do

I make a pipeline that perform these main steps:

1. **Text Normalization**

   * Change all words to lowercase.
   * Remove extra spaces, punctuation, and URLs.
   * Example: “WOW!!! Service was Great!!!” → “wow service was great”

2. **Stopword Removal**

   * I remove common useless words like *is, am, the, hai, main, ka, ke, ki*, etc.
   * These words not help model to understand feeling or topic.
   * Used stopword list from NLTK for English and plan to build one for Urdu later.

3. **Tokenization**

   * Break sentence into words (tokens).
   * Example: “service was great” → `[“service”, “great”]`

4. **Lemmatization / Stemming**

   * Convert words to their base form.
   * Example: “services”, “serving” → “service”.
   * Helps to treat all same-meaning words as one.

---

### 🔧 Libraries Used

* **re** → for regex cleaning (remove URLs, mentions, hashtags).
* **nltk** → for stopwords, tokenization, lemmatization.
* **emoji** → (later) for removing or converting emojis to text like “😊” → “happy”.
* **contractions** → (later) to expand short forms like “don’t” → “do not”.
* **textblob** → (optional) for correction and sentiment check.

---

### 🧱 Structure of Data after this Stage

Now my dataset looks like this:

| id | text                     | cleaned               |
| -- | ------------------------ | --------------------- |
| 1  | “Service was excellent!” | “service excellent”   |
| 2  | “Product not working 😞” | “product not working” |

✅ `id` = just serial number (will drop later)
✅ `text` = original feedback
✅ `cleaned` = ready text for next NLP step

---

### 🧠 Challenges I Faced

| Problem                                   | Why it happened                                     | How I solved it                                                   |                                 |        |
| ----------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------- | ------ |
| **Too much noise in text**                | People write URLs, tags, emojis                     | Used regex to remove `http`, `www`, `@username`, `#tag`           |                                 |        |
| **Regex not working**                     | I wrote spaces around `                             | ` symbol                                                          | Learned correct syntax: `r'@\w+ | #\w+'` |
| **Extra spaces after cleaning**           | Multiple spaces remained after removing URLs        | Added `re.sub(r'\s+', ' ', text)`                                 |                                 |        |
| **Confusion between index and id column** | CSV saved both index and `id`                       | Used `df.drop(columns=['id'])` and `index=False`                  |                                 |        |
| **Urdu + English mix text**               | Some feedbacks are bilingual                        | Decided to clean English first, plan Urdu normalization later     |                                 |        |
| **Code looked confusing**                 | Many steps in one function                          | Broke it into small functions: regex cleaning, tokenization, etc. |                                 |        |
| **Understanding what each line does**     | I didn’t know why `.strip()`, `.lower()`, etc. used | Tested step-by-step and understood purpose manually               |                                 |        |

---

### 🧭 Lessons Learned

* Always test small pieces of code to understand logic.
* Regex spaces matter — one wrong space can break cleaning.
* Cleaning text is not “one formula”; it depends on language and data style.
* Keep both raw and cleaned versions — helps debug errors later.

---




