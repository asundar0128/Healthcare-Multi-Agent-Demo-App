# Streamlit UI - 4 roles and 7 patients Sample Outputs

- Member

<img width="892" height="832" alt="Healthcare Multi Agent Demo App - member - different patient" src="https://github.com/user-attachments/assets/b7af36ae-a65f-411f-8d0e-569c009429bc" />

<img width="1330" height="817" alt="Healthcare Multi Agent Demo App - member" src="https://github.com/user-attachments/assets/d774061c-cd31-4c71-9883-41cd432faf03" />

- Clinician

<img width="917" height="797" alt="Healthcare Multi Agent Demo App - clinician - emily johnson" src="https://github.com/user-attachments/assets/940f828b-2628-4c2e-9e33-df57b8bd025e" />

<img width="906" height="787" alt="Healthcare Multi Agent Demo App - clinician - sarah patel" src="https://github.com/user-attachments/assets/f14daa39-bff7-4286-a45d-14e9f0cb5817" />

- Provider

<img width="922" height="772" alt="Healthcare Multi Agent Demo App - provider - different patient" src="https://github.com/user-attachments/assets/d98d6842-cc29-476d-9a4b-15bb38a4ba38" />

<img width="832" height="752" alt="Healthcare Multi Agent Demo App - provider" src="https://github.com/user-attachments/assets/ce64a691-357e-4c9c-94ef-1c5d9d737938" />

- Care Manager

<img width="897" height="840" alt="Healthcare Multi Agent Demo App - care manager - condition counts" src="https://github.com/user-attachments/assets/4c7331d5-75e1-43f1-b097-0e980e3f3f4f" />

<img width="1072" height="725" alt="Healthcare Multi Agent Demo App - care manager - population summary" src="https://github.com/user-attachments/assets/0fb05632-d8b0-4052-b661-13626d2fc18d" />

<img width="1167" height="792" alt="Healthcare Multi Agent Demo App - care manager" src="https://github.com/user-attachments/assets/2254f272-dd7b-4c9d-8f2f-84daa8e8a9b8" />

# Healthcare Multi Agent Demo App

A lightweight healthcare AI prototype demonstrating a **Leader Agent architecture** with role-based routing for different healthcare stakeholders.

The system uses a single FastAPI endpoint and a central Leader Agent to route requests to specialized healthcare agents:

* Member Agent
* Clinician Agent
* Provider Agent
* Care Manager Agent

The project also includes a simple Retrieval-Augmented Generation (RAG) layer that retrieves role-specific healthcare knowledge from local knowledge files.

---

## Project Overview

Healthcare workflows often involve multiple stakeholders with different information needs.

This project simulates a simplified healthcare environment where a central Leader Agent routes requests to specialized agents based on user role.

Examples:

* Patients (Members) need simplified explanations of their conditions and lab results.
* Clinicians need clinical summaries and care gap information.
* Providers need prior authorization and documentation reviews.
* Care Managers need population health and outreach insights.

---

## Architecture

```text
Streamlit UI
     |
     v
FastAPI API
     |
     v
Leader Agent
     |
     +----------------+
     |                |
     v                v
Member Agent     Clinician Agent
     |
     +----------------+
     |                |
     v                v
Provider Agent   Care Manager Agent
     |
     v
Simple Local RAG
```

---

<img width="1024" height="617" alt="c4a12f22-9baa-4f85-bf51-3a840611a20b" src="https://github.com/user-attachments/assets/84b2f524-cb4b-4c09-a1cf-054b534e9cb9" />

## Agents

### Member Agent

Patient-facing assistant.

Responsibilities:

* Explain conditions in simple language
* Summarize medications
* Explain lab results
* Recommend next steps
* Retrieve educational healthcare guidance

---

### Clinician Agent

Clinician-facing assistant.

Responsibilities:

* Generate clinical summaries
* Calculate simple risk scores
* Display care gaps
* Review medications and labs
* Retrieve clinical care-gap guidance

---

### Provider Agent

Provider-facing assistant.

Responsibilities:

* Review prior authorization requests
* Identify missing documentation
* Estimate denial risk
* Provide submission recommendations
* Retrieve utilization management guidance

---

### Care Manager Agent

Population health assistant.

Responsibilities:

* Analyze all patients
* Identify patients with care gaps
* Identify high-utilization patients
* Generate outreach lists
* Support value-based care concepts

---

## Retrieval-Augmented Generation (RAG)

This project uses a lightweight RAG implementation.

Instead of embeddings or vector databases, each agent retrieves role-specific information from local knowledge files.

Examples:

* patient_education.txt
* clinical_care_gaps.txt
* prior_auth.txt
* population_health.txt

The goal is to demonstrate how retrieval can be integrated into an agent workflow while keeping the architecture simple and explainable.

---

## Mock Patient Population

The project includes a synthetic patient population containing examples of:

* Diabetes
* Hypertension
* Congestive Heart Failure (CHF)
* Chronic Kidney Disease (CKD)
* COPD
* Hyperlipidemia
* Asthma

Each patient includes:

* Conditions
* Lab values
* Medications
* Care gaps
* Utilization history
* Prior authorization information

No real patient data is used.

---

## Technology Stack

* Python
* FastAPI
* Streamlit
* Simple RAG
* REST APIs

---

## Running the Project

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI

```bash
python -m uvicorn app:app --reload
```

### Start Streamlit

```bash
python -m streamlit run streamlit_app.py
```

---

## Example Workflow

1. Select a role in Streamlit.
2. Select a patient.
3. Click Go.
4. The Leader Agent routes the request.
5. The selected healthcare agent processes the request.
6. Relevant healthcare guidance is retrieved through the RAG layer.
7. Results are displayed in the UI.

---

<img width="1024" height="559" alt="d2bf71aa-dd26-4e0f-bf19-137f2f005fff" src="https://github.com/user-attachments/assets/57d11275-315e-4128-a9db-ae500e7e5451" />

## Learning Objectives

This project was built to explore:

* Multi-agent architectures
* Agent routing patterns
* Healthcare AI workflows
* Population health concepts
* Prior authorization workflows
* Care gap analysis
* Lightweight Retrieval-Augmented Generation (RAG)
* FastAPI and Streamlit integration

---

## Disclaimer

This project is for educational and demonstration purposes only.

All patient data is synthetic and does not represent real individuals.

The system does not provide medical advice and should not be used for clinical decision-making.
