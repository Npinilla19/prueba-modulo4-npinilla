from error import LargoExcedidoException


class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_data):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = {"Video": 0, "Display": 0, "Social": 0}

    def _crear_anuncios(self, anuncios_data):
        pass

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) > 250:
            raise LargoExcedidoException(
                "se debe validar que el nuevo nombre no supere los 250 caracteres."
            )
        self._nombre = value

    @property
    def anuncions(self):
        return self._anuncios

    def __str__(self):
        pass
