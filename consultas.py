from conexion import Conexion
import sqlite3


def formato(respuesta):
    lista_final=[]
    for fila in respuesta.fetchall():
        lista_final.append(dict(fila))
    return lista_final    

def select_all():
    conexionSelect = Conexion('SELECT * FROM movimiento;')
    respuesta = conexionSelect.res
    resp = formato(respuesta)
    conexionSelect.con.close()
    return resp

def select_by_id(id:int):
    conexionSelectBy = Conexion(f'SELECT * FROM movimiento WHERE id={id}')
    respuesta=conexionSelectBy.res
    resp = formato(respuesta)
    conexionSelectBy.con.close()
    return resp

def insert_data(data):
    try:
        conexionInsert=Conexion('INSERT INTO movimiento(date,concept,quantity) VALUES (?,?,?);',data)
        conexionInsert.res
        conexionInsert.con.commit()#para confirmar guardado
    except sqlite3.Error as error:
        print('Error: ',error)

    conexionInsert.con.close()

def update_data(id,data):
    try:
        conexionUpdate=Conexion(f'UPDATE movimiento SET date=?,concept=?,quantity=? WHERE id={id};',data)
        conexionUpdate.res
        conexionUpdate.con.commit()#confirmar el update
    except sqlite3.Error as error:
            print('Error: ',error)
    conexionUpdate.con.close()

def delete_data(id:int):
    try:
        conexionDelete=Conexion(f'DELETE FROM movimiento WHERE id={id};')
        conexionDelete.res
        conexionDelete.con.commit()#confirmar el borrado
    except sqlite3.Error as error:
        print('Error: ',error)    
    conexionDelete.con.close() 

def mostrar_ingresos():
    conexionIngreso = Conexion('SELECT sum(quantity) FROM movimiento WHERE quantity>0;')
    respuesta = conexionIngreso.res.fetchone()
    conexionIngreso.con.close()
    if respuesta and respuesta[0] is not None:
        valor = respuesta[0]
    else:
        valor = 0
    return str(valor)

def mostrar_gastos():
    conexionGasto = Conexion('SELECT sum(quantity) FROM movimiento WHERE quantity<0;')
    respuesta = conexionGasto.res.fetchone()
    conexionGasto.con.close()
    if respuesta and respuesta[0] is not None:
        valor = respuesta[0]
    else:
        valor = 0
    return str(valor)