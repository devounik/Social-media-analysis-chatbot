import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    # Configuration variables loaded from environment variables
    BASE_API_URL = os.getenv("BASE_API_URL", "")
    LANGFLOW_ID = os.getenv("LANGFLOW_ID", "")
    FLOW_ID = os.getenv("FLOW_ID", "")
    APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN", "")
    ENDPOINT = os.getenv("ENDPOINT", "")

# Tweaks dictionary for specific components
    TWEAKS = {
    "ChatInput-Ay49P": {},
    "Prompt-uIPjZ": {},
    "SplitText-P54TF": {},
    "ChatOutput-07hvn": {},
    "AstraDB-d3c2e": {},
    "AstraDB-eGQEx": {},
    "HuggingFaceInferenceAPIEmbeddings-3A3E8": {},
    "HuggingFaceInferenceAPIEmbeddings-nSUmm": {},
    "ParseData-lQjna": {},
    "File-vlhYD": {},
    "GroqModel-lK7Po": {},
    "HuggingFaceModel-4bDG8": {}
}
