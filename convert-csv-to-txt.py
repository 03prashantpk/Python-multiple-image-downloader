import pandas as pd

read_file = pd.read_csv (r'med_img.xlsx')
read_file.to_csv (r'med_images.txt', index=None)