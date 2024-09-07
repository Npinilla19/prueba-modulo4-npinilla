from error import LargoExcedidoException
from anuncio import Video, Display, Social


class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_data):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios_data)

    def _crear_anuncios(self, anuncios_data):
        anuncios = []
        for anuncio_data in anuncios_data:
            anuncio = self._crear_anuncio(
                anuncio_data
            )  # Método que crea el anuncio según el tipo
            anuncios.append(anuncio)
        return anuncios

    # por que no sale en el diagrama estos metodos debemos preguntar???pero la guía lo indica.
    def _crear_anuncio(self, anuncio_data):
        formato = anuncio_data.get("formato")
        if formato == "Video":
            return Video(**anuncio_data)
        elif formato == "Display":
            return Display(**anuncio_data)
        elif formato == "Social":
            return Social(**anuncio_data)
        else:
            raise ValueError("Formato de anuncio no reconocido")

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
        tipos = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self.anuncios:
            tipos[type(anuncio).__name__] += 1
        return f" Nombre de la campaña: {self.nombre} \n Anuncios: {tipos['Video']} Video, {tipos['Display']} Display, {tipos['Social']} Social"
