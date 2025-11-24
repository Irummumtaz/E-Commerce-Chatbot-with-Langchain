# E-Commerce Chatbot with Langchain

This project implements an intelligent chatbot for e-commerce platforms, capable of answering customer queries and providing product recommendations based on reviews.

---

## Technologies Used
- **Langchain:** For document retrieval and question answering.  
- **OpenAI:** For generating context-aware responses to customer queries.  
- **AstraDB:** For storing product data and performing similarity-based searches.  
- **Flask:** For creating a simple web interface.  
- **Python:** For the overall implementation.  

---

## Setup

### Clone the repository
```bash
git clone https://github.com/your-username/e-commerce-chatbot-langchain.git
cd e-commerce-chatbot-langchain

---

pip install -r requirements.txt
OPENAI_API_KEY=your-openai-api-key
ASTRA_DB_API_ENDPOINT=your-astra-db-api-endpoint
ASTRA_DB_APPLICATION_TOKEN=your-astra-db-application-token
ASTRA_DB_KEYSPACE=your-astra-db-keyspace

python app.py

---

## Project Structure
.
├── app.py                  # Flask web application
├── ecommbot/
│   ├── data_converter.py   # Data preprocessing and conversion
│   ├── ingestion.py        # Data ingestion and vector storage
│   ├── retrieval_generation.py # Query handling and response generation
│   └── __init__.py         # Package initialization
├── templates/
│   └── chat.html            # HTML template for the chatbot UI
├── .env                    # Environment variables for API keys
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation


