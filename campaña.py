class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_data):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios_data)
