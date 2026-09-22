"""
UBANGI FLOOD PREDICT - AMMI Portfolio 2026
Prédiction inondations Gemena / Ubangi Sud-Ubangi RDC
Auteur: Ir Victor Lengena Semin
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. Données simulées (niveau rivière Ubangi + pluviométrie)
print("🌊 Projet Ubangi Flood Predict - Chargement données...")
np.random.seed(42)
days = 365*3
rain = np.random.gamma(2, 15, days) # mm/jour
river_level = 300 + np.cumsum(rain*0.05 - 2) + np.random.normal(0,10,days)
river_level = np.clip(river_level, 250, 650) # cm

df = pd.DataFrame({
    'rainfall': rain,
    'river_level': river_level,
    'rain_3d': pd.Series(rain).rolling(3).mean().fillna(0),
    'rain_7d': pd.Series(rain).rolling(7).mean().fillna(0)
})
df['next_day_level'] = df['river_level'].shift(-1).fillna(method='ffill')

# 2. Modèle
X = df[['rainfall','rain_3d','rain_7d','river_level']]
y = df['next_day_level']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
mae = mean_absolute_error(y_test, pred)

print(f"✅ Modèle entraîné - MAE: {mae:.2f} cm")
print(f"Exemple: Pluie aujourd'hui 45mm, niveau 520cm -> Demain prédit: {model.predict([[45,30,25,520]])[0]:.1f} cm")

# Alerte
threshold = 580
if pred[-1] > threshold:
    print(f"🚨 ALERTE INONDATION Gemena! Niveau prévu {pred[-1]:.0f}cm > {threshold}cm")
else:
    print(f"✅ Pas d'alerte - Niveau prévu {pred[-1]:.0f}cm")