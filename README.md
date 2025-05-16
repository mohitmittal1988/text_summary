# 🦜 TXTSUM: Text Summarizer for YouTube & Websites

TXTSUM is a lightweight Streamlit app that summarizes content from:
- 🎥 **YouTube videos** (via transcript extraction)
- 🌐 **Web articles** (via URL scraping)

It uses **Groq's blazing-fast LLaMA3 model** to summarize the content in natural language using LangChain.

---

## 🚀 Features

- 🎯 One-click summarization of any YouTube video (with captions)
- 🌍 Summarizes any article or website content
- ⚡ Powered by Groq's `llama3-8b-8192` model
- 🧠 LangChain summarization chain
- 🔒 Secure API key input in sidebar

---

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Groq API](https://console.groq.com/)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [Python 3.10+](https://www.python.org/)

---



### 1. Clone the Repository

  ```bash
  git clone https://github.com/mohitmittal1988/text_summary.git
  cd text_summary
  ```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🔐 API Key Requirement

When prompted in the UI, provide your **Groq API Key** to access the `Llama3-8b-8192` LLM.

---

## 📁 Project Structure

```plaintext
├── app.py                     # Main Streamlit application
├── requirement.txt           # Required packages
├── .env                       # Environment token for HuggingFace
└── README.md                  # Documentation
```

---

