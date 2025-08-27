import pickle

import sklearn
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fogml.generators import GeneratorFactory

import argparse

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'FogML as a Service API'}

@app.get('/environment')
def ml_environment():
    return {'scikit-learn': sklearn.__version__}

@app.post("/convert/pickle")
async def convert_pickle(request: Request):
    try:
        # Read binary body
        body = await request.body()

        # Deserialize the scikit-learn model
        model = pickle.loads(body)

        # Generate the source-code of the model
        factory = GeneratorFactory()
        generator = factory.get_generator(model)
        generator.generate(fname="response.c")

        # Read generated file
        with open("response.c", "rb") as f:
            file_content = f.read()

        # Return generated source-code
        return JSONResponse(content={
            "status": "success",
            "model": str(file_content)
        })

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Script that adds 3 numbers from CMD"
    )
    parser.add_argument("--port", required=True, type=int, default=8000, help="Please provide port number")
    args = parser.parse_args()

    uvicorn.run(app, host='0.0.0.0', port=args.port)