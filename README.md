# Blog Project Agentic

An AI blog generator built with LangGraph, LangChain, Groq, and Streamlit.

## Workflow

1. The user enters a blog topic in the Streamlit interface.
2. The topic is sent to the LangGraph topic workflow.
3. The `title_creation` node asks the Groq model to create an SEO-friendly title.
4. The `content_generation` node uses the topic and title to generate the blog content in Markdown.
5. The generated title and content are displayed in the Streamlit UI.
6. The result can be downloaded as a Markdown file.

## Requirements

- Python 3.13 or newer
- A Groq API key
- Optional: a LangSmith API key for tracing

## Setup

Open PowerShell in the project directory and create the virtual environment:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create or update `.env` in the project root:

```env
GROQ_API_KEY=your_real_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

The LangSmith key is optional. Never commit `.env` or share its contents.

## Run The Streamlit UI

Streamlit is the primary user interface for this project:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run streamlit_app.py
```

Open the URL shown in the terminal, normally:

http://localhost:8501

Enter a topic and select **Generate blog**.

## Project Structure

```text
streamlit_app.py          Streamlit user interface
src/graphs/               LangGraph workflow construction
src/nodes/                Title and blog content generation nodes
src/llms/                 Groq model configuration
src/states/               Blog state and data models
.env                      Local API keys, ignored by Git
```

## Troubleshooting

- If credentials are changed while a server is running, stop it with `Ctrl+C` and start it again.
- If generation fails with a model error, verify that the configured Groq account has access to the model in `src/llms/groqllm.py`.
