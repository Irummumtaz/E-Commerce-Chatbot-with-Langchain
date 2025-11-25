# E-Commerce Chatbot with Langchain

This project implements an intelligent **chatbot for e-commerce platforms**, capable of answering customer queries and providing product recommendations based on reviews.

---

## 🛠 Technologies Used

- **Langchain:** For document retrieval and question answering.
- **OpenAI:** For generating context-aware responses to customer queries.
- **AstraDB:** For storing product data and performing similarity-based searches.
- **Flask:** For creating a simple web interface.
- **Python:** Overall implementation.

---

## ⚡ Features

- **Product Recommendation:** Suggests products based on customer queries and reviews.
- **Real-Time Query Handling:** Customers get instant responses using a state-of-the-art NLP model (OpenAI).
- **Search & Retrieval:** Performs similarity search on product reviews stored in AstraDB to find the most relevant information.

---

## 📂 Project Structure


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


---

## 🚀 Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/e-commerce-chatbot-langchain.git
cd e-commerce-chatbot-langchain

2. **Install dependencies:**
pip install -r requirements.txt

3. **Set up environment variables:**

Create a .env file with the following variables:
OPENAI_API_KEY=your-openai-api-key
ASTRA_DB_API_ENDPOINT=your-astra-db-api-endpoint
ASTRA_DB_APPLICATION_TOKEN=your-astra-db-application-token
ASTRA_DB_KEYSPACE=your-astra-db-keyspace

python app.py

---


CSV Product Reviews
        │
        ▼
  ┌────────────────────┐
  │   Data Converter    │
  │ - Reads product_title & review
  │ - Creates Langchain Document objects
  └────────────────────┘
        │
        ▼
  ┌────────────────────┐
  │ AstraDB Vector Store│
  │ - Stores Document embeddings
  │ - Enables similarity search
  └────────────────────┘
        │
        ▼
  ┌─────────────┐
  │  User Query │
  │ - Customer asks a question
  └─────────────┘
        │
        ▼
  ┌─────────────┐
  │ Retriever   │
  │ - Fetches top-k relevant reviews
  └─────────────┘
        │
        ▼
  ┌────────────────────┐
  │ OpenAI Chat Model  │
  │ - Generates context-aware response
  │ - Concise, relevant answers
  └────────────────────┘
        │
        ▼
  ┌─────────────┐
  │ Response to │
  │    User     │
  └─────────────┘


🔹 Step-by-Step Explanation

Data Preparation:
Convert CSV product reviews into Langchain Document objects with product metadata using data_converter.py.

Vector Storage:
Embed documents using OpenAI embeddings and store them in AstraDB for fast similarity search.

Query Retrieval:
Retrieve relevant reviews from AstraDB when a customer asks a question.

Response Generation:
Pass retrieved reviews to OpenAI Chat model for context-aware responses.

User Interaction:
Return responses through the Flask web interface for real-time interaction.



