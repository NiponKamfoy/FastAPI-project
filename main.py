from fastapi import FastAPI,Header
from typing import Union
import uvicorn, json
from pydantic import BaseModel
from nc_json import convert_nc_json
from fastapi.middleware.cors import CORSMiddleware

f = open(r'token.json')
data = json.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*'],
 
)
@app.get('/get_index/{data_index}&{p_name}&{date}&{index_folder}')
def getGridSpei(data_index: str, index_folder: str, p_name: str, date:str = '2006-01', x_access_token: Union[list[str], None] = Header(default=None)):
    test = data['key']
    if (x_access_token != None and x_access_token[0] == data['key']):
        temp = convert_nc_json(p_name, date, data_index, index_folder)
        # response = jsonify(temp)
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return temp
    return x_access_token == data['key']
        

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1", port=8000)