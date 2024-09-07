from error import SubTipoInvalidoException


class Anuncio:
    def __init__(self, ancho, alto, sub_tipo, url_archivo, url_clic):
        self.ancho = ancho if ancho > 0 else 1
        self.alto = alto if alto > 0 else 1
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self._url_archivo = value

    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        self._url_clic = value

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoException(f"Subtipo {value} no permitido")
        self._sub_tipo = value

    @staticmethod
    def mostrar_formato():
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
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, sub_tipo, url_archivo, url_clic, duracion):
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
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        self._duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
