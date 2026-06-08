from rag.rag import get_context


def clinical_summary(patient):
    rag_result = get_context("clinician")

    return {
        "agent": "Clinician Agent",
        "title": "Clinical Summary",
        "patient": patient["name"],
        "conditions": patient["conditions"],
        "medications": patient["medications"],
        "labs": patient["labs"],
        "care_gaps": patient["care_gaps"],
        "risk_level": estimate_risk(patient),
        "clinical_note": build_note(patient),
        "knowledge_source": rag_result["source"],
        "context": rag_result["context"]
    }


def estimate_risk(patient):
    score = 0

    if patient["age"] >= 65:
        score += 1

    if "CHF" in patient["conditions"]:
        score += 2

    if "CKD" in patient["conditions"]:
        score += 2

    if patient["utilization"]["er_visits"] >= 2:
        score += 2

    if patient["utilization"]["hospitalizations"] >= 1:
        score += 2

    if len(patient["care_gaps"]) >= 2:
        score += 1

    if score >= 5:
        return "High"

    if score >= 3:
        return "Medium"

    return "Low"


def build_note(patient):
    if patient["care_gaps"]:
        gaps = ", ".join(patient["care_gaps"])
    else:
        gaps = "no open care gaps"

    return (
        f"{patient['age']}-year-old patient with "
        f"{', '.join(patient['conditions'])}. "
        f"Current medications include {', '.join(patient['medications'])}. "
        f"Recent labs include BP {patient['labs']['bp']} and LDL {patient['labs']['ldl']}. "
        f"Open care gaps: {gaps}."
    )
