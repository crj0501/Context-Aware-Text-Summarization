import numpy as np
from sentence_transformers import SentenceTransformer, util

class RetrievalQA:
    def __init__(self, context, model_name="all-MiniLM-L6-v2"):
        self.context = context
        self.model = SentenceTransformer(model_name)
        self.context_embeddings = self.embed_context(context)

    def embed_context(self, context):
        # Break context into chunks
        chunk_size = 500
        chunks = [context[i:i+chunk_size] for i in range(0, len(context), chunk_size)]

        # Encode context chunks
        context_embeddings = self.model.encode(chunks, convert_to_tensor=True)
        return context_embeddings, chunks

    def get_relevant_chunks(self, query):
        # Encode the user's query
        query_embedding = self.model.encode(query, convert_to_tensor=True)

        # Compute similarity between query and context chunks
        similarities = util.pytorch_cos_sim(query_embedding, self.context_embeddings[0])

        # Get the index of the most similar chunk
        most_similar_idx = np.argmax(similarities)

        # Return the most relevant chunk
        return self.context_embeddings[1][most_similar_idx]

    def answer_question(self, query):
        relevant_chunk = self.get_relevant_chunks(query)
        # Here you can pass the relevant_chunk to a model for further QA processing (e.g., GPT, Gemini)
        # For simplicity, we just return the chunk here
        return relevant_chunk
