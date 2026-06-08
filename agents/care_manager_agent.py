from rag.rag import get_context


def care_manager_summary(patients):
    rag_result = get_context("care_manager")

    patients_with_gaps = [
        patient for patient in patients
        if patient["care_gaps"]
    ]

    high_utilization = [
        patient for patient in patients
        if patient["utilization"]["er_visits"] >= 2
        or patient["utilization"]["hospitalizations"] >= 1
    ]

    return {
        "agent": "Care Manager Agent",
        "title": "Population Health Summary",
        "total_patients": len(patients),
        "patients_with_care_gaps": len(patients_with_gaps),
        "high_utilization_patients": len(high_utilization),
        "condition_counts": count_conditions(patients),
        "outreach_list": build_outreach_list(patients),
        "focus_areas": [
            "Close chronic disease care gaps",
            "Reduce avoidable ER visits",
            "Prioritize high-utilization patients"
        ],
        "knowledge_source": rag_result["source"],
        "context": rag_result["context"]
    }


def count_conditions(patients):
    counts = {}

    for patient in patients:
        for condition in patient["conditions"]:
            if condition not in counts:
                counts[condition] = 0

            counts[condition] += 1

    return counts


def build_outreach_list(patients):
    outreach = []

    for patient in patients:
        has_care_gaps = len(patient["care_gaps"]) > 0
        high_er_use = patient["utilization"]["er_visits"] >= 2
        recent_hospitalization = patient["utilization"]["hospitalizations"] >= 1

        if has_care_gaps or high_er_use or recent_hospitalization:
            outreach.append({
                "patient_id": patient["id"],
                "name": patient["name"],
                "conditions": ", ".join(patient["conditions"]),
                "care_gaps": "; ".join(patient["care_gaps"]) if patient["care_gaps"] else "None",
                "er_visits": patient["utilization"]["er_visits"],
                "hospitalizations": patient["utilization"]["hospitalizations"]
            })

    return outreach
