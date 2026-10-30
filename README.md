# College Assistant Chatbot using LangChain

## Project Description
This project is a College Assistant Chatbot developed using LangChain and Ollama. It helps students get simple answers to common college-related questions.

## Objectives
- Understand the basics of LangChain.
- Create reusable Prompt Templates.
- Connect LangChain with the Ollama LLM.
- Build a chatbot using chains.
- Store chatbot queries and responses in CSV files.

## Technologies Used
- Python
- LangChain
- Ollama
- Llama 3.2
- Pandas
- VS Code

## Chatbot Categories
1. General
2. Admission
3. Library
4. Examination
5. Fees

## Additional Chains
- Summarization Chain
- Question Answering Chain

## Project Structure
```text
LangChain_Basics/
├── dataset/
│   ├── prompts.csv
│   ├── user_queries.csv
│   ├── chatbot_responses.csv
│   └── chain_results.csv
├── notebook/
│   └── Week10_LangChain_Basics.ipynb
├── langchain_chatbot.py
├── requirements.txt
└── README.md
```

## Execution
Run the chatbot using Python:

```bash
python langchain_chatbot.py
```

## Result
The College Assistant Chatbot successfully generates responses for different college-related categories. User queries and chatbot responses are saved in CSV files.

## Conclusion
This project demonstrates how LangChain Prompt Templates and Chains can be used with a local Ollama language model to develop a simple chatbot application.
