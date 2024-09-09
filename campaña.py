from error import LargoExcedidoException
from anuncio import Video, Display, Social


class Campaña:
    """
    Clase para representar una campaña publicitaria.

    Atributos:
        nombre (str): El nombre de la campaña.
        fecha_inicio (datetime): La fecha de inicio de la campaña.
        fecha_termino (datetime): La fecha de término de la campaña.
        anuncios (dict): Un diccionario que contiene listas de anuncios por tipo.

    Métodos:
        crear_anuncio(anuncio): Añade un anuncio a la campaña.
    """
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_data):
        """
        Inicializa una instancia de la clase Campaña.

        Args:
            nombre (str): El nombre de la campaña.
            fecha_inicio (datetime): La fecha de inicio de la campaña.
            fecha_termino (datetime): La fecha de término de la campaña.
            anuncios_data (list): Una lista de datos de anuncios.

        Raises:
            LargoExcedidoException: Si el nombre está vacío o supera los 250 caracteres.
            ValueError: Si la fecha de término es anterior o igual a la fecha de inicio.
            ValueError: Si la lista de anuncios está vacía o contiene más de 1000 anuncios.
        """
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
        """
        Añade un anuncio a la campaña.

        Args:
            anuncio (Anuncio): Una instancia de la clase Anuncio (o sus subclases).

        Raises:
            ValueError: Si el tipo de anuncio no es válido.
        """
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
        """Obtiene el nombre de la campaña."""
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """
        Establece el nombre de la campaña.

        Args:
            value (str): El nombre de la campaña.

        Raises:
            LargoExcedidoException: Si el nombre supera los 250 caracteres.
        """
        if len(value) > 250:
            raise LargoExcedidoException(
                "El nombre no puede superar los 250 caracteres."
            )
        self._nombre = value

    @property
    def anuncios(self):
        """Obtiene el diccionario de anuncios de la campaña."""
        return self._anuncios

    def __str__(self):
        """
        Representa la instancia de la clase Campaña como una cadena de texto.

        Returns:
            str: Una cadena que describe la campaña y el número de anuncios por tipo.
        """
        video_count = len(self.anuncios["Video"])
        display_count = len(self.anuncios["Display"])
        social_count = len(self.anuncios["Social"])
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {video_count} Video, {display_count} Display, {social_count} Social"
