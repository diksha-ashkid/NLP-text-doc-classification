
import pandas as pd
from collections import defaultdict

class DocumentSearch:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def search_keywords(self, keywords):
        results = []
        for keyword in keywords:
            keyword_results = self.df[self.df['Keyword'].str.contains(keyword, case=False, na=False)]
            results.extend(keyword_results.to_dict('records'))
        return results

    def rank_documents(self, results, keywords):
        keyword_counts = defaultdict(int)
        for keyword in keywords:
            for result in results:
                keyword_counts[keyword] += result['Keyword'].lower().count(keyword.lower())#change 'Keyword' to the main text?
        sorted_results = sorted(results, key=lambda x: sum(keyword_counts[key] for key in keywords), reverse=True)##research this
        return sorted_results

    def retrieve_documents(self, keywords):
        search_results = self.search_keywords(keywords)
        ranked_results = self.rank_documents(search_results, keywords)
        return ranked_results


csv_path = 'C:/Users/HP/Downloads/combined_final_dataset.csv'
document_search = DocumentSearch(csv_path)

user_input_keywords = input("Enter keywords (comma-separated): ").split(',')
retrieved_documents = document_search.retrieve_documents(user_input_keywords)

print("Retrieved Documents:")
for i, doc in enumerate(retrieved_documents, start=1):
    print(f"{i}. Title: {doc['Title']}, Category: {doc['main_category']}, Date: {doc['date']}, Description: {doc['description']}")


# In[ ]:




