import pandas as pd
import os

# 1. Obtener la ruta del dataset de forma dinámica
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, 'credit_risk.csv')

print("="*60)
print("🚀 [PASO 3] ANÁLISIS EXPLORATORIO Y LIMPIEZA DE DATOS")
print("="*60)

# 2. Cargar el dataset
if not os.path.exists(DATASET_PATH):
    print(f"❌ Error: No se encuentra el archivo {DATASET_PATH}")
    exit()

df = pd.read_csv(DATASET_PATH)

print("\n--- 1. Datos crudos (Primeras 3 filas) ---")
print(df.head(3))

# 3. Preprocesamiento: Convertir variables de texto a numéricas (Encoding)
print("\n--- 2. Aplicando Encoding (Texto -> Números) ---")

# Mapeos directos para que las categorías sean números claros
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Married'] = df['Married'].map({'Yes': 1, 'No': 0})
df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})  # 1 = Aprobado, 0 = Rechazado

print("✅ Mapeo completado.")

print("\n--- 3. Dataset Preprocesado (Listo para la IA) ---")
print(df.head(3))

print("\n--- 4. Verificación de Nulos y Tipos de Datos ---")
print(df.info())

print("\n" + "="*60)
print("✨ Limpieza completada. Datos listos para entrenamiento.")
print("="*60)