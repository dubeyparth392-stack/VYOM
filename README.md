🌪️ VYOM — Intelligent Disaster Prediction & Response System

VYOM is an AI-powered disaster prediction and decision-support system developed as part of the Smart India Hackathon (SIH). The platform aims to assist in disaster preparedness and response by predicting disaster trajectories, estimating potential losses, and providing an interactive AI agent to help users understand predictions and their implications.

By combining machine learning models with a conversational AI agent, VYOM aims to transform complex prediction outputs into actionable insights for disaster management.

🚀 Key Features

* Trajectory Prediction: Predicts the potential trajectory of a disaster using relevant environmental and atmospheric parameters.
* Loss Estimation: Supports the assessment of potential loss of life and capital to inform disaster preparedness and response.
* AI-Powered Assistant: Integrates the VYOM conversational agent to answer questions and provide contextual explanations.
* Interactive Frontend Integration: Connects prediction models and the conversational agent to the frontend through API endpoints.
* Real-Time Visualization: Enables predicted trajectory coordinates to be returned to the frontend for visualization.
* Context-Aware Responses: Allows the conversational agent to use trajectory prediction context when generating responses.

🧠 System Architecture

VYOM combines a prediction pipeline with a conversational AI pipeline.

1. Trajectory Prediction Pipeline

The frontend collects the required input parameters and sends them to the FastAPI backend.

The backend processes the request, invokes the trajectory prediction model, and returns the predicted trajectory coordinates to the frontend for visualization.

Workflow:

Frontend → FastAPI (/predict) → Trajectory Prediction Model → Predicted Coordinates → Frontend Visualization

2. Conversational AI Pipeline

The conversational AI pipeline enables users to interact with the VYOM agent and ask questions about predictions.

The backend routes chat requests to the agent service, which uses a Gemma-based language model and relevant trajectory context to generate responses.

Workflow:

Frontend → FastAPI (/chat) → Agent Service → Gemma LLM → Contextual Response → Frontend

Architecture Overview

                    ┌──────────────────────┐
                    │      Frontend        │
                    │  User Input & Maps   │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  │                         │
                  ▼                         ▼
        ┌──────────────────┐     ┌──────────────────┐
        │  FastAPI Backend │     │  Chat Interface  │
        │    /predict      │     │     /chat        │
        └────────┬─────────┘     └────────┬─────────┘
                 │                        │
                 ▼                        ▼
        ┌──────────────────┐     ┌──────────────────┐
        │ Trajectory Model │     │   VYOM Agent     │
        │                  │     │   Gemma LLM      │
        └────────┬─────────┘     └────────┬─────────┘
                 │                        │
                 ▼                        ▼
        ┌──────────────────┐     ┌──────────────────┐
        │ Predicted        │     │ Contextual AI    │
        │ Trajectory       │     │ Response         │
        └────────┬─────────┘     └────────┬─────────┘
                 │                        │
                 └────────────┬───────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Frontend Output      │
                    │ Visualization & Chat │
                    └──────────────────────┘

🛠️ Technology Stack

Component	Technology
Backend API	Python, FastAPI
Trajectory Prediction	Machine Learning
Conversational AI	Gemma-based LLM
API Communication	REST APIs, JSON
Frontend Integration	HTTP requests and API endpoints
Model Serving & Testing	Local services, API testing, ngrok-based tunnelling during development

👨‍💻 My Contributions

Role: Machine Learning Model Deployment & AI Agent Integration

My primary responsibility was making the machine learning model and conversational AI agent accessible to the frontend through a working backend integration.

1. Machine Learning Model Deployment

* Integrated the trajectory prediction model with a FastAPI backend.
* Developed and worked with the /predict endpoint to accept environmental parameters and return trajectory predictions.
* Handled structured inputs, model invocation, and prediction responses.
* Enabled the frontend to consume predicted trajectory coordinates for visualization.

2. AI Agent Integration

* Worked on integrating the VYOM conversational agent with the application.
* Connected the /chat endpoint to the agent service.
* Integrated the Gemma-based language model into the conversational workflow.
* Worked on passing trajectory prediction context to the agent to support context-aware responses.

3. Frontend–Backend Communication

* Established API communication between the frontend and backend using HTTP requests and JSON payloads.
* Worked on routing prediction and chat requests to their respective services.
* Helped connect the model outputs and AI-generated responses to the frontend interface.

4. Model Serving & Deployment Workflow

* Worked with FastAPI and local model-serving environments to expose inference functionality through APIs.
* Used ngrok-based tunnelling during development to make locally running services accessible to other components.
* Troubleshot connectivity, runtime, and integration issues across the prediction model, agent service, and frontend.

📡 API Endpoints

POST /predict

Accepts environmental parameters and returns the predicted trajectory.

Example request:

{
  "latitude": 15.0,
  "longitude": 85.0,
  "pressure": 990.0,
  "wind": 120.0,
  "sst": 29.0,
  "speed": 15.0
}

The values above are illustrative inputs, not validated operational thresholds.

Purpose:

* Accepts the required prediction parameters.
* Invokes the trajectory prediction model.
* Returns predicted trajectory coordinates for frontend visualization.

The exact response schema depends on the model implementation.

POST /chat

Accepts user messages and routes them to the VYOM conversational agent.

Example request:

{
  "message": "What could be the potential impact of this predicted trajectory?"
}

Purpose:

* Receives a user query from the frontend.
* Routes the query to the agent service.
* Uses the available prediction context where supported.
* Returns a generated response to the frontend.

The request and response schemas should be adjusted to match the actual implementation.

🔄 Application Workflow

1. The user enters the required environmental parameters through the frontend.
2. The frontend sends a request to the FastAPI prediction endpoint.
3. The trajectory model processes the input and generates predictions.
4. The backend returns the results to the frontend for visualization.
5. The user can interact with the VYOM agent through the chat interface.
6. The chat backend routes the query to the agent service.
7. The agent uses the available context to generate a response.
8. The frontend displays the response alongside the prediction interface.

🎯 Project Objective

VYOM aims to combine predictive machine learning and conversational AI to support disaster preparedness and decision-making.

By making model predictions accessible through a user-facing interface and providing a conversational layer for interpreting results, the system seeks to make complex disaster-related information easier to understand and use.

⚠️ Limitations

* Prediction accuracy depends on the underlying model, input quality, and available environmental data.
* Potential casualty and financial-loss estimates depend on the corresponding estimation models and assumptions.
* Conversational AI responses may contain inaccuracies and should not be treated as independently verified predictions.
* The system should not be used as the sole basis for emergency response or life-critical decisions without appropriate validation.

👥 Team & Acknowledgements

Developed as part of the Smart India Hackathon (SIH).

VYOM represents a collaborative effort spanning machine learning, backend development, frontend integration, and conversational AI.

⸻

VYOM — From Prediction to Preparedness.
