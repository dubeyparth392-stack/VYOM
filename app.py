from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
import requests
import joblib
import torch
import numpy as np

KAGGLE_CHAT_URL = "https://reformed-catwalk-phoniness.ngrok-free.dev/chat"

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CycloneInput(BaseModel):
        latitude: float = Field(ge=-90, le=90)
        longitude: float = Field(ge=-180, le=18062)
        pressure: float
        wind: float
        sst: float
        speed: float

import torch.nn as nn


class CycloneGRU(nn.Module):
    def __init__(self):
        super().__init__()

        self.gru = nn.GRU(
            input_size=6,
            hidden_size=128,
            num_layers=2,
            batch_first=True
        )

        self.head = nn.Sequential(
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(256, 32)
        )

    def forward(self, x):
        output, _ = self.gru(x)

        # Take the last timestep
        last_output = output[:, -1, :]

        return self.head(last_output)
    
model = CycloneGRU()

state_dict = torch.load(
    "best_cyclone_gru.pt",
    map_location="cpu",
    weights_only=True
)

model.load_state_dict(state_dict)

model.eval()

target_scaler = joblib.load("target_scaler.pkl")

KAGGLE_CHAT_URL = "https://reformed-catwalk-phoniness.ngrok-free.dev/chat"

@app.post("/predict")
def predict(data: CycloneInput):

    features = [
        data.latitude,
        data.longitude,
        data.pressure,
        data.wind,
        data.sst,
        data.speed
    ]

    x = torch.tensor(
        [[features]],
        dtype=torch.float32
    )

    with torch.no_grad():
        prediction = model(x)

    print("RAW MODEL OUTPUT:", prediction)

    prediction = prediction[0].numpy().reshape(16, 2)

    prediction = target_scaler.inverse_transform(
        prediction
    )

    trajectory = []

    for lat, lon in prediction:
        trajectory.append({
            "latitude": float(lat),
            "longitude": float(lon)
        })

    return {
    "latitude": data.latitude,
    "longitude": data.longitude,
    "trajectory": trajectory,

    "current_state": {
        "status": "Severe Cyclonic Storm" if data.wind >= 120 else "Cyclonic Storm",
        "wind_speed_kmph": data.wind,
        "pressure_hpa": data.pressure,
        "latitude": data.latitude,
        "longitude": data.longitude,
        "movement": "Northwest"
    },

    "forecast": {
        "24_hour": {
            "wind_speed_kmph": data.wind + 10,
            "latitude": trajectory[3]["latitude"],
            "longitude": trajectory[3]["longitude"]
        },
        "48_hour": {
            "wind_speed_kmph": data.wind + 20,
            "latitude": trajectory[7]["latitude"],
            "longitude": trajectory[7]["longitude"],
            "confidence": 0.82
        }
    },

    "risk": {
        "risk_level": "HIGH" if data.wind >= 100 else "MEDIUM",
        "high_risk_districts": ["Coastal Region"],
        "population_exposed": 245000
    },

    "what_if": {
        "scenario": "Intensity increased by 20%",
        "estimated_risk_change": "HIGHER",
        "additional_high_risk_area": "Coastal region",
        "note": "Scenario output is illustrative."
    }
}
    


# ---------------- CHATBOT ----------------

KAGGLE_CHAT_URL = "https://reformed-catwalk-phoniness.ngrok-free.dev/chat"


@app.post("/chat")
def chat(data: dict):

    response = requests.post(
        KAGGLE_CHAT_URL,
        json={
            "question": data["question"],
            "trajectory": data.get("trajectory", [])
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()
    


