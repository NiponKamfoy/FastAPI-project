from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {'data': {'name': 'nipon'}}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1", port=8000)