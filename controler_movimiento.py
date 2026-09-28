from fastapi import FastAPI
from consultas import *
from pydantic import BaseModel

app = FastAPI()

class ModelMovimiento(BaseModel):
    date:str
    concept:str
    quantity:float

@app.get("/movimientos",tags=['Movimiento'])
def index():
    return select_all()

@app.get("/movimientos/ingresos",tags=['Movimiento'])
def movimiento_ingresos():
    return mostrar_ingresos()

@app.get("/movimientos/gastos",tags=['Movimiento'])
def movimiento_gastos():
    return mostrar_gastos()  

@app.get("/movimientos/{id}",tags=['Movimiento'])
def movimiento_by_id(id:int):
    return select_by_id(id)

@app.post("/movimientos",tags=['Movimiento'])
def movimiento_registro(body:ModelMovimiento):
    try:
        insert_data( [body.date,body.concept,body.quantity] )
        return {'mensaje':'registro correcto'}

    except Exception as ex:
        print(ex)
        return {'error': 'ha fallado el registro'}

@app.put("/movimientos/{id}",tags=['Movimiento'])
def movimiento_update(id:int,body:ModelMovimiento):
    try:
        update_data(id,[body.date,body.concept,body.quantity])
        return {'mensaje':'actualizacion correcta'}
    except Exception as ex:
        print(ex)
        return {'error':'ha fallado la actualizacion'}

@app.delete("/movimientos/{id}",tags=['Movimiento'])
def movimiento_borrado(id:int):
    try:
        delete_data(id)
        return {'mensaje':'borrado correcto'}
    except Exception as ex:
        print(ex)
        return {'error':'ha fallado el borrado'} 