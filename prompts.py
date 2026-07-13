from langchain_core.prompts import PromptTemplate


prompt =PromptTemplate.from_template(
    """
You are an expert content analysing assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, reply:

"I couldn't find that information in the youtube transcript."

Context:
{context}

Question:
{question}

Answer:
"""
)
