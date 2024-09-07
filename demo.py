from campaña import Campaña
from error import LargoExcedidoException, SubTipoInvalidoException


def main():
    anuncios_data = [
        {
            "formato": "Video",
            "sub_tipo": "instream",
            "url_archivo": "http://example.com/video.mp4",
            "url_clic": "http://example.com",
            "duracion": 30,
        }
    ]
    campaña = Campaña(
        nombre="Campaña Inicial",
        fecha_inicio="2024-09-01",
        fecha_termino="2024-09-30",
        anuncios_data=anuncios_data,
    )

    nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
    nuevo_sub_tipo = input(
        "Ingrese un nuevo sub_tipo para el anuncio (instream/outstream): "
    )

    try:
        campaña.nombre = nuevo_nombre
        campaña.anuncios[0].sub_tipo = nuevo_sub_tipo
    except (LargoExcedidoException, SubTipoInvalidoException) as e:
        with open("error.log", "a") as error_file:
            error_file.write(f"{str(e)}\n")
        print(f"Error: {str(e)}")

    print(campaña)


if __name__ == "__main__":
    main()
