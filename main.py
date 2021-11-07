'''
Instruction

Just Run: PS: py main.py
It will start downloading files and will remain automatically.
'''
print("\n")
download_no_of_images = int(input("Enter No of files you want to download: "))
print("\n")
import urllib.request
webUrl  = urllib.request.urlopen('https://www.enally.in/author.txt')
credit = webUrl.read()

#print ("" + str(webUrl.getcode()))

connection_status = (str(webUrl.getcode()))
if connection_status == "200":
    print("============================================")
    print("Connection Established Successfully!")
    print("============================================")
else:
    print("Error Code" + str(webUrl.getcode()))

import getpass
import main_script
import schedule
import time
import importlib



#x = datetime.datetime.now()

for i in range(download_no_of_images):
    schedule.run_pending()

    if i == 0:
        #importlib.reload(main_script)
        print(" ")
    else:
        importlib.reload(main_script)

    #main script call downloading function
    main_script.get_images_data()

    if i == download_no_of_images-1:
        print("\n===========================================================")
        print("  All Files Downloaded Successfully!",getpass.getuser(),)
        print (   credit  )
        print("===========================================================\n")


'''
This Project is developed by https://github.com/03prashantpk
'''