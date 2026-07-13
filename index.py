from ingest import load_yt
 
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_text_splitters import RecursiveCharacterTextSplitter

def vector_store():
    docs = load_yt()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks= splitter.split_text(docs)

    embedding_model=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_storing = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )
    vector_storing.save_local("data/yt_transcripts")
    return vector_storing

if __name__ == "__main__":
    vector_store()