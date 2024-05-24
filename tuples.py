"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    coordenada = record[1]
    return coordenada



def convert_coordinate(coordinate):

    coord_separada = (coordinate[0],coordinate[1])
    return (coord_separada)

def create_record(azara_record, rui_record):
    
    a, b = azara_record
    c, d, e = rui_record  
    if convert_coordinate(b) == d:
        respuesta = azara_record + rui_record
        return respuesta
    else:
        return "not a match"

