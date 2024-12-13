from transformers import pipeline
from typing import Dict, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize summarization pipeline with fixed parameters
try:
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn",
        truncation=True,
    )
except Exception as e:
    logger.error(f"Error initializing pipeline: {str(e)}")
    raise

def chunk_text(text: str, max_chunk_length: int = 500) -> list:
    """Split text into smaller chunks"""
    sentences = text.split('.')
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        sentence = sentence.strip() + '.'
        sentence_length = len(sentence.split())
        
        if current_length + sentence_length > max_chunk_length:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_length = sentence_length
        else:
            current_chunk.append(sentence)
            current_length += sentence_length
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

async def generate_summary(text: str, max_length: int = 4000) -> Dict[str, Any]:
    """Generate summary using HuggingFace model"""
    try:
        logger.info("Starting summary generation...")
        
        # Split text into smaller chunks
        chunks = chunk_text(text)
        
        # Generate summaries for each chunk
        summaries = []
        for chunk in chunks:
            if not chunk.strip():
                continue
                
            try:
                # Calculate dynamic lengths based on input
                input_length = len(chunk.split())
                max_output_length = max(min(input_length // 2, 100), 50)
                min_output_length = min(max_output_length - 20, 30)
                
                summary = summarizer(
                    chunk,
                    max_length=max_output_length,
                    min_length=min_output_length,
                    do_sample=False,
                    early_stopping=True
                )
                
                if summary and len(summary) > 0:
                    summaries.append(summary[0]['summary_text'])
            except Exception as e:
                logger.error(f"Error summarizing chunk: {str(e)}")
                continue
        
        if not summaries:
            raise Exception("Failed to generate any summary")
            
        final_summary = " ".join(summaries)
        
        return {
            "summary": final_summary,
            "token_count": len(text.split()),
            "success": True
        }
    except Exception as e:
        logger.error(f"Error in summary generation: {str(e)}")
        return {
            "summary": "",
            "token_count": 0,
            "success": False,
            "error": str(e)
        }

def get_token_count(text: str) -> int:
    """Count tokens in text"""
    return len(text.split())