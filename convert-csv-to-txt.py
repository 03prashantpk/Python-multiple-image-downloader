import pandas as pd

read_file = pd.read_csv (r'book4.csv')
read_file.to_csv (r'med_images.txt', index=None)