class persona(object):

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def setEdad(self, edad):
        self.edad = int(edad)

    def getEdad(self):
        return self.edad

    def __str__(self):
        return "%s %s %d" % (self.getNombre(), self.getApellido(), self.getEdad())
