import os
from datetime import date, datetime, time

import pandas as pd
import streamlit as st

from src.modelling import load_model

st.set_page_config(page_title="Energy Forecasting App", layout="wide")
st.title("Energy Consumption Forecasting App")
st.markdown(
    "Predict hourly electricity usage based on date and time features using a LightGBM model."
)

model = load_model()

st.sidebar.header("Select a Date & Time")

selected_date = st.sidebar.date_input(
    "Select a date",
    value=date.today(),
    min_value=date(2009, 1, 1),
    max_value=date(2030, 12, 31),
)
selected_time = st.sidebar.time_input("Select an hour", time(14, 0))

dt = datetime.combine(selected_date, selected_time)

st.info(
    "The predictions are based on a house located in Sceaux (7km of Paris, France) between December 2006 and November 2010."
)

future_dates = pd.date_range(start=dt, periods=168, freq="h")
future_df = pd.DataFrame({"Datetime": future_dates})
future_df["hour"] = future_df["Datetime"].dt.hour
future_df["day"] = future_df["Datetime"].dt.day
future_df["weekday"] = future_df["Datetime"].dt.weekday
future_df["month"] = future_df["Datetime"].dt.month
X = future_df[["hour", "day", "weekday", "month"]]

if st.sidebar.button("Predict"):
    predictions = model.predict(X)
    future_df["Prediction"] = predictions
    st.success("Prediction completed successfully.")
else:
    future_df = pd.DataFrame()

if not future_df.empty:
    st.subheader("Predicted Power Usage (Next 7 days)")
    st.line_chart(
        future_df.set_index("Datetime")["Prediction"].rename("Predicted Power (kW)")
    )
