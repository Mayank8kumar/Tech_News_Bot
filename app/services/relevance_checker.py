import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_relevant_news(news_articles):
    """
    Compare news articles to the user's resume vector store and return sorted relevant articles.
    """
    # Load stored resume vector index
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    resume_vector = FAISS.load_local("app/faiss_index", embeddings, allow_dangerous_deserialization=True)

    relevance_scores = []
    for article in news_articles:
        content = f"{article.get('title', '')}\n{article.get('description', '')}"
        docs = resume_vector.similarity_search_with_score(content, k=1)  # Get top 1 match

        if docs:
            score = docs[0][1]  # Second item is the distance
            relevance_scores.append((article, score))
        else:
            relevance_scores.append((article, float("inf")))

    # Sort articles by similarity score (lower = more relevant)
    relevance_scores.sort(key=lambda x: x[1])
    return [item[0] for item in relevance_scores]
