#!/usr/bin/env python
import sys
import warnings
import os
import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#from langtrace_python_sdk import langtrace # Must precede any llm module imports
#langtrace.init(api_key = os.environ['LANGTRACE_API_KEY'])
from crew import SqlAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(query):
    """
    Run the crew.
    """
    inputs = {
    "query": query
    }
    
    dick = SqlAgent().setdb("azure")
    result=dick.crew().kickoff(inputs=inputs)
    return result

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        SqlAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SqlAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        SqlAgent().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
#result = run()
#print(result)
def temp_func(query:str):
    pass
@app.get("/")
async def hello():
    
    return {"message":"working"}
@app.post("/sent_query/{query}")
async def send_notification(query:str):
    _ = run(query=query)
    file_path = './report.md'
    if os.path.exists(file_path):
        return FileResponse(
            file_path,
            media_type="text/markdown",
            filename="report.md"
        )
    else:
        return {"error": "File not found"}
if __name__ =="__main__":
    run("list all the tables")