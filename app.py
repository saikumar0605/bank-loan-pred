import sys
from fastapi import FastAPI, Request
from typing import Optional
from uvicorn import run as app_run
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.exception import CustomException

from src.utils.MainUtils import MainUtils

from src.components.model_predictor import LoanstatusPredictor, bankData
from src.constant import APP_HOST, APP_PORT

from src.pipline.train_pipeline import TrainPipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.Gender: Optional[str] = None
        self.Married: Optional[str] = None
        self.Depender: Optional[str] = None
        self.Education: Optional[str] = None
        self.Self_Employed: Optional[str] = None
        self.Applicantincome: Optional[str] = None
        self.Coapplicantincome: Optional[str] = None
        self.LoanAmount: Optional[str] = None
        self.Loan_Amount_Term: Optional[str] = None
        self.Credit_History: Optional[str] = None
        self.Property_Area: Optional[str] = None
        self.Loan_Status: Optional[str] = None
        

    async def get_bank_data(self):
        form =  await self.request.form()
        self.Gender = form.get("Gender")
        self.Married = form.get("Married")
        self.Depender = form.get("Depender")
        self.Education = form.get("Education")
        self.Self_Employed = form.get("Self_Employed")
        self.Applicantincome = form.get("Applicantincome")
        self.Coapplicantincome = form.get("Coapplicantincome")
        self.LoanAmount = form.get("LoanAmount")
        self.Loan_Amount_Term = form.get("Loan_Amount_Term")
        self.Credit_History = form.get("Credit_History")
        self.Property_Area = form.get("Property_Area")
        self.Loan_Status = form.get("Loan_Status")

#changes required below..
@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.get("/predict")
async def predictGetRouteClient(request: Request):
    try:
        utils = MainUtils()

        return templates.TemplateResponse(
            "bank.html",{"request": request, "context": "Rendering"})

    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predictRouteClient(request: Request):
    try:
        # utils = MainUtils()
        # bankData = utils.get_Bank_list()
        form = DataForm(request)
        await form.get_bank_data()
        
        bankdata = bankData(Gender= form.Gender, 
                                   Married= form.Married, 
                                   Depender= form.Depender, 
                                   Education= form.Education, 
                                   Self_Employed= form.Self_Employed, 
                                   Applicantincome= form.Applicantincome, 
                                   Coapplicantincome= form.Coapplicantincome,
                                   LoanAmount= form.LoanAmount,
                                   Loan_Amount_Term = form.Loan_Amount_Term,
                                   Credit_History = form.Credit_History
                                   )
        
        src_df = bankdata.get_bankdata_input_data_frame()
        src_predictor = LoanstatusPredictor()
        src_value = round(src_predictor.predict(X=src_df)[0], 2)

        return templates.TemplateResponse(
            "bank.html",
            {"request": request, "context": src_value}
        )

    except Exception as e:
        raise CustomException(e,sys) from e

if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)