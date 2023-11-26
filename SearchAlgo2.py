from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class KeywordBasedSearch:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.document_vectors = self.vectorizer.fit_transform(self.df['description'])  # Replace 'text_column' with the column containing document text

    def search_documents(self, keywords):
        keyword_vector = self.vectorizer.transform([' '.join(keywords)])
        keyword_scores = keyword_vector.toarray()[0]

        document_scores = self.document_vectors.dot(keyword_scores)
        ranked_documents = sorted(enumerate(document_scores), key=lambda x: x[1], reverse=True)

        return ranked_documents

# Example usage
csv_path = 'your_dataset.csv'  # Replace with your dataset path
search_engine = KeywordBasedSearch(csv_path)

user_keywords = input("Enter keywords (comma-separated): ").split(',')
retrieved_docs = search_engine.search_documents(user_keywords)

print("Top 5 Retrieved Documents:")
for idx, score in retrieved_docs[:5]:  # Display top 5 retrieved documents
    print(f"Document ID: {idx}, Similarity Score: {score}, Text: {search_engine.df.iloc[idx]['title']}")
