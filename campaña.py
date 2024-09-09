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
        self._anuncios = {
            "Video": [],
            "Display": [],
            "Social": [],
        }

    def crear_anuncio(self, anuncio):
        if isinstance(anuncio, Video):
            self.anuncios["Video"].append(anuncio)
        elif isinstance(anuncio, Display):
            self.anuncios["Display"].append(anuncio)
        elif isinstance(anuncio, Social):
            self.anuncios["Social"].append(anuncio)
        else:
            raise ValueError("Tipo de anuncio no válido.")

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
        video_count = len(self.anuncios["Video"])
        display_count = len(self.anuncios["Display"])
        social_count = len(self.anuncios["Social"])
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {video_count} Video, {display_count} Display, {social_count} Social"
