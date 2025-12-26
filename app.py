import sys
import os

import certifi

ca = certifi.where()

from dotenv import load_dotenv

load_dotenv()
mongo_db_url = os.getenv("MONGODB_URL_KEY")
print(mongo_db_url)
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request, Form
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from networksecurity.utils.main_utils.utils import load_object

from networksecurity.utils.ml_utils.model.estimator import NetworkModel


client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")


@app.get("/", tags=["authentication"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about")
async def about_route(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/how-it-works")
async def how_it_works_route(request: Request):
    return templates.TemplateResponse("how.html", {"request": request})


@app.get("/health")
async def health_route():
    return {"status": "healthy"}


@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


@app.post("/predict")
async def predict_route(request: Request, file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        # print(df)
        preprocesor = load_object("final_model/preprocessor.pkl")
        final_model = load_object("final_model/model.pkl")
        network_model = NetworkModel(preprocessor=preprocesor, model=final_model)
        # print(df.iloc[0])
        y_pred = network_model.predict(df)
        # print(y_pred)
        df["predicted_column"] = y_pred
        # print(df["predicted_column"])

        # Save output for reference (optional, keeping existing logic)
        df.to_csv("prediction_output/output.csv")

        # Convert to HTML table with styling
        table_html = df.to_html(
            classes="min-w-full divide-y divide-gray-200", index=False
        )

        return templates.TemplateResponse(
            "result.html", {"request": request, "table": table_html}
        )

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


# API Endpoint for programmatic access (Optional)
@app.post("/api/predict")
async def api_predict_route(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        preprocesor = load_object("final_model/preprocessor.pkl")
        final_model = load_object("final_model/model.pkl")
        network_model = NetworkModel(preprocessor=preprocesor, model=final_model)
        y_pred = network_model.predict(df)
        df["predicted_column"] = y_pred
        return df.to_dict(orient="records")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


@app.post("/predict-form")
async def predict_form_route(
    request: Request,
    having_IP_Address: int = Form(...),
    URL_Length: int = Form(...),
    Shortining_Service: int = Form(...),
    having_At_Symbol: int = Form(...),
    double_slash_redirecting: int = Form(...),
    Prefix_Suffix: int = Form(...),
    having_Sub_Domain: int = Form(...),
    SSLfinal_State: int = Form(...),
    Domain_registeration_length: int = Form(...),
    Favicon: int = Form(...),
    port: int = Form(...),
    HTTPS_token: int = Form(...),
    Request_URL: int = Form(...),
    URL_of_Anchor: int = Form(...),
    Links_in_tags: int = Form(...),
    SFH: int = Form(...),
    Submitting_to_email: int = Form(...),
    Abnormal_URL: int = Form(...),
    Redirect: int = Form(...),
    on_mouseover: int = Form(...),
    RightClick: int = Form(...),
    popUpWidnow: int = Form(...),
    Iframe: int = Form(...),
    age_of_domain: int = Form(...),
    DNSRecord: int = Form(...),
    web_traffic: int = Form(...),
    Page_Rank: int = Form(...),
    Google_Index: int = Form(...),
    Links_pointing_to_page: int = Form(...),
    Statistical_report: int = Form(...),
):
    try:
        # Create dictionary from form data
        data = {
            "having_IP_Address": [having_IP_Address],
            "URL_Length": [URL_Length],
            "Shortining_Service": [Shortining_Service],
            "having_At_Symbol": [having_At_Symbol],
            "double_slash_redirecting": [double_slash_redirecting],
            "Prefix_Suffix": [Prefix_Suffix],
            "having_Sub_Domain": [having_Sub_Domain],
            "SSLfinal_State": [SSLfinal_State],
            "Domain_registeration_length": [Domain_registeration_length],
            "Favicon": [Favicon],
            "port": [port],
            "HTTPS_token": [HTTPS_token],
            "Request_URL": [Request_URL],
            "URL_of_Anchor": [URL_of_Anchor],
            "Links_in_tags": [Links_in_tags],
            "SFH": [SFH],
            "Submitting_to_email": [Submitting_to_email],
            "Abnormal_URL": [Abnormal_URL],
            "Redirect": [Redirect],
            "on_mouseover": [on_mouseover],
            "RightClick": [RightClick],
            "popUpWidnow": [popUpWidnow],
            "Iframe": [Iframe],
            "age_of_domain": [age_of_domain],
            "DNSRecord": [DNSRecord],
            "web_traffic": [web_traffic],
            "Page_Rank": [Page_Rank],
            "Google_Index": [Google_Index],
            "Links_pointing_to_page": [Links_pointing_to_page],
            "Statistical_report": [Statistical_report],
        }

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Load artifacts
        preprocesor = load_object("final_model/preprocessor.pkl")
        final_model = load_object("final_model/model.pkl")
        network_model = NetworkModel(preprocessor=preprocesor, model=final_model)

        # Predict
        y_pred = network_model.predict(df)
        df["predicted_column"] = y_pred

        # Convert to HTML table with styling
        table_html = df.to_html(
            classes="min-w-full divide-y divide-gray-200", index=False
        )

        return templates.TemplateResponse(
            "result.html", {"request": request, "table": table_html}
        )

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8000)
