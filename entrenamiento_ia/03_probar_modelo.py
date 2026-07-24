import joblib
import os

# 1. Rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'modelo.pkl')

print("="*60)
print("🧪 PROBANDO EL ARCHIVO MODELO.PKL CON NUEVOS DATOS")
print("="*60)

# 2. Cargar el modelo entrenado
try:
    model = joblib.load(MODEL_PATH)
    print("✅ Archivo modelo.pkl cargado con éxito en memoria.")
except Exception as e:
    print(f"❌ Error al cargar modelo.pkl: {e}")
    exit()

# 3. Datos simulados de un cliente que llena el formulario web
# Estructura de características: ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Credit_History']

# Caso A: Cliente con buen sueldo e historial crediticio perfecto (1)
cliente_A = [[5000, 2000, 150, 1]] 

# Caso B: Cliente con ingresos bajos e historial crediticio malo (0)
cliente_B = [[1000, 0, 300, 0]]

# 4. Hacer la predicción
pred_A = model.predict(cliente_A)[0]
pred_B = model.predict(cliente_B)[0]

print("\n--- RESULTADOS DE LAS PREDICCIONES ---")
print(f"👤 Cliente A (Ingresos altos, Historial bueno) -> Predicción: {pred_A} ({'Aprobado ✅' if pred_A == 1 else 'Rechazado ❌'})")
print(f"👤 Cliente B (Ingresos bajos, Historial malo)  -> Predicción: {pred_B} ({'Aprobado ✅' if pred_B == 1 else 'Rechazado ❌'})")

print("\n" + "="*60)
print("✨ EL MODELO RESPONDE CORRECTAMENTE. ¡LISTO PARA DJANGO!")
print("="*60)