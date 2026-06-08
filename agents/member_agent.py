from rag.rag import get_context


def member_summary(patient):
    rag_result = get_context("member")

    return {
    "agent": "Member Agent",
    "title": "Patient-Friendly Health Summary",
    "patient": patient["name"],
    "summary": (
    f"{patient['name']} has the following conditions: "
    f"{', '.join(patient['conditions'])}. "
    f"Current medications include: "
    f"{', '.join(patient['medications'])}. "
    "This view explains health information in simple language."
),
    "lab_explanation": explain_labs(patient),
    "next_steps": build_next_steps(patient),
    "knowledge_source": rag_result["source"],
    "context": rag_result["context"]
}

def explain_labs(patient):
    labs = patient["labs"]
    explanations = []

    hba1c = labs.get("hba1c")

    if hba1c is not None:
        if hba1c >= 8:
            explanations.append(
                f"HbA1c is {hba1c}, which may mean blood sugar has been running high."
            )
        else:
            explanations.append(
                f"HbA1c is {hba1c}, which appears closer to common diabetes goals."
            )

    bp = labs.get("bp")

    if bp:
        systolic = int(bp.split("/")[0])

        if systolic >= 140:
            explanations.append(
                f"Blood pressure is {bp}, which is elevated and may need follow-up."
            )
        else:
            explanations.append(
                f"Blood pressure is {bp}, which appears closer to goal."
            )

    if not explanations:
        explanations.append("No major lab explanation is available in this demo.")

    return explanations


def build_next_steps(patient):
    if patient["care_gaps"]:
        return [
            f"Ask your care team about: {gap}"
            for gap in patient["care_gaps"]
        ]

    return ["Continue routine follow-up with your care team."]
