import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    dudi1 = reconhece_face("./img/dudi.jpg") #lembre de mudar o nome do arquivo no seu pc  -> dudi vai aki
    if(dudi1[0]):
        rostos_conhecidos.append(dudi1[1][0])
        nomes_dos_rostos.append("Dudi")

    gabriel1 = reconhece_face("./img/gabriel.jpg") #lembre de mudar o nome do arquivo no seu pc  -> gabriel vai aki
    if(gabriel1[0]):
        rostos_conhecidos.append(gabriel1[1][0])
        nomes_dos_rostos.append("Gabriel")
    
    return rostos_conhecidos, nomes_dos_rostos