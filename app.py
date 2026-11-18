import pickle
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.metrics import (accuracy_score,classification_report,ConfusionMatrixDisplay)


st.set_page_config(page_title="Antibiotic Resistance Prediction ",page_icon="🧫",layout="wide")

st.markdown("""<style>.stApp {background-color: #F5F7FA;.stFormSubmitButton > button {background-color: #00897B;color: white;border: none;}
            .stFormSubmitButton > button:hover {background-color: #00695C;color: white;}</style>""", unsafe_allow_html=True)

st.markdown("""<style>.stApp {background-color: #F5F7FA;}</style>""", unsafe_allow_html=True)

st.markdown("""<h1 style='text-align: left;'><span style='color: #00897B;'>Bacti</span><span style='color: #263238;'>Sense</span>
</h1><h3 style='text-align: left;'>Predictive Machine Learning For Bacterial Antibiotic Resistance</h3>""", unsafe_allow_html=True)

st.markdown("""<div style="background-color: #E8F5E9; color: #2E7D32; padding: 12px; border-radius: 8px;">
<b>⚠️ Educational project only.</b> This model is not clinically validated.Do not use predictions to choose antibiotics or prescribe medicines.
</div>""", unsafe_allow_html=True)

MODEL_PATH = Path(__file__).parent / "antibiotic_model.pkl"
@st.cache_resource
def load_saved_data():
    with open(MODEL_PATH, "rb") as file:
        saved_object = pickle.load(file)

    if isinstance(saved_object, dict):
        model = saved_object["model"]
        y_test = saved_object.get("y_test")
        y_pred = saved_object.get("y_pred")
    else:
        model = saved_object
        y_test = None
        y_pred = None

    return model, y_test, y_pred


try:
    model, y_test, y_pred = load_saved_data()
except Exception as error:
    st.error(f"Could not load antibiotic_model.pkl: {error}")
    st.info(
        "Keep antibiotic_model.pkl in the same folder as app.py. "
        "Use the scikit-learn version used to save the model."
    )
    st.stop()

feature_columns = ["Age","Gender","Organism","Diabetes",
                   "Hypertension","Hospital_before","Infection_Freq","Antibiotic"]
try:
    encoder = (model.named_steps["preprocessor"].named_transformers_["cat"].named_steps["encoder"])
    categorical_columns = ["Gender","Organism","Diabetes","Hypertension","Hospital_before","Infection_Freq","Antibiotic",]
    options = {column: sorted(list(values))for column, values in zip(categorical_columns, encoder.categories_)}
except Exception as error:
    st.error(f"Could not read categories from the saved model: {error}")
    st.stop()

st.header("Predict Resistance Status")
st.write("Enter the information below to obtain an experimental model prediction.")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=40)
        gender = st.selectbox("Gender", options["Gender"])
        organism = st.selectbox("Organism", options["Organism"])
        antibiotic = st.selectbox("Antibiotic", options["Antibiotic"])

    with col2:
        diabetes = st.selectbox("Diabetes", options["Diabetes"])
        hypertension = st.selectbox("Hypertension", options["Hypertension"])
        hospital_before = st.selectbox(
            "Hospitalized before", options["Hospital_before"]
        )
        infection_freq = st.selectbox(
            "Infection Frequency", options["Infection_Freq"]
        )

    submitted = st.form_submit_button(
        "Predict", type="primary", use_container_width=True
    )

if submitted:
    input_data = pd.DataFrame(
        [{
            "Age": age,
            "Gender": gender,
            "Organism": organism,
            "Diabetes": diabetes,
            "Hypertension": hypertension,
            "Hospital_before": hospital_before,
            "Infection_Freq": infection_freq,
            "Antibiotic": antibiotic,
        }],
        columns=feature_columns,
    )

    try:
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        classes = model.named_steps["classifier"].classes_
        probability_values = dict(zip(classes, probabilities))

        st.subheader("Prediction Result")
        if prediction == "R":
            st.error("Predicted Class: RESISTANT (R)")
        else:
            st.success("Predicted Class: SUSCEPTIBLE (S)")

        col1, col2 = st.columns(2)
        col1.metric(
            "Estimated probability of R",
            f"{probability_values.get('R', 0):.2%}",
        )
        col2.metric(
            "Estimated probability of S",
            f"{probability_values.get('S', 0):.2%}",
        )
        st.caption(
            "These are model-estimated probabilities and have not been clinically "
            "calibrated. They must not guide treatment decisions."
        )
    except Exception as error:
        st.error(f"Prediction failed: {error}")

st.divider()


