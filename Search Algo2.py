from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class VectorSpaceModel:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.document_vectors = self.vectorizer.fit_transform(self.df['text_column'])  # Replace 'text_column' with the column containing document text

    def retrieve_documents(self, query):
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, self.document_vectors).flatten()
        document_scores = list(enumerate(cosine_similarities))
        ranked_documents = sorted(document_scores, key=lambda x: x[1], reverse=True)

        return ranked_documents

# Example usage
csv_path = 'your_dataset.csv'  # Replace with your dataset path
vsm = VectorSpaceModel(csv_path)

user_query = input("Enter your query: ")
retrieved_docs = vsm.retrieve_documents(user_query)

print("Top 5 Retrieved Documents:")
for idx, score in retrieved_docs[:5]:  # Display top 5 retrieved documents
    print(f"Document ID: {idx}, Similarity Score: {score}, Text: {vsm.df.iloc[idx]['text_column']}")
