# Document Summarizer 📄

A powerful document summarization application that leverages Large Language Models to create concise summaries of long texts. Built with FastAPI, Streamlit, and HuggingFace Transformers.

> ![image](https://github.com/user-attachments/assets/a384ffb3-2282-470f-8055-e00e19bd7068)


> ![image](https://github.com/user-attachments/assets/5e35a92f-3535-47fc-8f03-354667af0a0d)

## 🌟 Features

- **Smart Text Summarization**: Efficiently summarizes long documents while preserving key information
- **User-friendly Interface**: Clean and intuitive Streamlit frontend
- **RESTful API**: Robust FastAPI backend with proper error handling
- **Chunk Processing**: Handles long documents by intelligently splitting them into manageable chunks
- **Real-time Status**: Live feedback on API status and processing steps

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **ML Model**: HuggingFace Transformers (BART-large-CNN)
- **Additional Libraries**: 
  - transformers
  - torch
  - python-dotenv
  - uvicorn

## 📦 Installation

**1. Clone the repository**
```bash
git clone https://sureshravuris/doc-summarizer.git
cd doc-summarizer
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

**3. Install dependencies**
```bash
pip install fastapi streamlit transformers torch python-dotenv uvicorn
```

## 🚀 Running the Application

**1. Start the FastAPI backend:**
```bash
uvicorn main:app --reload --port 8000
```

**2. In a new terminal, start the Streamlit frontend:**
```bash
streamlit run frontend/streamlit_app.py
```

**3. Open your browser and navigate to:**

- Frontend: http://localhost:8501
- API Documentation: http://localhost:8000/docs


## 📁 Project Structure
```bash
doc-summarizer/
├── app/
│   ├── __init__.py
│   ├── config.py      # Configuration settings
│   └── utils.py       # Utility functions and ML model
├── frontend/
│   └── streamlit_app.py  # Streamlit interface
├── main.py            # FastAPI application
└── README.md
```


## 💡 Usage

Access the application through your web browser
Paste your text into the input area
Click "Summarize"
View the generated summary along with token count

## 🔧 API Endpoints

- GET /: Health check endpoint
- POST /summarize/: Text summarization endpoint

- Request body: {"text": "your text here"}
- Returns: Summary and token count



## ⚙️ Configuration
The application uses the following configurable parameters:

- Maximum token length: 4000
- Dynamic chunk sizing for long texts
- Adjustable summarization parameters

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
## 🙏 Acknowledgements

- HuggingFace Transformers
- FastAPI
- Streamlit





