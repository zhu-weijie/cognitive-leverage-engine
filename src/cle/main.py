from fastapi import FastAPI

app = FastAPI(
    title="Cognitive Leverage Engine",
    description="An engine to demonstrate AI leverage over traditional certainty-based tasks.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Cognitive Leverage Engine"}
