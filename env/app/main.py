import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# error cases

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
async def root():
    return {"Hello": "World"}


@app.put("/get/item/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/get/item/int/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
