import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Definir rutas de archivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, 'credit_risk.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'modelo.pkl')

print("="*60)
print("🤖 [PASO 4] ENTRENAMIENTO DEL MODELO DE INTELIGENCIA ARTIFICIAL")
print("="*60)

# 2. Cargar y Preprocesar los datos
df = pd.read_csv(DATASET_PATH)

# Aplicar encoding (mismos mapeos numéricos)
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Married'] = df['Married'].map({'Yes': 1, 'No': 0})
df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

# 3. Separar Características (X) y la Variable Objetivo (y)
# Seleccionamos las columnas que usará el usuario en la web
features = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Credit_History']
X = df[features]
y = df['Loan_Status']

print(f"\n📊 Variables de entrada para el modelo: {features}")
print(f"🎯 Variable a predecir: Loan_Status (1 = Aprobado, 0 = Rechazado)")

# 4. Dividir datos en Entrenamiento y Prueba (80% / 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Entrenar el Algoritmo (Random Forest Classifier)
print("\n⚙️ Entrenando el modelo...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluar la precisión
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n--- RESULTADOS DE LA EVALUACIÓN ---")
print(f"🎯 Exactitud (Accuracy) del Modelo: {accuracy * 100:.2f}%")

# 7. Exportar el Modelo a .pkl con Joblib
joblib.dump(model, MODEL_PATH)

print("\n" + "="*60)
print(f"📦 ¡ÉXITO TOTAL! Modelo guardado dinámicamente en:")
print(f"   --> {MODEL_PATH}")
print("="*60)