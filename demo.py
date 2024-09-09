from campaña import Campaña
from anuncio import Video
from error import LargoExcedidoException, SubTipoInvalidoException


def main():

    video = Video(
        sub_tipo="instream",
        url_archivo="http://example.com/video.mp4",
        url_clic="http://example.com",
        duracion=30,
    )
    campaña = Campaña(
        nombre="Campaña Inicial",
        fecha_inicio="2024-09-01",
        fecha_termino="2024-09-30",
        anuncios_data=[video],
    )
    # Metodo crear anuncio
    campaña.crear_anuncio(video)
    print(campaña)

    print(f"El nombre actual es: {campaña.nombre}")
    print(f"El subtipo actual es: {video.sub_tipo}")

    try:
        nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
        campaña.nombre = nuevo_nombre

        nuevo_subtipo = input("Ingrese el nuevo subtipo de anuncio: ")
        video.sub_tipo = nuevo_subtipo

        print(
            f"el nuevo nombre es: {campaña.nombre}, el nuevo subtipo es: {video.sub_tipo}"
        )
    except (SubTipoInvalidoException, LargoExcedidoException) as e:
        with open("error.log", "a") as error_log:
            error_log.write(str(e) + "\n")
            print("Error:", e)


if __name__ == "__main__":
    main()
