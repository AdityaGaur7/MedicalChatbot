# Medical Chatbot with LLMs, LangChain, Pinecone, and Flask

An intelligent medical chatbot that leverages Large Language Models (LLMs) and vector embeddings to provide accurate medical information and assistance.

## Overview

This Medical Chatbot is a Retrieval-Augmented Generation (RAG) based application that provides intelligent responses to medical queries by combining the power of Large Language Models with a vector database of medical knowledge. The system processes medical documents, creates embeddings, and uses semantic search to retrieve relevant context before generating accurate, context-aware responses.

## Features

- **🤖 Intelligent Medical Q&A**: Answers medical questions using advanced LLM technology (Google Gemini 2.0 Flash)
- **📚 Knowledge Base from PDFs**: Processes and indexes medical documents from PDF files for accurate information retrieval
- **🔍 Semantic Search**: Uses vector embeddings and similarity search to find the most relevant medical information
- **💬 Interactive Web Interface**: User-friendly chat interface with real-time messaging
- **🚀 RAG Architecture**: Retrieval-Augmented Generation ensures responses are grounded in the provided medical knowledge base
- **☁️ Scalable Vector Storage**: Uses Pinecone for efficient vector database management
- **🔐 Secure API Management**: Environment-based configuration for API keys
- **🐳 Docker Support**: Containerized deployment ready for production
- **☁️ AWS Deployment**: CI/CD pipeline with GitHub Actions for automated AWS deployment

## Project Structure

```
MedicalChatbot/
├── app.py                 # Flask application and main chat endpoint
├── store_index.py         # Script to process PDFs and store embeddings in Pinecone
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this file)
├── data/                 # Medical PDF documents directory
│   └── Medical_book.pdf
├── src/                  # Source code modules
│   ├── helper.py         # PDF loading, text splitting, and embedding functions
│   └── prompt.py         # System prompt template for the LLM
├── templates/            # HTML templates
│   └── chat.html         # Chat interface UI
├── static/               # Static files (CSS, JS)
│   └── style.css         # Styling for the chat interface
└── Dockerfile            # Docker configuration for containerization
```

## How It Works

### Architecture

The chatbot follows a **Retrieval-Augmented Generation (RAG)** architecture:

1. **Document Processing** (`store_index.py`):

   - Loads medical PDF documents from the `data/` directory
   - Splits documents into smaller chunks (500 characters with 20 character overlap)
   - Generates embeddings using HuggingFace's `sentence-transformers/all-MiniLM-L6-v2` model (384 dimensions)
   - Stores embeddings in Pinecone vector database for fast similarity search

2. **Query Processing** (`app.py`):

   - User submits a medical question through the web interface
   - System converts the query into an embedding vector
   - Performs similarity search in Pinecone to retrieve top 3 most relevant document chunks
   - Passes the retrieved context and user query to Google Gemini 2.0 Flash LLM
   - LLM generates a concise, context-aware response (max 3 sentences)

3. **Response Generation**:
   - The system prompt instructs the LLM to use retrieved context
   - If information is not available, the bot explicitly states it doesn't know
   - Responses are kept concise and medically informative

### Technology Flow

```
User Query → Embedding → Pinecone Vector Search → Context Retrieval →
LLM (Gemini 2.0 Flash) → Context-Aware Response → User Interface
```

### Key Components

- **LangChain**: Orchestrates the RAG pipeline, connecting retrieval and generation
- **Pinecone**: Vector database storing document embeddings for semantic search
- **HuggingFace Embeddings**: Converts text to 384-dimensional vectors
- **Google Gemini 2.0 Flash**: Generates natural language responses
- **Flask**: Web framework serving the chat interface
- **PyPDF**: Extracts text from medical PDF documents

## Tech Stack

- **Python 3.10** - Programming language
- **LangChain** - Framework for building LLM applications and RAG pipelines
- **Flask** - Lightweight web framework for the chat interface
- **Google Gemini 2.0 Flash** - Large Language Model for response generation
- **Pinecone** - Managed vector database for storing and searching embeddings
- **HuggingFace Sentence Transformers** - Embedding model for text vectorization
- **PyPDF** - PDF document processing library

## Local Setup and Installation

### Prerequisites

- Python 3.10 or higher
- Conda (recommended for environment management)
- Google API key (for Gemini 2.0 Flash)
- Pinecone API key

### Installation Steps

1. Clone the repository

```bash
git clone https://github.com/AdityaGaur7/MedicalChatbot.git
cd MedicalChatbot
```

2. Create and activate a conda environment

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables
   Create a `.env` file in the root directory with your API credentials:

```ini
PINECONE_API_KEY = "your_pinecone_api_key"
GOOGLE_API_KEY = "your_google_api_key"
```

**Note**: You can also use `OPENAI_API_KEY` if you prefer to use OpenAI models (modify `app.py` accordingly).

### Running the Application

1. Initialize the vector database with embeddings:

```bash
python store_index.py
```

2. Start the Flask application:

```bash
python app.py
```

3. Access the chatbot interface by opening your browser and navigating to:

```
http://localhost:8080
```

**Note**: The application runs on port 8080 by default (as configured in `app.py`).

## AWS Deployment with GitHub Actions

This section describes how to deploy the Medical Chatbot to AWS using GitHub Actions for CI/CD.

### Prerequisites

- AWS Account
- GitHub Account
- Basic understanding of AWS services (EC2, ECR)

### Deployment Steps

1. **Create IAM User**

   - Create a new IAM user with the following permissions:
     - `AmazonEC2ContainerRegistryFullAccess`
     - `AmazonEC2FullAccess`

2. **Set Up Amazon ECR**

   - Create a new Elastic Container Registry (ECR) repository
   - Note the repository URI for later use

3. **Launch EC2 Instance**

   - Create an Ubuntu EC2 instance
   - Install Docker:
     ```bash
     sudo apt-get update -y
     curl -fsSL https://get.docker.com -o get-docker.sh
     sudo sh get-docker.sh
     sudo usermod -aG docker ubuntu
     newgrp docker
     ```

4. **Configure GitHub Actions**

   a. Set up EC2 as a self-hosted runner:

   - Go to Repository Settings > Actions > Runners
   - Click "New self-hosted runner"
   - Follow the setup instructions for your OS

   b. Configure GitHub Secrets:
   Add the following secrets to your repository:

   ```
   AWS_ACCESS_KEY_ID
   AWS_SECRET_ACCESS_KEY
   AWS_DEFAULT_REGION
   ECR_REPO
   PINECONE_API_KEY
   GOOGLE_API_KEY
   ```

   **Note**: If using OpenAI instead, use `OPENAI_API_KEY` instead of `GOOGLE_API_KEY`.

### Deployment Process

The GitHub Actions workflow will:

1. Build the Docker image
2. Push the image to ECR
3. Pull and run the image on the EC2 instance

For detailed deployment logs and status, check the Actions tab in your GitHub repository.

## Important Disclaimer

⚠️ **Medical Disclaimer**: This chatbot is designed for informational purposes only. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read or received from this chatbot.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See the [LICENSE](LICENSE) file for details.
