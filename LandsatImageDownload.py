import os

# -----------------------------------------------------------
# v1.2.0
# - Guidelines:
# - Be installed and configured AWS CLI.
# - Use only Landsat 8-9 Collection 2 Level-1 images.
# - Directory: The download will be carried out in a folder with the scene, which will be created within the directory where the script is located.
# - Image name: Make sure the image is Landsat Collection 2 Level-1. Enter the images you want to download separated by space. Example input: LC08_L1TP_221080_20201223_20210310_02_T1.
# - The available bands are B1, B2, B3, B4, B5, B6, B7, B8, B9, B10. Enter the bands you want to download separated by space. Input example: B4.
# -----------------------------------------------------------

image_id = input('Insira o nome da imagem Landsat (para baixar multiplas imagens basta inserir separado por espaço): ')

id_split = image_id.split(' ')

band_list = []

numBands = input('Insira a banda desejada fazer download (para baixar multiplas bandas basta inserir separado por espaço). Ou digite 0 para baixar todas as bandas: ')
if numBands == '0':
    band_list = ['B1','B2','B3', 'B4','B5','B6', 'B7','B8']
else:
    bands_split = numBands.split(' ')
    for band in bands_split:
        band_list.append(band.upper())

# - Start routine

dir_path = os.path.dirname(os.path.abspath(__file__))

for imageId in id_split:

    image_split = imageId.split('_')

    satelite = image_split[0]
    year = image_split[3][:4]
    path = image_split[2][:3]
    row = image_split[2][-3:]
    collection = image_split[5]
    level = image_split[1][1] 

    # Directory path
    output_dir_name = f'{satelite}_{path}_{row}'
    output_dir_path = os.path.join(dir_path, output_dir_name)

    def downloadImage():
        cmd = f'aws s3api get-object --bucket usgs-landsat --key collection{collection}/level-{level}/standard/oli-tirs/{year}/{path}/{row}/{imageId}/{imageId}_{band}.TIF  --request-payer requester {imageId}_{band}.TIF'
        
        if not os.path.exists( output_dir_path):
            os.makedirs( output_dir_path)
            
        os.chdir( output_dir_path)
        if os.system(cmd) == 0 :
            os.system(cmd)
        else:
            print('Erro ao baixar imagem. Certifique-se que:\n- A imagem seja Landsat Collection 2 Level-1.\n- A banda foi descrita com B seguido do número (Ex.B4).')
            exit()
        
    for band in band_list:
            downloadImage()
            print(f'Download da banda {band} realizado com sucesso.') 
           
# - End routine




