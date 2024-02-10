import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#cargar los modelos

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    selected = option_menu('Sistema de Predicción de Enfermedades',

                           ['Analisis Diabetes',
                            'Analisis Corazon',
                            'Analisis Parkinson'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
    
# analisis de diabetes
if selected == 'Analisis Diabetes':

    # page title
    st.title('Analisis de Diabetes mediante ML')
    
     # obteniendo datos del usuario
    col1, col2, col3 = st.columns(3)  #oredenar las columnas de tres en tres

    with col1:
        Pregnancies = st.text_input('Numero de embarazos')

    with col2:
        Glucose = st.text_input('Nivel de Glucosa')

    with col3:
        BloodPressure = st.text_input('Presion Sanguinea')

    with col1:
        SkinThickness = st.text_input('Grosor Piel')

    with col2:
        Insulin = st.text_input('Nivel de Insulina')

    with col3:
        BMI = st.text_input('Indice de Masa Corporal')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Valor Funcion de Historial Familiar')

    with col2:
        Age = st.text_input('Edad')


    # codigo para prediccion
    diab_diagnosis = ''

    # creamos boton de resultado

    if st.button('Evaluacion Final'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input] #cambiamos a float los inputs

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Paciente positivo D'
        else:
            diab_diagnosis = 'Paciente Negativo D'

    st.success(diab_diagnosis)
    

# analisis corazon
if selected == 'Analisis Corazon':

    # page title
    st.title('Analisis de Enfermedades Cardiovasculares mediante ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Edad')

    with col2:
        sex = st.text_input('Sexo')

    with col3:
        cp = st.text_input('Tipo Dolor de Pecho')

    with col1:
        trestbps = st.text_input('Presion Arterial en  Reposo')

    with col2:
        chol = st.text_input('Colesterol en suero mg/dl')

    with col3:
        fbs = st.text_input('Glucosa en ayunas > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resultados Electrocardiogrmas en reposo')

    with col2:
        thalach = st.text_input('Frecuencia Cardiaca Maxima')

    with col3:
        exang = st.text_input('Angina inducida por ejercicio')

    with col1:
        oldpeak = st.text_input('Depresion ST inducida por ejercicio')

    with col2:
        slope = st.text_input('Pendiente del ST en Pico de ejercicio')

    with col3:
        ca = st.text_input('Vasos Principales coloreados mediante fluoroscopía')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Evaluacion Final'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'La Persona tiene Problemas Cardiacos'
        else:
            heart_diagnosis = 'La Persona no tiene Problemas Cardiacos'
            

    st.success(heart_diagnosis)

    

if selected == "Analisis Parkinson":

    # page title
    st.title("Analisis de Parkinson mediante ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('Frecuencia fundamental media')

    with col2:
        fhi = st.text_input(' Frecuencia fundamental máxima(Hz)')

    with col3:
        flo = st.text_input('Frecuencia fundamental mínima(Hz)')

    with col4:
        Jitter_percent = st.text_input('variabilidad en los períodos entre ciclos de vibración de la voz.(%)')

    with col5:
        Jitter_Abs = st.text_input('variabilidad en los períodos entre ciclos de vibración de la voz.(Abs)')

    with col1:
        RAP = st.text_input('RAP')

    with col2:
        PPQ = st.text_input('PPQ')

    with col3:
        DDP = st.text_input('DDP')

    with col4:
        Shimmer = st.text_input('Shimmer')

    with col5:
        Shimmer_dB = st.text_input('Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('APQ3')

    with col2:
        APQ5 = st.text_input('APQ5')

    with col3:
        APQ = st.text_input('APQ')

    with col4:
        DDA = st.text_input('DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('Dimensión de entropía de perturbación relativa')

    with col3:
        DFA = st.text_input('Exponente alfa de la caminata fractal')

    with col4:
        spread1 = st.text_input('Medida de la dispersión de la dimensión 1')

    with col5:
        spread2 = st.text_input('Medida de la dispersión de la dimensión 2')

    with col1:
        D2 = st.text_input('Dimensión de correlación')

    with col2:
        PPE = st.text_input(' relación entre la variabilidad de la frecuencia y la energía total en la señal.')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Evaluacion Final"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "Parkinson Positivo"
        else:
            parkinsons_diagnosis = "Parkinson Negativo"

    st.success(parkinsons_diagnosis)