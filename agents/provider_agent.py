from rag.rag import get_context


def provider_summary(patient):
    rag_result = get_context("provider")

    prior_auth = patient["prior_auth"]
    missing_docs = prior_auth["missing_docs"]

    if missing_docs:
        denial_risk = "High"
    else:
        denial_risk = "Low"

    return {
        "agent": "Provider Agent",
        "title": "Prior Authorization Summary",
        "patient": patient["name"],
        "service": prior_auth["service"],
        "status": prior_auth["status"],
        "missing_docs": missing_docs,
        "denial_risk": denial_risk,
        "recommendation": build_recommendation(missing_docs),
        "knowledge_source": rag_result["source"],
        "context": rag_result["context"]
    }


def build_recommendation(missing_docs):
    if missing_docs:
        return (
            "Collect missing documentation before "
            "submission or review."
        )

    return (
        "No missing documentation is listed "
        "in this demo."
    )
