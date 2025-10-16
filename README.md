# car-efficiency-streamlit
A deployable ML pipeline transformed into an interactive Streamlit app — from data preprocessing to live predictions on car efficiency. (Um pipeline de ML implantável, transformado em app interativo Streamlit — do pré-processamento à predição ao vivo.)


# 🚗 Car Efficiency Predictor – Streamlit App  

[![Streamlit App](https://img.shields.io/badge/Launch-App-blue?logo=streamlit)](https://car-efficiency.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML%20Model-orange?logo=scikitlearn)](https://scikit-learn.org/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🇧🇷 Descrição (Português)

Este projeto é uma aplicação interativa em **Streamlit** que utiliza Machine Learning para prever a eficiência de veículos com base no dataset `cars.csv`.  
O modelo foi treinado com um **Decision Tree Classifier**, após etapas de **pré-processamento, normalização e criação de variável de eficiência** (`mpg > 25`).

O app permite que o usuário:
- Faça upload do próprio dataset, ou use dados de demonstração.  
- Visualize estatísticas do conjunto de dados.  
- Insira características de um carro e veja se ele é eficiente ou não.

---

### Tecnologias utilizadas
- Python 3.11+  
- Streamlit  
- Scikit-learn  
- Pandas / NumPy  

---

### Como executar localmente
1. Clone este repositório:
   ```bash
   git clone https://github.com/soares-ari/car-efficiency-streamlit.git
   cd car-efficiency-streamlit
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Rode o app:
   ```bash
   streamlit run app.py
   ```
4. Acesse o app em: http://localhost:8501

---

### Deploy
Aplicação disponível online:  
👉 https://car-efficiency.streamlit.app

---

### Sobre o modelo
O modelo utiliza os atributos:
['cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60']
para prever a eficiência (`mpg > 25`).
Treinado com DecisionTreeClassifier(random_state=42) e StandardScaler().

---

### Autor
**Ariel Soares**  
Engenheiro de Machine Learning & Desenvolvedor Full Stack  
📍 Brasília, Brasil  
🔗 LinkedIn: https://www.linkedin.com/in/soares-ari  
🔗 GitHub: https://github.com/soares-ari

---

## 🇺🇸 Description (English)

This project is an interactive **Streamlit web app** that uses Machine Learning to predict vehicle fuel efficiency based on the `cars.csv` dataset.  
The model was trained using a **Decision Tree Classifier** after preprocessing, normalization, and efficiency variable creation (`mpg > 25`).

The app allows users to:
- Upload their own dataset or use demo data.  
- Explore descriptive statistics.  
- Input car attributes and instantly see if it’s efficient or not.

---

### Tech Stack
- Python 3.11+  
- Streamlit  
- Scikit-learn  
- Pandas / NumPy  

---

### Run Locally
```bash
git clone https://github.com/soares-ari/car-efficiency-streamlit.git
cd car-efficiency-streamlit
pip install -r requirements.txt
streamlit run app.py
```

---

### Live App
👉 https://car-efficiency.streamlit.app

---

### Model Overview
Features used for training:
['cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60']
Target: binary efficiency label (`mpg > 25`)
Algorithm: Decision Tree Classifier + StandardScaler

---

### Author
**Ariel Soares**  
Machine Learning Engineer & Full Stack Developer  
📍 Brasília, Brazil  
🔗 LinkedIn: https://www.linkedin.com/in/ari-soares  
🔗 GitHub: https://github.com/soares-ari

---

### License
This project is licensed under the MIT License.
