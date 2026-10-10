from fastapi import FastAPI

app = FastAPI(
    title="Jagrut Netra AI Surveillance System",
    description="API for the Jagrut Netra surveillance project",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "project": "Jagrut Netra AI Surveillance System",
        "status": "running",
        "modules": [
            "Crowd Management",
            "Fire and Smoke Detection",
            "Restricted Area Security",
            "Night-Time Surveillance",
            "Loitering Detection",
        ],
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
