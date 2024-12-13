from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging
from app.utils import generate_summary
from app.config import API_TITLE, API_DESCRIPTION, API_VERSION, MAX_TOKEN_LENGTH
from fastapi.middleware.cors import CORSMiddleware

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DocumentRequest(BaseModel):
    text: str
    max_length: Optional[int] = MAX_TOKEN_LENGTH

@app.get("/")
async def root():
    return {"message": "Welcome to Document Summarizer API"}

@app.post("/summarize/")
async def summarize_document(request: DocumentRequest):
    try:
        if not request.text:
            raise HTTPException(status_code=400, detail="No text provided")
        
        result = await generate_summary(request.text, request.max_length)
        
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result.get('error'))
        
        return result
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))