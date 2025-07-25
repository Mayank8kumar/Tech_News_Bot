import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO)

project_name = "tech_relevance_ai"

list_of_file = [
    f"app/main.py",
    
    f"app/routers/__init__.py",
    f"app/routers/upload.py",
    f"app/routers/fetch_news.py",
    f"app/routers/ask_bot.py",
    
    f"app/services/__init__.py",
    f"app/services/embedding_service.py",
    f"app/services/vector_store.py",
    f"app/services/llm_chain.py",
    f"app/services/domain_classifier.py",
    f"app/services/trend_analyzer.py",
    
    f"app/utils/__init__.py",
    f"app/utils/extract_text.py",
    f"app/utils/scheduler.py",

    f"app/faiss_index/.gitkeep",  # placeholder so the directory is tracked

    ".env",
    "requirements.txt",
    "README.md",
]


for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")

