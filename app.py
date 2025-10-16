import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

# ------------------------------
# Título e introdução
# ------------------------------
st.set_page_config(page_title="Car Efficiency ML App 🚗", layout="centered")

st.title("🚗 Car Efficiency Classifier")
st.markdown("""
This app predicts **vehicle efficiency** using a Machine Learning model trained on the classic *cars.csv* dataset.
Upload your dataset or use the demo data below.
""")

# ------------------------------
# Upload ou dataset demo
# ------------------------------
uploaded_file = st.file_uploader("📂 Upload your `cars.csv` file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.info("No file uploaded. Using demo dataset.")
    df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

# ------------------------------
# Pré-processamento
# ------------------------------
for col in ['cubicinches', 'weightlbs']:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '').str.strip(), errors='coerce')
    df[col].fillna(df[col].mean(), inplace=True)

df['efficiency'] = np.where(df['mpg'] > 25, 1, 0)

scaler = StandardScaler()
X = df[['cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60']]
y = df['efficiency']
X_scaled = scaler.fit_transform(X)

# ------------------------------
# Modelo
# ------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_scaled, y)

st.success("✅ Model trained successfully!")

# ------------------------------
# Estatísticas básicas
# ------------------------------
st.subheader("📊 Dataset Overview")
st.write(df.describe())

# ------------------------------
# Interface de previsão
# ------------------------------
st.subheader("🔮 Try your own car data")

c1, c2, c3 = st.columns(3)
cylinders = c1.number_input("Cylinders", 3, 12, 4)
cubicinches = c2.number_input("Cubic Inches", 60, 500, 150)
hp = c3.number_input("Horsepower (HP)", 40, 300, 100)

c4, c5 = st.columns(2)
weight = c4.number_input("Weight (lbs)", 1500, 6000, 2500)
time_to_60 = c5.number_input("Time to 60 mph (s)", 5, 25, 15)

if st.button("Predict Efficiency 🚀"):
    new_data = np.array([[cylinders, cubicinches, hp, weight, time_to_60]])
    new_data_scaled = scaler.transform(new_data)
    prediction = model.predict(new_data_scaled)[0]
    if prediction == 1:
        st.success("🌱 This vehicle is **Efficient!** (mpg > 25)")
    else:
        st.error("⛽ This vehicle is **Not Efficient.** (mpg ≤ 25)")
