# 🦙 Llama AI Chatbot

A web-based AI chatbot built with **Django, Python, and Ollama**, powered by the **Llama 3.2 (1B)** language model. This application provides an interactive conversational experience with persistent chat history, allowing users to create new conversations and revisit previous ones.

## 📌 About The Project

Llama AI Chatbot is a conversational web application developed to explore the integration of Large Language Models (LLMs) into Django-based web applications.

The application connects Django with Ollama's local API to process user prompts and generate AI-powered responses using the Llama 3.2 model. It combines a user-friendly chat interface with backend functionality for managing conversations and storing chat history.

## ✨ Features

- **AI-Powered Conversations:** Generate responses using the Llama 3.2 (1B) language model.
- **New Chat:** Start a fresh conversation whenever needed.
- **Chat History:** Access and revisit previous conversations.
- **Persistent Conversations:** Store conversations and messages in the database.
- **Interactive Chat Interface:** Send messages and receive AI-generated responses.
- **Sidebar Navigation:** Easily navigate between previous conversations and create new chats.
- **Responsive Design:** A clean interface designed to work across different screen sizes.
- **Local AI Integration:** Run the language model locally through Ollama.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application framework |
| Ollama | Local LLM integration |
| Llama 3.2 (1B) | Language model |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend interactions |
| SQLite / Configured Database | Conversation and message storage |

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download and install Ollama from:

https://ollama.com/

### 6. Download the Llama Model

Open your terminal and run:

```bash
ollama pull llama3.2:1b
```

Make sure Ollama is running locally.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Start the Django Development Server

```bash
python manage.py runserver
```

### 9. Open the Application

Visit the following URL in your browser:

http://127.0.0.1:8000/

## 💬 How It Works

1. The user opens the chatbot application through the web interface.
2. The user enters a message in the chat input.
3. Django receives the message and communicates with Ollama's local API.
4. Ollama processes the prompt using the Llama 3.2 model.
5. The generated response is returned to Django.
6. The conversation and messages are stored in the database.
7. The response is displayed in the chatbot interface.

## 📂 Project Structure

```text
llama-chatbot/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── chatbot/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│
└── static/
    ├── css/
    ├── js/
    └── ...
```

*Note: The project structure above is illustrative. Adjust it to match your actual folders and files.*

## 🚀 Future Improvements

- Support for multiple AI models.
- Streaming responses for a more interactive experience.
- User authentication and personalized chat sessions.
- Enhanced conversation management.
- Deployment for public access.

## 👩‍💻 Author

Developed as a personal project to explore AI integration, Large Language Models, and full-stack web development.

---

⭐ If you find this project interesting, feel free to explore the repository!