# Sports vs Politics Text Classification

**CSL7640: Natural Language Understanding**

**Assignment 1 Problem 4**

**Name:** Namya Dhingra

**Roll No:** B23CS1040

## 1. Project Overview

This project implements a complete **end-to-end NLP pipeline** to classify news articles into two categories:

- **Sports**
- **Politics**

The system is built from scratch, covering:

- Data collection
- Query filtering
- Web scraping
- Dataset construction
- Manual NLP preprocessing
- Manual Bag-of-Words feature extraction
- Model training & evaluation
- Comparative analysis of three machine learning models

The goal is to demonstrate both **practical implementation skills** and **theoretical understanding** of Natural Language Processing workflows.

## 2. System Architecture

The complete workflow follows this pipeline:

```
Raw QueryDataset(india news.csv)
        ↓
QueryFiltering(filter_queries.py)
        ↓
FilteredURLs(url_indian_news.csv)
        ↓
WebScraping(scrape_articles.py)
        ↓
ExtractedArticles(indian_news_with_text.csv)
        ↓
StructuralCleaning(load_data.py)
        ↓
Manual NLPPreprocessing(preprocess.py)
        ↓
Feature Extraction + ModelTraining(train_models.py)
```

## 3. Repository Structure

```
├── filter_queries.py
├── scrape_articles.py
├── build_dataset.py
├── load_data.py
├── preprocess.py
├── train_models.py
├── india_news.csv
├── bbc-text.csv
├── indian_news_with_text.csv
├── README.md
└── Report.pdf
```

Full repository:

🔗 https://github.com/namyadhingra/NLP_Classifies-SportsVsPolitics

## 4. Datasets Used

### 4.3 India News Dataset

- Contains search queries and associated URLs
- Filtered using rule-based substring matching
- Extracted: **255 URLs**

### 4.2 BBC News Dataset

- Public dataset (commonly available on Kaggle)
- Total samples used: **994**
- Used to supplement training data
- Categories include Sports and Politics

## 5. Query Filtering

Implemented in `filter_queries.py`.

Instead of exact matching, **substring matching** was used for robustness:

- Queries containing `"politic"` or `"election"` → Politics
- Queries containing `"cricket"` or `"sport"` → Sports

Output:

- 255 filtered URLs

## 6. Web Scraping

Implemented in `scrape_articles.py`.

Steps:

1. HTTP request using `requests`
2. HTML parsing using `BeautifulSoup`
3. Extract `<p>` tag content
4. Remove articles shorter than 200 characters
5. Store category, URL, and text in CSV

Ethical practice:

- ⏱ 1-second delay between requests

Output:

```
indian_news_with_text.csv
```

## 7. Data Cleaning

Implemented in `load_data.py`.

Operations:

- Load CSV using pandas
- Keep only `category` and `text`
- Remove missing values

### Final Dataset:

- **Total Samples:** 233
- **Politics:** 152
- **Sports:** 81

## 8. Manual NLP Preprocessing (From Scratch)

No use of:

- NLTK tokenizers
- sklearn vectorizers

Everything implemented manually.

### 8.1 Tokenization

- Convert text to lowercase
- Extract alphabetic tokens using regex

### 8.2 Stopword Removal

- Manually defined stopword list
- Remove words shorter than 3 characters

### 8.3 Manual Bag of Words

Steps:

1. Build vocabulary mapping: `word → index`
2. Count word frequencies per document
3. Construct feature vectors manually

### Vocabulary Size:

```
16,940unique words
```

## 9. Train-Test Split

- Stratified 80-20 split
- Training samples: 186
- Testing samples: 47
- Class proportions preserved

## 10. Models Implemented

All models implemented using `sklearn`.

### 10.1 Multinomial Naive Bayes

- Assumes conditional independence
- Struggles with sparse high-dimensional features

### 10.2 Logistic Regression

- Linear classifier
- Optimized with log-loss
- Used `class_weight="balanced"`

### 10.3 Linear Support Vector Machine

- Maximizes margin between classes
- Also used balanced class weights

## 11. Results

| Model | Accuracy | Macro F1 |
| --- | --- | --- |
| Naive Bayes | 0.60 | 0.59 |
| Logistic Regression | **0.83** | **0.80** |
| Linear SVM | 0.81 | 0.78 |

### 11.1 Observations

- **Logistic Regression achieved the best overall performance (82.98%)**
- Linear SVM performed comparably
- Naive Bayes struggled due to:
    - Independence assumption
    - High vocabulary sparsity

Confusion matrix analysis showed:

- Naive Bayes misclassified many Politics articles as Sports
- Logistic Regression achieved balanced precision and recall

## 12. Key Insights

- Linear models handle high-dimensional sparse data effectively
- Class weighting improves performance under imbalance
- Manual Bag-of-Words increases sparsity
- Feature engineering plays a crucial role in text classification

## 13. Limitations

- Small dataset (233 samples)
- Moderate class imbalance
- Large sparse vocabulary
- No stemming or lemmatization
- Web scraping noise possible
- Model may overfit to India-specific vocabulary

## 14. How to Run the Project

### 14.1 Install Dependencies

```bash
pip install pandas numpy scikit-learn requests beautifulsoup4
```

### 14.2 Run Filtering

```bash
python filter_queries.py
```

### 14.3 Run Scraping

```bash
python scrape_articles.py
```

### 14.4 Load and Clean Data

```bash
python load_data.py
```

### 14.5 Train Models

```bash
python train_models.py
```

## 15. Future Improvements

- Add TF-IDF features
- Add n-grams
- Perform stemming / lemmatization
- Hyperparameter tuning
- Cross-validation
- Use deep learning models (LSTM, BERT)

## 16. Conclusion

This project demonstrates a complete NLP classification pipeline, from raw data acquisition to model evaluation.

By implementing preprocessing and Bag-of-Words manually, this project reinforces foundational NLP concepts while achieving competitive performance.

- **Best Model:** Logistic Regression
- **Best Accuracy:** 82.98%
