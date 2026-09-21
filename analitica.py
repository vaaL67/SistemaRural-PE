# Programacion Funcional con lambdas y map/filter
def filtrar_citas_programadas(citas):
    return list(filter(lambda c: c['estado'] == 'PROGRAMADA', citas))

def calcular_total_copagos(citas):
    from functools import reduce
    return reduce(lambda acc, c: acc + c['costo'], citas, 0.0)
