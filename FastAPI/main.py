#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field  #Field igual a Body, Query y Path pero está directamente realcionada a Pydantic

#FastAPI
from fastapi import FastAPI         #FastAPI trabaja sobre Pydantic
from fastapi import Body, Query, Path

app = FastAPI()

#Models
class HairColor (Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str  
    state: str 
    country: str 

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=1,
        le=115
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)
    

#Path operation decorator. Utiliza el método get que viene de la instancia app.
@app.get('/')
def home():         #Path function
    return {'Hello': 'World'}

#Request and Response Body
@app.post('/person/new') # post es un método que se utiliza cuando el cliente envía a la pág web
def create_person(person: Person = Body (...)): # El "..." significa que ese parámetro es obligatorio
    return person

#Validations: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,   #valido que el nombre tenga entre 1 y 50 caracteres
        max_length=50,
        title= 'Person Name',
        description= 'This is the person name between 1 and 50 characters'
        ), 
    age: Optional[str] = Query(
        ...,
        title='Person Age',
        description="This is the person age. It's requiered"
        )
):
    return {name: age}


# Validations: Path Parameters
@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title=" Person ID",
        description="It's the description of Person ID")
):
    return {person_id: 'It exists!'}

# Validations: Request Body
@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(
        ...,
        title= 'Person ID',
        description= 'This is a Person ID',
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results