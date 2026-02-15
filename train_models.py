from load_data import load_data
from preprocess import clean_text
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
from collections import Counter
import numpy as np

def build_vocabulary(tokenized_texts):
    #builds vocabulary dictionary:
    #word → index

    vocab = {}
    index = 0

    for tokens in tokenized_texts:
        for word in tokens:
            if word not in vocab:
                vocab[word] = index
                index += 1

    return vocab

def vectorize_bow(tokenized_texts, vocab):
    #converts tokenized documents into bag-of-words vectors
    #returns numpy matrix

    num_docs = len(tokenized_texts)
    vocab_size = len(vocab)

    X = np.zeros((num_docs, vocab_size))

    for i, tokens in enumerate(tokenized_texts):

        word_counts = Counter(tokens)

        for word, count in word_counts.items():
            if word in vocab:
                X[i][vocab[word]] = count

    return X

def main():

    # 1. load dataset
    df = load_data("indian_news_with_text.csv")

    print("Total samples:", len(df))

    print("\nClass distribution:")
    print(df["category"].value_counts())

    # 2. preprocess text (manual tokenization + stopword removal)
    tokenized_texts = df["text"].apply(clean_text)

    # 3. build vocabulary (manual BoW)
    vocab = build_vocabulary(tokenized_texts)
    print("\nVocabulary size:", len(vocab))

    X_features = vectorize_bow(tokenized_texts, vocab)

    y = df["category"]

    # 4. train-test split (stratified)
    X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size=0.2, random_state=42, stratify=y)

    # 5. define models
    models = {
        "Naive Bayes": MultinomialNB(),
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced"),
        "Linear SVM": LinearSVC(class_weight="balanced", max_iter= 5000) #had to fix iterations from here because of following error:
        #base.py:1250: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.
    }

    # 6. train and evaluate
    for name, model in models.items():

        print("\n==============================")
        print("Model:", name)

        # train
        model.fit(X_train, y_train)

        # predict
        y_pred = model.predict(X_test)

        # accuracy
        acc = accuracy_score(y_test, y_pred)
        print("Accuracy:", round(acc, 4))

        # confusion matrix
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        # detailed metrics
        print("Classification Report:")
        print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    main()
