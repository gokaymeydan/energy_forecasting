import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import matplotlib.pyplot as plt
from datetime import datetime, date, time
from src.modelling import load_model
from src.preprocessing import load_and_preprocess
from sklearn.metrics import mean_absolute_error, mean_squared_error

os.makedirs("outputs", exist_ok=True)

st.set_page_config(page_title="Energy Forecasting App", layout="wide")
st.title("⚡ Energy Consumption Forecasting App")
st.markdown("Predict hourly electricity usage based on date and time features using a LightGBM model.")

model = load_model()
df, X, y = load_and_preprocess()

st.sidebar.header("📆 Select a Date & Time")

selected_date = st.sidebar.date_input("Select a date", date(2009, 1, 1))
selected_time = st.sidebar.time_input("Select an hour", time(14, 0))

dt = datetime.combine(selected_date, selected_time)
input_features = pd.DataFrame({
    "hour": [dt.hour],
    "day": [dt.day],
    "weekday": [dt.weekday()],
    "month": [dt.month]
})
input_features=input_features[model.feature_name_]

prediction = None

if st.sidebar.button("Predict"):
    prediction = model.predict(input_features)[0]
    st.sidebar.success(f"🔋 Estimated Power: {prediction:.2f} kW")

st.subheader("📊 Model Evaluation (on all data)")
y_pred = model.predict(X)

results_df = pd.DataFrame({
    'actual': y,
    'predicted': y_pred
}).dropna()

mae = None
rmse = None

if results_df.empty:
    st.warning("No valid rows for MAE/RMSE calculation (data may contain all NaNs).")
else:
    mae = mean_absolute_error(results_df['actual'], results_df['predicted'])
    rmse = np.sqrt(mean_squared_error(results_df['actual'], results_df['predicted']))

    col1, col2 = st.columns(2)
    col1.metric("Mean Absolute Error", f"{mae:.3f} kW")
    col2.metric("Root Mean Squared Error", f"{rmse:.3f} kW")

plot_df = df.copy()
plot_df['prediction'] = y_pred
plot_df = plot_df[-168:]

if prediction is not None:
    output_df = input_features.copy()
    output_df["predicted_power_kW"] = prediction
    output_df.to_csv("outputs/predictions.csv", index = False)
else:
    st.warning("No prediction to save - button not clicked yet.")

with open("outputs/metrics.txt","w") as f:
    f.write(f"MAE: {mae:.3f}\nRMSE:{rmse:.3f}\n")

X.to_csv("outputs/input_features.csv")
results_df.to_csv("outputs/train_results.csv",index=False)

plt.figure(figsize=(10,5))
plt.plot(plot_df.index, plot_df['Global_active_power'], label="Actual")
plt.plot(plot_df.index, plot_df['prediction'], label="Predicted")
plt.legend()
plt.title("Real vs Predicted Power Usage (Last 168 hours)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/prediction_plot.png")
plt.close()

with open("outputs/model_version.txt", "w") as f:
    f.write("Model: LightGBM\n")
    f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

st.subheader("Real vs Predicted (Last 168 hours)")
st.line_chart(plot_df[['Global_active_power','prediction']].rename(columns={
    'Global_active_power': 'Actual',
    'prediction': 'Predicted'
}))