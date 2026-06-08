PATIENTS = [
    {
        "id": "P001",
        "name": "John Smith",
        "age": 67,
        "conditions": ["Diabetes", "Hypertension", "CHF"],
        "labs": {
            "hba1c": 8.9,
            "bp": "152/95",
            "ldl": 145
        },
        "medications": [
            "Metformin",
            "Lisinopril",
            "Furosemide"
        ],
        "care_gaps": [
            "Diabetic eye exam overdue",
            "HbA1c follow-up overdue"
        ],
        "utilization": {
            "er_visits": 2,
            "hospitalizations": 1
        },
        "prior_auth": {
            "service": "Lumbar MRI",
            "status": "Pending",
            "missing_docs": [
                "Physical therapy notes"
            ]
        }
    },

    {
        "id": "P002",
        "name": "Maria Garcia",
        "age": 54,
        "conditions": [
            "Diabetes",
            "Hyperlipidemia"
        ],
        "labs": {
            "hba1c": 6.8,
            "bp": "126/82",
            "ldl": 160
        },
        "medications": [
            "Metformin",
            "Atorvastatin"
        ],
        "care_gaps": [
            "Diabetic eye exam overdue"
        ],
        "utilization": {
            "er_visits": 0,
            "hospitalizations": 0
        },
        "prior_auth": {
            "service": "Continuous Glucose Monitor",
            "status": "Approved",
            "missing_docs": []
        }
    },

    {
        "id": "P003",
        "name": "Robert Lee",
        "age": 72,
        "conditions": [
            "CHF",
            "Hypertension"
        ],
        "labs": {
            "hba1c": None,
            "bp": "160/100",
            "ldl": 132
        },
        "medications": [
            "Carvedilol",
            "Furosemide"
        ],
        "care_gaps": [
            "Blood pressure follow-up overdue",
            "CHF weight monitoring overdue"
        ],
        "utilization": {
            "er_visits": 3,
            "hospitalizations": 2
        },
        "prior_auth": {
            "service": "Home Health Monitoring",
            "status": "Submitted",
            "missing_docs": []
        }
    },

    {
        "id": "P004",
        "name": "Sarah Patel",
        "age": 61,
        "conditions": [
            "COPD"
        ],
        "labs": {
            "hba1c": None,
            "bp": "130/84",
            "ldl": 118
        },
        "medications": [
            "Albuterol",
            "Tiotropium"
        ],
        "care_gaps": [
            "Pulmonary follow-up overdue"
        ],
        "utilization": {
            "er_visits": 1,
            "hospitalizations": 0
        },
        "prior_auth": {
            "service": "Pulmonary Rehab",
            "status": "Pending",
            "missing_docs": [
                "Recent spirometry report"
            ]
        }
    },

    {
        "id": "P005",
        "name": "David Kim",
        "age": 69,
        "conditions": [
            "CKD",
            "Hypertension"
        ],
        "labs": {
            "hba1c": None,
            "bp": "148/92",
            "ldl": 125
        },
        "medications": [
            "Losartan",
            "Amlodipine"
        ],
        "care_gaps": [
            "Kidney function follow-up overdue",
            "Blood pressure follow-up overdue"
        ],
        "utilization": {
            "er_visits": 1,
            "hospitalizations": 1
        },
        "prior_auth": {
            "service": "Nephrology Referral",
            "status": "Approved",
            "missing_docs": []
        }
    },

    {
        "id": "P006",
        "name": "Emily Johnson",
        "age": 29,
        "conditions": [
            "Asthma"
        ],
        "labs": {
            "hba1c": None,
            "bp": "118/76",
            "ldl": 95
        },
        "medications": [
            "Albuterol"
        ],
        "care_gaps": [],
        "utilization": {
            "er_visits": 0,
            "hospitalizations": 0
        },
        "prior_auth": {
            "service": "None",
            "status": "None",
            "missing_docs": []
        }
    },

    {
        "id": "P007",
        "name": "Linda Brown",
        "age": 64,
        "conditions": [
            "Diabetes",
            "CKD"
        ],
        "labs": {
            "hba1c": 9.2,
            "bp": "142/88",
            "ldl": 138
        },
        "medications": [
            "Insulin",
            "Losartan"
        ],
        "care_gaps": [
            "HbA1c follow-up overdue",
            "Kidney function follow-up overdue"
        ],
        "utilization": {
            "er_visits": 2,
            "hospitalizations": 1
        },
        "prior_auth": {
            "service": "Continuous Glucose Monitor",
            "status": "Pending",
            "missing_docs": [
                "Recent glucose logs"
            ]
        }
    }
]


def get_patient(patient_id):
    for patient in PATIENTS:
        if patient["id"] == patient_id:
            return patient

    return None
