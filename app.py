import streamlit as st
import pickle
import numpy as np

# Load the pretrained model
model_path = r"model1.pkl"
model = pickle.load(open(model_path, 'rb'))

# Define the function to make predictions
def predict_heart_disease(cp, thalach, slope, restecg, chol, trestbps, fbs, oldpeak):
    input_data = np.array([[cp, thalach, slope, restecg, chol, trestbps, fbs, oldpeak]])
    prediction = model.predict(input_data)[0]
    return prediction

# Create the Streamlit app
def main():
    st.title("Heart Disease Prediction App")

    st.sidebar.title("Input Parameters")
    cp = st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3])
    thalach = st.sidebar.slider("Maximum Heart Rate Achieved", 60, 200, 100)
    slope = st.sidebar.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
    restecg = st.sidebar.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
    chol = st.sidebar.slider("Serum Cholesterol (mg/dl)", 100, 500, 200)
    trestbps = st.sidebar.slider("Resting Blood Pressure (mm Hg)", 90, 200, 120)
    fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    oldpeak = st.sidebar.slider("ST Depression Induced by Exercise Relative to Rest", 0.0, 6.2, 1.0)

    if st.sidebar.button("Predict"):
        result = predict_heart_disease(cp, thalach, slope, restecg, chol, trestbps, fbs, oldpeak)
        if result == 0:
            st.write("Prediction: No Heart Disease")
        else:
            st.write("Prediction: Heart Disease Present")

if __name__ == "__main__":
    main()
