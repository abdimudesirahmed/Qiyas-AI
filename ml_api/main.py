from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib


# ==========================================
# Create FastAPI Application
# ==========================================

app = FastAPI(
    title="Oil Sales Prediction API",
    description="Predict value_sales using a trained multivariate regression model",
    version="1.0.0"
)


# ==========================================
# Load Model and Preprocessing Objects
# ==========================================

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("encoders.pkl")


# ==========================================
# Request Model
# ==========================================

class PredictionRequest(BaseModel):

    average_price: float
    volume_sales: float
    year: int
    month: int

    city: str
    manufacturer: str
    brand: str
    product_class: str
    price_bracket: str


# ==========================================
# Health Check
# ==========================================

@app.get("/")
def root():

    return {
        "message": "Oil Sales Prediction API is running"
    }


# ==========================================
# Prediction Endpoint
# ==========================================

@app.post("/predict")
def predict(request: PredictionRequest):

    try:

        # --------------------------------------
        # Convert request to dictionary
        # --------------------------------------

        data = {
            "average_price": request.average_price,
            "volume_sales": request.volume_sales,
            "year": request.year,
            "month": request.month,
            "city": request.city,
            "manufacturer": request.manufacturer,
            "brand": request.brand,
            "class": request.product_class,
            "price_bracket": request.price_bracket
        }


        # --------------------------------------
        # Encode categorical values
        # --------------------------------------

        categorical_cols = [
            "city",
            "manufacturer",
            "brand",
            "class",
            "price_bracket"
        ]


        for col in categorical_cols:

            encoder = label_encoders[col]

            try:

                data[col] = encoder.transform([data[col]])[0]

            except ValueError:

                raise HTTPException(
                    status_code=400,
                    detail=f"Unknown value '{data[col]}' for column '{col}'"
                )


        # --------------------------------------
        # Create DataFrame
        # --------------------------------------

        feature_cols = [
            "average_price",
            "volume_sales",
            "year",
            "month",
            "city",
            "manufacturer",
            "brand",
            "class",
            "price_bracket"
        ]


        input_df = pd.DataFrame(
            [data],
            columns=feature_cols
        )


        # --------------------------------------
        # Apply Scaling
        # --------------------------------------

        input_scaled = scaler.transform(input_df)


        # --------------------------------------
        # Make Prediction
        # --------------------------------------

        prediction = model.predict(input_scaled)


        return {
            "predicted_value_sales": float(prediction[0])
        }


    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )