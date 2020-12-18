import csv

from clientes.modelos import Cliente

class ClienteServicios:

    def __init__(self, tabla_nombre):
        self.tabla_nombre = tabla_nombre

    def cliente_crear(self, cliente):
        with open(self.tabla_nombre, mode='a') as f:
            escritor = csv.DictWriter(f, fieldnames=Cliente.esquema())
            escritor.writerow( cliente.to_dict() )
