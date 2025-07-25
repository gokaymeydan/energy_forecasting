import logging
from io import StringIO

import azure.functions as func
import joblib
import pandas as pd

from src.modelling import predict_lightgbm
from src.preprocessing import prepare_features

app = func.FunctionApp()


@app.blob_trigger(
    arg_name="myblob", path="input-data/{name}", connection="AzureWebJobsStorage"
)
@app.blob_output(
    arg_name="outputblob",
    path="output-data/{name}-prediction.csv",
    connection="AzureWebJobsStorage",
)
def forecast_from_blob(myblob: func.InputStream, outputblob: func.Out[str]):
    logging.info(f"Processing blob: {myblob.name}")

    csv_str = myblob.read().decode("utf-8")
    df = pd.read_csv(StringIO(csv_str))
    # prepare features
    df = prepare_features(df)
    # load model
    model = joblib.load("src/model.pkl")
    # do prediction
    predictions = predict_lightgbm(model, df)
    df["Prediction"] = predictions

    out_csv = df[["Datetime", "Prediction"]].to_csv(index=False)
    outputblob.set(out_csv)

    logging.info("Prediction written to output blob")
