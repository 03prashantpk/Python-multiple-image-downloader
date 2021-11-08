'''
Instruction
Just Run: PS: py main.py
It will start downloading files and will remain automatically.
'''
import time
import getpass
import schedule
import importlib
import urllib.request
import progressbar

def animated_marker():
      
    widgets = ['Testing your Internet Connection... ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)

print("\n")
download_no_of_images = int(input("Enter No of files you want to download: "))

webUrl  = urllib.request.urlopen('https://www.enally.in/author.txt')
credit = webUrl.read()

for x in range(0):
    if x == 0:
        print("\n")
        print("============================================")
        print(animated_marker())
        print("============================================")
        print("\n")
        time.sleep(1)
    else:
        print("")
    

#print ("" + str(webUrl.getcode()))

connection_status = (str(webUrl.getcode()))
if connection_status == "200":
    print("============================================")
    print("   Connection Established Successfully!")
    print("============================================")
else:
    print("Error Code" + str(webUrl.getcode()))

import main_script

#x = datetime.datetime.now()

i = 1

for i in range(download_no_of_images):
    schedule.run_pending()

    if i == 0:
        #importlib.reload(main_script)
        print(" ")
    else:
        importlib.reload(main_script)

    #main script call downloading function
    main_script.get_images_data()

    
    percenteage = (((i+1) / download_no_of_images) * 100)
    print("=======================================================")
    print("             %.0f"%percenteage,"% Completed")
    print("=======================================================")

    if i == download_no_of_images-1:
        print("\n===========================================================")
        print("  All Files Downloaded Successfully!",getpass.getuser(),)
        print (   credit  )
        print("===========================================================\n")


'''
This Project is developed by https://github.com/03prashantpk
'''