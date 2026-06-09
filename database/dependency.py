from langchain_openrouter import ChatOpenRouter
from sentence_transformers import SentenceTransformer
from core.config import settings

api_key = settings.OPENROUTERAPIKEY

_emb_model = None

def get_llm():
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is not configured")
    try:
        return ChatOpenRouter(model="openrouter/owl-alpha" , api_key=api_key)
    except Exception as exc:
        try:
            return ChatOpenRouter(model="poolside/laguna-xs.2:free", api_key=api_key)
        except Exception as exc2:
            raise RuntimeError("Failed to initialize model") from exc2
        
def get_emb_model() -> SentenceTransformer:
    global _emb_model
    if _emb_model is not None :
        return _emb_model
    try:
        _emb_model = SentenceTransformer("all-MiniLM-L6-v2")
        return _emb_model
    except:
        raise RuntimeError("Failed to initialize embedding model")

