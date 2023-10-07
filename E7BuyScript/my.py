import os
import cv2

file_path = r'C:\Users\Melli\Documents\GitHub\E7ShopScript\shop.PNG'

if not os.path.exists(file_path):
    print(f'File does not exist: {file_path}')
else:
    try:
        img = cv2.imread(file_path)
        if img is None:
            print(f'Failed to read image: {file_path}')
        else:
            print(f'Successfully read image: {file_path}')
    except Exception as e:
        print(f'Error reading image: {file_path}, error: {str(e)}')
