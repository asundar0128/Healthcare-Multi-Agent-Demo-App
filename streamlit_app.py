import requests
import streamlit as st

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Healthcare Multi Agent Demo App",
    page_icon="🏥",
    layout="centered"
)

st.title("Healthcare Multi Agent Demo App")

st.caption(
    "Select a role and patient. The Leader Agent routes the request "
    "to the appropriate healthcare agent."
)

# --------------------------------------
# Load Patients
# --------------------------------------

try:
    patients = requests.get(f"{API_URL}/patients").json()
except Exception:
    st.error(
        "FastAPI backend is not running.\n\n"
        "Start it using:\n"
        "python -m uvicorn app:app --reload"
    )
    st.stop()

# --------------------------------------
# Dropdown Data
# --------------------------------------

patient_lookup = {
    f"{patient['id']} - {patient['name']}": patient["id"]
    for patient in patients
}

# --------------------------------------
# Controls
# --------------------------------------

role = st.selectbox(
    "Role",
    [
        "member",
        "clinician",
        "provider",
        "care_manager"
    ]
)

selected_patient = st.selectbox(
    "Patient",
    list(patient_lookup.keys())
)

patient_id = patient_lookup[selected_patient]

go = st.button(
    "Go",
    use_container_width=True
)

# --------------------------------------
# Results
# --------------------------------------

if go:

    params = {
        "role": role
    }

    if role != "care_manager":
        params["patient_id"] = patient_id

    response = requests.get(
        f"{API_URL}/invoke",
        params=params
    )

    result = response.json()

    st.divider()

    st.subheader(
        result.get(
            "title",
            "Agent Result"
        )
    )

    st.success(
        f"Routed to {result.get('agent', 'Unknown Agent')}"
    )

    # ----------------------------------
    # MEMBER
    # ----------------------------------

    if role == "member":

        st.write(result["summary"])

        st.markdown("### Lab Explanation")

        for item in result["lab_explanation"]:
            st.write(f"• {item}")

        st.markdown("### Next Steps")

        for step in result["next_steps"]:
            st.write(f"• {step}")

    # ----------------------------------
    # CLINICIAN
    # ----------------------------------

    elif role == "clinician":

        st.markdown("### Clinical Note")

        st.write(
            result["clinical_note"]
        )

        st.markdown("### Risk Level")

        risk = result["risk_level"]

        if risk == "High":
            st.error("High")

        elif risk == "Medium":
            st.warning("Medium")

        else:
            st.success("Low")

        st.markdown("### Conditions")

        for condition in result["conditions"]:
            st.write(f"• {condition}")

        st.markdown("### Care Gaps")

        if result["care_gaps"]:

            for gap in result["care_gaps"]:
                st.write(f"• {gap}")

        else:
            st.write(
                "No open care gaps."
            )

    # ----------------------------------
    # PROVIDER
    # ----------------------------------

    elif role == "provider":

        st.markdown(
            "### Prior Authorization"
        )

        st.write(
            f"**Patient:** {result['patient']}"
        )

        st.write(
            f"**Service:** {result['service']}"
        )

        st.write(
            f"**Status:** {result['status']}"
        )

        st.write(
            f"**Denial Risk:** {result['denial_risk']}"
        )

        st.markdown(
            "### Missing Documentation"
        )

        if result["missing_docs"]:

            for doc in result["missing_docs"]:
                st.write(f"• {doc}")

        else:
            st.write(
                "No missing documentation."
            )

        st.markdown(
            "### Recommendation"
        )

        st.write(
            result["recommendation"]
        )

    # ----------------------------------
    # CARE MANAGER
    # ----------------------------------

    elif role == "care_manager":

        st.markdown(
            "### Population Summary"
        )

        st.write(
            f"**Total Patients:** {result['total_patients']}"
        )

        st.write(
            f"**Patients With Care Gaps:** "
            f"{result['patients_with_care_gaps']}"
        )

        st.write(
            f"**High Utilization Patients:** "
            f"{result['high_utilization_patients']}"
        )

        st.markdown(
            "### Condition Counts"
        )

        st.dataframe(
            [
                {
                    "Condition": condition,
                    "Count": count
                }
                for condition, count
                in result["condition_counts"].items()
            ],
            use_container_width=True,
            hide_index=True
        )

        st.markdown(
            "### Outreach List"
        )

        st.dataframe(
            result["outreach_list"],
            use_container_width=True,
            hide_index=True
        )

        st.markdown(
            "### Focus Areas"
        )

        for item in result["focus_areas"]:
            st.write(f"• {item}")

    # ----------------------------------
    # SIMPLE RAG DISPLAY
    # ----------------------------------

    with st.expander(
        "Knowledge Context"
    ):
        st.write(
            result.get(
                "context",
                "No context available."
            )
        )
