# Flood Risk Prediction in Kinshasa - DRC

## 🌍 Problem
Kinshasa floods cause deaths and damage every year. This project predicts flood risk in communes like Lemba, Limete, Mont Ngafula.

## 🧠 Solution - Machine Learning
Machine Learning model trained on DRC geographical data (altitude, rainfall, river proximity, urban density).

### Features used:
- altitude (m)
- rainfall (mm)
- river_distance (km)
- urban_density
- slope, soil_type, drainage

### Model: RandomForestClassifier (accuracy > 90%)

## 🚨 Alert System
- check_risk(): Real-time risk for Gemena-Karawa, Lisala-Bumba
- Alert if risk > 70%: EVACUATION

## 💻 How to run
pip install -r requirements.txt
python main.py

## 👨‍💻 Author
Ir Victor Mputu Mamba - Geomatics Engineer
Lubumbashi, DRC - Candidate AMMI 2026
GitHub: Mputu96

## 🎯 Why AMMI?
I want to bring AI for humanitarian action in DRC. First Congolese to use ML for flood prevention in Equateur & Kinshasa.

## 🔗 Dataset
Synthetic data inspired by real topography of Congo Basin.