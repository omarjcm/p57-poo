import uuid

class Cliente:
    def __init__(self, nombre, empresa, correo, posicion, uid=None):
        self.name = name
        self.empresa = empresa
        self.correo = correo
        self.posicion = posicion
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)

    @staticmethod
    def esquema():
        return ['nombre', 'empresa', 'correo', 'posicion', 'uid']