from fastapi import FastAPI


app = FastAPI(
    title="InterviewAI Backend",
    description="AI powered interview preparation platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to InterviewAI Backend 🚀"
    }