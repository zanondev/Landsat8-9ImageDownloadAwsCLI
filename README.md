# Download landsat images with aws cli
Script to download landsat 8-9 images using aws cli


Guidelines:
- Be installed and configured AWS CLI.
- Use only Landsat 8-9 Collection 2 Level-1 images.
- Directory: The download will be carried out in a folder with the scene, which will be created within the directory where the script is located.
- Image name: Make sure the image is Landsat Collection 2 Level-1. Enter the images you want to download separated by space. Example input: LC08_L1TP_221080_20201223_20210310_02_T1.
- The available bands are B1, B2, B3, B4, B5, B6, B7, B8, B9, B10. Enter the bands you want to download separated by space. Input example: B4.

Run:
`python LandsatImageDownload.py`
