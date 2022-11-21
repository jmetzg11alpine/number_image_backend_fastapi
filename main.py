from fastapi import FastAPI
from deta import Deta
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


class Data(BaseModel):
    number: str
    data: list = []


# class Number(BaseModel):
#     data: list = []


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

deta = Deta('a0499p4s_aP4D8LBstFNj8tujRmuz6vGdVMYfBRB5')
numbers_db = deta.Base('numbers')


@app.get('/')
def get_model():
    return {'gretting': 'hi donkey', 'message': 'this backend is just used to upload training data'}


# @app.post('/prediction')
# def make_prediction(number: Number):
#     response = number.dict()
#     data = np.array(response['data'])
#     data = data.reshape((-1, 28, 28))
#     data = np.expand_dims(data, -1)
#     predictions = model.predict(data)
#     prediction = np.argmax(predictions)
#     return {'prediction': int(prediction)}


# used to load the data
@app.post('/')
def q1_post(data: Data):
    response = data.dict()
    numbers_db.insert({'number': response['number'], 'data': response['data']})
    return {"message": f"number: {response['number']} was added"}
