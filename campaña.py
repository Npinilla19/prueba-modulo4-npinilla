from error import LargoExcedidoException
from anuncio import Anuncio


class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_data):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios_data)

    def _crear_anuncios(self, anuncios_data):
        anuncios = []
        for anuncio_data in anuncios_data:
            anuncio = Anuncio(
                anuncio_data["ancho"],
                anuncio_data["alto"],
                anuncio_data["sub_tipo"],
                anuncio_data["url_archivo"],
                anuncio_data["url_clic"],
            )
            anuncios.append(anuncio)
        return anuncios

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
        for anuncio in self._anuncios:
            if anuncio.formato == "Video":
                tipos["Video"] += 1
            elif anuncio.formato == "Display":
                tipos["Display"] += 1
            elif anuncio.formato == "Social":
                tipos["Social"] += 1
        return (
            f"Nombre de la campaña: {self._nombre}\n"
            f"Anuncios: {tipos['Video']} Video, "
            f"{tipos['Display']} Display, "
            f"{tipos['Social']} Social"
        )
