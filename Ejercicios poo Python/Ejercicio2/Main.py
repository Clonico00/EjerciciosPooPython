from Electrodomestico import Electrodomestico
from Lavadora import Lavadora
from Television import Television

electrodomestico = ()
electrodomestico = list(electrodomestico)

electrodomestico.insert(-1, Electrodomestico(consumoEnerguia="A", peso=20))
electrodomestico.insert(-1, Electrodomestico(consumoEnerguia="A", peso=40))
electrodomestico.insert(-1, Electrodomestico(consumoEnerguia="A", peso=60))
electrodomestico.insert(-1, Electrodomestico(consumoEnerguia="A", peso=80))

electrodomestico.insert(-1, Lavadora(consumoEnerguia="E", peso=50, carga=30))
electrodomestico.insert(-1, Lavadora(consumoEnerguia="A", peso=50, carga=60))

electrodomestico.insert(-1, Television(peso=20, resolucion=40))
electrodomestico.insert(-1, Television(peso=20, resolucion=80))

television = 0
lavadora = 0
electrodomestico = 0
i = 0

for electroc in electrodomestico:
    i += 1
    electroc.precioFinal()

    if isinstance(electroc, Television):
        television += electroc.precioBase
    elif isinstance(electroc, Lavadora):
        lavadora += electroc.precioBase
    else:
        electrodomestico += electroc.precioBase

print("Televisores totales " + repr(television))
print("Lavadoras totales " + repr(lavadora))
print("Electrodomesticos totales " + repr(electrodomestico))

print("Total de todo: " + repr(television + lavadora + electrodomestico))
