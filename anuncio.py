from error import SubTipoInvalidoException

class Anuncio:

    def __init__(self, ancho, alto, sub_tipo, url_archivo, url_clic):
        self.ancho = ancho if ancho > 0 else 1
        self.alto = alto if ancho > 0 else 1
        self.sub_tipo = sub_tipo
        self.url_archivo = url_archivo
        self.url_clic = url_clic

# Getters y Setters 
@property
def sub_tipo(self):
    return self.sub_tipo

@sub_tipo.setter
def sub_tipo(self, value):
    if value not in self.sub_tipo:
        raise SubTipoInvalidoException(f"Subtipo {value} no permitido ")
    self.sub_tipo = value

@staticmethod
def mostrar_formato(value, subtipo):
    print (f"Formato: {value}, subtipo: {subtipo}")

class Video(Anuncio):
    def __init__(self,duracion):
        pass

