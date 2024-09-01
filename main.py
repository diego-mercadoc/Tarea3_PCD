from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, conlist
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definición del modelo de usuario
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    user_id = Column(Integer, unique=True, index=True)
    user_email = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)
    recommendations = Column(JSON)
    ZIP = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

# Definición de Pydantic
class UserCreate(BaseModel):
    user_name: str
    user_id: int
    user_email: EmailStr
    age: Optional[int] = None
    recommendations: List[str]
    ZIP: Optional[str] = None

# Inicializar FastAPI
app = FastAPI()

# Crear un usuario
@app.post("/users/")
def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.user_email == user.user_email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Actualizar un usuario
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtener un usuario
@app.get("/users/{user_id}")
def read_user(user_id: int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

# Eliminar un usuario
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(db_user)
    db.commit()
    return {"detail": "Usuario eliminado"}
