import os

# -----------------------------------------------------------
# ORIENTAÇÕES:
# - Estar instalado e configurado CLI AWS.
# - Utilizar apenas imagens do Landsat Collection 2 Level-1.
# - Diretorio: O download sera realizado em uma pasta com o nome da imagem, que será criada dentro do diretorio em que se encontra o script.
# - Nome da imagem: Certifique-se que a imagem seja Landsat Collection 2 Level-1. Exemplo de input: LC08_L1TP_221080_20201223_20210310_02_T1.
# - As bandas disponíveis são B1, B2, B3, B4, B5, B6, B7, B8, B9, B10. Informe quantas bandas deseja fazer o download, e em seguida insira cada banda por vez. Exemplo de input: B4.
# -----------------------------------------------------------

# Landsat ID
image_id = input('Insira o nome da imagem Landsat: ')

# Directory path
dir_path = f'{os.getcwd()}\{image_id}'

band_list = []

numBands = input('Insira quantas bandas deseja fazer download (Para baixar todas as bandas (B2-B8) digite 0): ')
if numBands == '0':
    band_list = ['B1','B2','B3', 'B4','B5','B6', 'B7','B8']
else:
    print('## ATENÇÃO: A banda deve ser composta por B maiusculo seguido do número da banda (Ex: B4). ##')
    for index in range(int(numBands)):
        band = input(f'Insira a {index+1} banda que deseja fazer download: ')
        band_list.append(band)

# - Start routine

image_split = image_id.split('_')

year = image_split[3][:4]
path = image_split[2][:3]
row = image_split[2][-3:]
collection = image_split[5]
level = image_split[1][1] 

def downloadImage():
    cmd = f'aws s3api get-object --bucket usgs-landsat --key collection{collection}/level-{level}/standard/oli-tirs/{year}/{path}/{row}/{image_id}/{image_id}_{band}.TIF  --request-payer requester {image_id}_{band}.TIF'
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        
    os.chdir(dir_path)
    if os.system(cmd) == 0 :
        os.system(cmd)
    else:
        print('Erro ao baixar imagem. Certifique-se que:\n- A imagem seja Landsat Collection 2 Level-1.\n- A banda foi descrita com B maisculo seguido do número (Ex.B4).')
        exit()
    
for band in band_list:
        downloadImage()
        print(f'Download da banda {band} realizado com sucesso.') 
           
# - End routine




