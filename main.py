# File: app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import uvicorn

# Define the input data model
class TextInput(BaseModel):
    text: str

# Load the pre-trained model
model = joblib.load('english_model.pkl')

# Create a FastAPI instance
app = FastAPI()

@app.post("/predict")
async def predict(input: TextInput):
    text = input.text
    try:
        # Assuming your model expects a list of strings as input
        prediction = model.predict([text])
        result = "offensive" if prediction[0] == 1 else "not offensive"
        return {"text": text, "prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
