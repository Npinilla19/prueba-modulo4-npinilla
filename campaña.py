from error import LargoExcedidoException
from anuncio import Video, Display, Social


class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_data):
        if not nombre or len(nombre) > 250:
            raise LargoExcedidoException(
                "El nombre no puede estar vacío ni superar los 250 caracteres."
            )
        if fecha_termino <= fecha_inicio:
            raise ValueError(
                "La fecha de término debe ser posterior a la fecha de inicio."
            )
        if not anuncios_data:
            raise ValueError("La lista de anuncios no puede estar vacía.")
        if len(anuncios_data) > 1000:
            raise ValueError(
                "La lista de anuncios no puede contener más de 1000 anuncios."
            )

        self._nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios_data)

    def _crear_anuncios(self, anuncios_data):
        anuncios = []
        for anuncio_data in anuncios_data:
            anuncio = self._crear_anuncio(anuncio_data)
            anuncios.append(anuncio)
        return anuncios

    def _crear_anuncio(self, anuncio_data):
        formato = anuncio_data.pop("formato")
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
                "El nombre no puede superar los 250 caracteres."
            )
        self._nombre = value

    @property
    def anuncios(self):
        return self._anuncios

    def __str__(self):
        tipos = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self.anuncios:
            tipos[type(anuncio).__name__] += 1
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {tipos['Video']} Video, {tipos['Display']} Display, {tipos['Social']} Social"
