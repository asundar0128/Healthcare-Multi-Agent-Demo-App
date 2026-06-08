from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
KB_DIR = BASE_DIR / "knowledge_base"

TOPIC_TO_FILE = {
    "member": "patient_education.txt",
    "clinician": "clinical_care_gaps.txt",
    "provider": "prior_auth.txt",
    "care_manager": "population_health.txt"
}


def get_context(topic):

    file_name = TOPIC_TO_FILE.get(topic)

    if file_name is None:
        return {
            "source": None,
            "context": "No knowledge context available."
        }

    file_path = KB_DIR / file_name

    if not file_path.exists():
        return {
            "source": file_name,
            "context": "Knowledge file not found."
        }

    return {
        "source": file_name,
        "context": file_path.read_text(encoding="utf-8")
    }
