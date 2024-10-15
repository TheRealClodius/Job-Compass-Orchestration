import os
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from .env

def hello():
    return "Hello, Job Compass Orchestration!"

def get_api_key(key_name):
    return os.getenv(key_name)

if __name__ == "__main__":
    print(hello())
    print(f"API Key 1: {get_api_key('API_KEY_1')}")
    print(f"API Key 2: {get_api_key('API_KEY_2')}")