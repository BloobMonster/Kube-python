import uvicorn
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from database.Database import engine, SessionLocal
from model.Models import Record as modelRecord, Base as modelBase
from schema.Schemas import Record as schemaRecord

modelBase.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/records/", response_model=List[schemaRecord])
def show_records(db: Session = Depends(get_db)):
    records = db.query(modelRecord).all()
    return records


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
