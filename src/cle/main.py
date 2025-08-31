from fastapi import FastAPI
from cle.api.endpoints import health, simulators

app = FastAPI(
    title="Cognitive Leverage Engine",
    description="An engine to demonstrate AI leverage over traditional certainty-based tasks.",
    version="0.1.0",
)


app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])
app.include_router(simulators.router, prefix="/api/v1/simulators", tags=["Simulators"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Cognitive Leverage Engine"}
