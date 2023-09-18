# LandsatImageDownloadAwsCLI
Script to download landsat 8-9 images using aws cli


ORIENTAÇÕES:
- Estar instalado e configurado CLI AWS. (contate um membro do time de tecnologia para auxilio).
- Utilizar apenas imagens do Landsat 8-9 Collection 2 Level-1.
- Diretorio: O download sera realizado em uma pasta com a scene, que será criada dentro do diretorio em que se encontra o script.
- Nome da imagem: Certifique-se que a imagem seja Landsat Collection 2 Level-1. Informe as imagens que deseja fazer download separadas por espaço. Exemplo de input: LC08_L1TP_221080_20201223_20210310_02_T1.
- As bandas disponíveis são B1, B2, B3, B4, B5, B6, B7, B8, B9, B10. Informe as bandas que deseja fazer download separadas por espaço. Exemplo de input: B4.

Run:
`python LandsatImageDownload.py`
