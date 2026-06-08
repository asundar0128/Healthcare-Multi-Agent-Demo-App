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
