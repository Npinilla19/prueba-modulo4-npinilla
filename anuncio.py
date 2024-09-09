from error import SubTipoInvalidoException


class Anuncio:
    """
    Clase base para representar un anuncio.

    Atributos:
        ancho (int): El ancho del anuncio.
        alto (int): El alto del anuncio.
        sub_tipo (str): El subtipo del anuncio.
        url_archivo (str): La URL del archivo del anuncio.
        url_clic (str): La URL de clic del anuncio.

    Métodos:
        mostrar_formato(): Muestra los formatos y subtipos disponibles.
    """
    def __init__(self, ancho, alto, sub_tipo, url_archivo, url_clic):
        """
        Inicializa una instancia de la clase Anuncio.

        Args:
            ancho (int): El ancho del anuncio.
            alto (int): El alto del anuncio.
            sub_tipo (str): El subtipo del anuncio.
            url_archivo (str): La URL del archivo del anuncio.
            url_clic (str): La URL de clic del anuncio.
        """
        self.ancho = ancho if ancho > 0 else 1
        self.alto = alto if alto > 0 else 1
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def url_archivo(self):
        """Obtiene la URL del archivo del anuncio."""
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        """Establece la URL del archivo del anuncio."""
        self._url_archivo = value

    @property
    def url_clic(self):
        """Obtiene la URL de clic del anuncio."""
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        """Establece la URL de clic del anuncio."""
        self._url_clic = value

    @property
    def sub_tipo(self):
        """Obtiene el subtipo del anuncio."""
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        """
        Establece el subtipo del anuncio.

        Args:
            value (str): El subtipo del anuncio.

        Raises:
            SubTipoInvalidoException: Si el subtipo no es permitido.
        """
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoException(f"Subtipo {value} no permitido")
        self._sub_tipo = value

    @staticmethod
    def mostrar_formato():
        """Muestra los formatos y subtipos disponibles."""
        formatos = {
            "Video": Video.SUB_TIPOS,
            "Display": Display.SUB_TIPOS,
            "Social": Social.SUB_TIPOS,
        }
        for formato, subtipos in formatos.items():
            print(f"FORMATO: {formato}")
            for subtipo in subtipos:
                print(f" - Subtipo: {subtipo}")


class Video(Anuncio):
    """
    Clase para representar un anuncio de video.

    Atributos:
        FORMATO (str): El formato del anuncio.
        SUB_TIPOS (tuple): Los subtipos permitidos para el formato.
        duracion (int): La duración del video en segundos.

    Métodos:
        comprimir_anuncio(): Comprime el anuncio de video.
        redimensionar_anuncio(): Redimensiona el anuncio de video.
    """
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, sub_tipo, url_archivo, url_clic, duracion):
        """
        Inicializa una instancia de la clase Video.

        Args:
            sub_tipo (str): El subtipo del anuncio de video.
            url_archivo (str): La URL del archivo del anuncio.
            url_clic (str): La URL de clic del anuncio.
            duracion (int): La duración del video en segundos.
        """
        super().__init__(
            ancho=1,
            alto=1,
            sub_tipo=sub_tipo,
            url_archivo=url_archivo,
            url_clic=url_clic,
        )
        self.duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        """Obtiene la duración del video en segundos."""
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        """Establece la duración del video en segundos."""
        self._duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        """Comprime el anuncio de video."""
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Redimensiona el anuncio de video."""
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    """
    Clase para representar un anuncio de display.

    Atributos:
        FORMATO (str): El formato del anuncio.
        SUB_TIPOS (tuple): Los subtipos permitidos para el formato.

    Métodos:
        comprimir_anuncio(): Comprime el anuncio de display.
        redimensionar_anuncio(): Redimensiona el anuncio de display.
    """
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        """Comprime el anuncio de display."""
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Redimensiona el anuncio de display."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    """
    Clase para representar un anuncio de redes sociales.

    Atributos:
        FORMATO (str): El formato del anuncio.
        SUB_TIPOS (tuple): Los subtipos permitidos para el formato.

    Métodos:
        comprimir_anuncio(): Comprime el anuncio de redes sociales.
        redimensionar_anuncio(): Redimensiona el anuncio de redes sociales.
    """
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        """Comprime el anuncio de redes sociales."""
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Redimensiona el anuncio de redes sociales."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
