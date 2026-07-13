from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from prompts import prompt


load_dotenv()

embedding_model= HuggingFaceEmbeddings(
     model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.load_local(
    "data/yt_transcripts",
    embeddings=embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever(
    search_kwargs={"k":4}
)

Model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


parser = StrOutputParser()

chain = prompt|Model|parser



def ask_question(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(text.page_content for text in docs)

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )
    return answer



if __name__ == "__main__":
    while True:
        question = input("\nAsk a Question: ")
        if question.lower() == "exit":
            break

        response = ask_question(question)
        print("\nAnswer:\n")
        print(response)