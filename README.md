# ⚡ Energy Consumption Forecasting App

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live-brightgreen?logo=streamlit)](https://energyforecasting-aajwzyuo4hckc78xuhuznx.streamlit.app/)

This Streamlit application predicts hourly electricity usage based on time-based features (hour, day, weekday, and month) using a trained LightGBM model.

---

## 🌐 Live Demo

👉 Try it here: [https://gokaymeydan-energy-forecasting.streamlit.app](https://energyforecasting-aajwzyuo4hckc78xuhuznx.streamlit.app/)

---

## 📂 Project Structure

```
energy_forecasting/
├── app/
│   └── app.py                 # Streamlit app entry point
├── src/
│   ├── init.py                # Makes src a module
│   ├── modelling.py           # Model loading logic
│   └── preprocessing.py       # Data loading and preprocessing
├── outputs/                   # Model evaluation results and prediction outputs
├── data/                      
├── requirements.txt           # Required packages
└── README.md                  # Project overview
```

---

## 🚀 How to Run the App

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/energy_forecasting.git
cd energy_forecasting
```

2. **(Optional) Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run app/app.py
```

---

## 📈 Outputs

After making predictions or evaluating the model, results will be saved under the `outputs/` folder:

- `prediction_plot.png` – Real vs Predicted plot
- `metrics.txt` – MAE and RMSE values
- `predictions.csv` – Result of the selected datetime prediction
- `train_results.csv` – Full dataset predictions

---

## 🤖 Model

- Model: `LightGBMRegressor`
- Features: `hour`, `day`, `weekday`, `month`
- Trained in: `notebooks/` or previously saved as `model.pkl`

---

## 🧩 Requirements

streamlit
pandas
numpy
matplotlib
scikit-learn
lightgbm