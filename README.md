# LandsatImageDownloadAwsCLI
Script to download landsat 8-9 images using aws cli


ORIENTAÇÕES:
- Estar instalado e configurado CLI AWS.
- Utilizar apenas imagens do Landsat 8-9 Collection 2 Level-1.
- Diretorio: O download sera realizado em uma pasta com o nome da imagem, que será criada dentro do diretorio em que se encontra o script.
- Nome da imagem: Certifique-se que a imagem seja Landsat Collection 2 Level-1. Exemplo de input: LC08_L1TP_221080_20201223_20210310_02_T1.
- As bandas disponíveis são B1, B2, B3, B4, B5, B6, B7, B8, B9, B10. Informe quantas bandas deseja fazer o download, e em seguida insira cada banda por vez. Exemplo de input: B4.

RUN:
`python LandsatImageDownload.py`
