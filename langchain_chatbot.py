
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pandas as pd
import os

# Connect Ollama model
llm = OllamaLLM(model="llama3.2")
parser = StrOutputParser()

# Five Prompt Templates
prompts = {
    "general": PromptTemplate.from_template(
        "You are a helpful college assistant. Answer simply: {question}"
    ),
    "admission": PromptTemplate.from_template(
        "You are a college admission assistant. Answer this question: {question}"
    ),
    "library": PromptTemplate.from_template(
        "You are a library assistant. Answer this question: {question}"
    ),
    "examination": PromptTemplate.from_template(
        "You are an examination assistant. Answer this question: {question}"
    ),
    "fees": PromptTemplate.from_template(
        "You are a college fees assistant. Answer this question: {question}"
    )
}

# Chatbot Chain
general_chain = prompts["general"] | llm | parser

# Summarization Chain
summary_prompt = PromptTemplate.from_template(
    "Summarize the following text in simple words: {text}"
)
summary_chain = summary_prompt | llm | parser

# Question Answering Chain
qa_prompt = PromptTemplate.from_template(
    "Answer the question based on the context.\n"
    "Context: {context}\n"
    "Question: {question}"
)
qa_chain = qa_prompt | llm | parser

# Store chatbot data
os.makedirs("dataset", exist_ok=True)

queries = []
responses = []
chain_results = []

print("COLLEGE ASSISTANT CHATBOT")
print("Type exit to stop")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    print("\nChoose a category:")
    print("1. General")
    print("2. Admission")
    print("3. Library")
    print("4. Examination")
    print("5. Fees")

    choice = input("Enter choice: ")

    categories = {
        "1": "general",
        "2": "admission",
        "3": "library",
        "4": "examination",
        "5": "fees"
    }

    category = categories.get(choice, "general")
    chain = prompts[category] | llm | parser

    response = chain.invoke({"question": question})

    print("\nBot:", response)

    queries.append(question)
    responses.append(response)
    chain_results.append(category)

# Save results into CSV files
pd.DataFrame({
    "User Query": queries
}).to_csv("dataset/user_queries.csv", index=False)

pd.DataFrame({
    "User Query": queries,
    "Response": responses
}).to_csv("dataset/chatbot_responses.csv", index=False)

pd.DataFrame({
    "User Query": queries,
    "Chain": chain_results,
    "Response": responses
}).to_csv("dataset/chain_results.csv", index=False)

print("\nChat history saved successfully!")
