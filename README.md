# Flood Risk Prediction in Sud-Ubangi - DRC

## 🌍 Problem
Sud-Ubangi floods (Gemena, Bumba, Lisala) cause deaths and damage every year along Ubangi River. This project predicts flood risk in real-time.

## 🧠 Solution - Machine Learning
Machine Learning model trained on Equateur region data (altitude, rainfall, river proximity, urban density).

### Features used:
- altitude (m) - low altitude in Gemena basin
- rainfall (mm) - rainy season Equateur
- river_distance (km) - distance to Ubangi River
- urban_density
- slope, soil_type, drainage

### Model: RandomForestClassifier (accuracy > 90%)

## 🚨 Alert System
- check_risk(): Real-time risk for Gemena, Lisala-Bumba, Zongo
- Alert if risk > 70%: EVACUATION - Save lives in Sud-Ubangi

## 💻 How to run
pip install -r requirements.txt
python main.py

## 👨‍💻 Author
Ir Victor LENGENASE SENEMONA- Geomatics Engineer
Gemena, Sud-Ubangi, DRC - Candidate AMMI 2026
GitHub: Mputu96

## 🎯 Why AMMI?
I live in flood-prone region of Sud-Ubangi. I want to bring AI for humanitarian action in DRC. First Congolese from Equateur to use ML for flood prevention in Gemena & Ubangi Basin.

## 🔗 Dataset
Synthetic data inspired by real topography of Ubangi River Basin, Gemena.