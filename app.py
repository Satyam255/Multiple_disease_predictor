import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(
    open(r'C:\Users\Admin\OneDrive\Desktop\ML projects\Multiple_disease_predictor\diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(
    open(r'C:\Users\Admin\OneDrive\Desktop\ML projects\Multiple_disease_predictor\heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(
    open(r'C:\Users\Admin\OneDrive\Desktop\ML projects\Multiple_disease_predictor\parkinsons_model.sav', 'rb'))

# sidebar for navigation


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction'],

                           icons=['activity', 'heart', 'person'],
                           default_index=0)

    ## default index 0 means that when the page is opened for first time. diabetes prediction will be selected

# Diabetes Predicition Page

if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Not Diabetic'

    st.success(diab_diagnosis)

# Heart Disease Predicition Page

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input('Age of the Person')
    with col2:
        sex = st.text_input('Sex (1 = male, 0 = female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0 to 3)')
    with col4:
        trestbps = st.text_input('Resting Blood Pressure')
    with col1:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar (> 120 mg/dl, 1 = true; 0 = false)')
    with col3:
        restecg = st.text_input('Resting ECG results (0 to 2)')
    with col4:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col1:
        exang = st.text_input('Exercise Induced Angina (1 = yes, 0 = no)')
    with col2:
        oldpeak = st.text_input('ST Depression induced by exercise relative to rest')
    with col3:
        slope = st.text_input('Slope of the Peak Exercise ST segment (0 to 2)')
    with col4:
        ca = st.text_input('Number of Major Vessels (0-3) colored by fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)')

    # Prediction and output
    heart_diagnosis = ''

    # Button for Prediction
    if st.button('Heart Disease Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The Person has a Heart problem'
        else:
            heart_diagnosis = 'The Person does not have a Heart problem'

    st.success(heart_diagnosis)

# Parkinson's Disease Prediction Page
if (selected == 'Parkinsons Disease Prediction'):
    # page title
    st.title('Parkinson\'s Disease Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)')
    with col4:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col1:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col2:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col3:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col4:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col1:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col2:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col3:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col4:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col4:
        HNR = st.text_input('HNR')
    with col1:
        RPDE = st.text_input('RPDE')
    with col2:
        DFA = st.text_input('DFA')
    with col3:
        spread1 = st.text_input('Spread1')
    with col4:
        spread2 = st.text_input('Spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # Prediction and output
    parkinsons_diagnosis = ''

    # Button for Prediction
    if st.button('Parkinsons Disease Result'):
        parkinsons_prediction = parkinsons_model.predict([[MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent,
                                                           MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                                                           MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
                                                           MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2,
                                                           D2, PPE]])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The Person has Parkinson\'s Disease'
        else:
            parkinsons_diagnosis = 'The Person does not have Parkinson\'s Disease'

    st.success(parkinsons_diagnosis)
