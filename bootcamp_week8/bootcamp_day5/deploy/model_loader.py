from llama_cpp import Llama
from deploy.config import MODEL_PATH, MODEL_CONFIG

_llm = None

def get_model():
    global _llm
    if _llm is None:
        _llm = Llama(
            model_path=MODEL_PATH,
            n_ctx=MODEL_CONFIG["n_ctx"],
            n_threads=MODEL_CONFIG["n_threads"],
        )
    return _llm
