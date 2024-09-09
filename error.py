class SubTipoInvalidoException(Exception):
    """
    Excepción lanzada cuando el subtipo de un anuncio no es válido.
    """
    pass


class LargoExcedidoException(Exception):
    """
    Excepción lanzada cuando el nombre de la campaña excede los 250 caracteres.
    """
    pass
