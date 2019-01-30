import codecs as cd


class lecturaArchivo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = cd.open(self.nombre, "r")

    def obtenerInformacion(self):
        return self.archivo.readlines()

    def cerrarArchivo(self):
        self.archivo.close()
