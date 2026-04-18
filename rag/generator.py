import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from rag.retriever import get_retriever

load_dotenv()


def get_qa_chain():
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )

    retriever = get_retriever()

    prompt = PromptTemplate.from_template(
        """
        You are a DBMS expert assistant helping students.

        Use ONLY the provided context to answer the question.
        If the answer is not in the context, say "I don't know".

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

    output_parser = StrOutputParser()

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    def qa_pipeline(query):
        docs = retriever.invoke(query)
        context = format_docs(docs)

        final_prompt = prompt.invoke({
            "context": context,
            "question": query
        })

        response = llm.invoke(final_prompt)

        return {
            "answer": output_parser.invoke(response),
            "sources": [doc.metadata.get("source", "unknown") for doc in docs]
        }

    return qa_pipeline


if __name__ == "__main__":
    qa = get_qa_chain()

    while True:
        query = input("\nAsk a DBMS question (or 'exit'): ")

        if query.lower() == "exit":
            break

        result = qa(query)

        print("\n🧠 Answer:\n")
        print(result["answer"])

        print("\n📚 Sources:\n")
        for src in result["sources"]:
            print(src)