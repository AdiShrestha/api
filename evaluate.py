import pickle
from clean import clean
with open('english_model.pkl', 'rb') as file:
    CV_pipe, CV, LR1 = pickle.load(file)

def evaluate(text: str):
    cleaned_text = clean(text)
    transformed_text = CV.transform([cleaned_text])
    prediction = LR1.predict(transformed_text)

    if prediction[0] == 1:
        return True
    else:
        return False