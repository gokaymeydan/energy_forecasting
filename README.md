# Energy Consumption Forecasting App

This application predicts hourly electricity usage based on time-based features such as hour, day, weekday, and month using a trained LightGBM model. The data used for training was sourced from an individual household’s energy consumption dataset available on the UCI Machine Learning Repository.

---

## Live Demo    

Access the application on Hugging Face Spaces:  
[https://huggingface.co/spaces/gokaymeydan/energy-forecasting](https://huggingface.co/spaces/gokaymeydan/energy-forecasting)

---

## How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/energy_forecasting.git
cd energy_forecasting
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```


## Output Files

After running predictions, results are saved to the `outputs/` folder:

- `prediction_plot.png` – Plot of actual vs predicted values
- `metrics.txt` – Evaluation metrics (MAE, RMSE)
- `predictions.csv` – Prediction result based on selected datetime
- `train_results.csv` – Model predictions on the training set



## Model Performance & Business Impact
To justify the model complexity, I established a baseline using Linear Regression.

* **Baseline (Linear Regression):** MAE: 0.585 | RMSE: 0.720
* **Champion Model (LightGBM):** MAE: 0.440 | RMSE: 0.603
* **Result:** The LightGBM model reduced the Mean Absolute Error (MAE) by **~25%**, significantly improving the accuracy of peak consumption forecasts compared to the linear baseline.