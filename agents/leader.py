from data.patients import PATIENTS, get_patient
from agents.member_agent import member_summary
from agents.clinician_agent import clinical_summary
from agents.provider_agent import provider_summary
from agents.care_manager_agent import care_manager_summary


def leader_route(role, patient_id=None):
    """
    Central leader router.

    The leader receives the role and patient_id.
    It decides which vertical agent should handle the request.
    """

    role = role.lower()

    if role == "care_manager":
        return care_manager_summary(PATIENTS)

    patient = get_patient(patient_id)

    if patient is None:
        return {"error": f"Patient {patient_id} not found"}

    if role == "member":
        return member_summary(patient)

    if role == "clinician":
        return clinical_summary(patient)

    if role == "provider":
        return provider_summary(patient)

    return {"error": f"Invalid role: {role}"}
