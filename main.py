'''
Instruction

Just Run: PS: py main.py
It will start downloading files and will remain automatically.
'''

download_no_of_images = int(input("Enter No of files you want to download: "))

import main_script
import schedule
import time
import importlib

for i in range(download_no_of_images):
    schedule.run_pending()
    #time.sleep(1)
    importlib.reload(main_script)
    #time.sleep(1)
    main_script.get_images_data()
  

'''
This Project is developed by https://github.com/03prashantpk
'''