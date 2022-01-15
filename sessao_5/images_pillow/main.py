import os
from PIL import Image

def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe')
    for root, dirs, files in os.walk((main_images_folder)):
        for file in files:
            caminho_completo = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            converted_tag = 'CONVERTED'

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            #
            # if converted_tag in caminho_completo:
            #     os.remove(caminho_completo)
            #
            # continue
            if os.path.isfile(caminho_completo):
                print(f'Arquivos {new_file_full_path} já existe')
                continue

            #verifica se contem o no 'CONVERTED isso significa que a imagem já foi convertida
            if converted_tag in caminho_completo:
                print('Imagem já convertida')
                continue


            img_pillow = Image.open(caminho_completo)

            # pega a data da foto
            # data_tirada = img_pillow._getexif()
            # print(data_tirada[36867])



            width, height = img_pillow.size
            new_height = round(new_width * height / width)

            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS

            )

            new_image.save(
                new_file_full_path,
                optimize = True,
                quality = 70
                # manter as informações das imagens
                # exif=img_pillow.info['exif']


            )

            print(f'{caminho_completo} convertido com sucesso!')
            new_image.close()

            """
            width         height
            new_width     ??
            """

            img_pillow.close()

            # apaga todos os arquivos antigos, originais
            # os.remove(caminho_completo)

if __name__ =='__main__':
    main_images_folder = r'C:\Users\Mestre\Downloads\images'
    main(main_images_folder, new_width=6000)