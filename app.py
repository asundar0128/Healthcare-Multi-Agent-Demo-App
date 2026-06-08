from fastapi import FastAPI
from data.patients import PATIENTS
from agents.leader import leader_route

app = FastAPI(
    title="Healthcare Leader Agent API",
    description="Single FastAPI endpoint routing role-based requests to healthcare agents."
)


@app.get("/")
def home():
    return {
        "message": "Healthcare Leader Agent API is running"
    }


@app.get("/patients")
def get_patients():
    return PATIENTS


@app.get("/invoke")
def invoke(
    role: str,
    patient_id: str | None = None
):
    return leader_route(
        role=role,
        patient_id=patient_id
    )
