from timeit import default_timer as timer
import requests
import re
import lxml
import json
import urllib.request
import urllib.request
from bs4 import BeautifulSoup
import datetime
import os
import time
import getpass

# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://www.enally.in/author.txt')

image_url_test  = urllib.request.urlopen('https://www.enally.in/author.txt')

#get the result code and print it
#print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
#print (data)


#----- Global Variable -----#
x = datetime.datetime.now()
FOLDER = 'images/'
totalFiles = 0
totalDir = 0

for base, dirs, files in os.walk(FOLDER):
    #print('Searching in : ',base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1


#print('Total number of files',totalFiles)
#print('Total Number of directories',totalDir)
#print('Total:',(totalDir + totalFiles))

# open file in read mode (Read total lines)
with open(r"med_images.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
total_to_download = count + 1

total_images = totalDir + totalFiles
#time.sleep(1)
print("\nTotal No of Remaining files:",total_to_download - total_images )
print("Total Number of downloads:", total_images)


# Reading Lines from txt files
myfile = open("med_images.txt", "r")
myline = myfile.readline()
items = myline
print("\nSearching for: ",items)


####---- Image folder and More Naming
folder = "images/"
count_total_image = total_images # Count total image to increment name by +1
image_id = 158630  # if want to add number with text
name_prefix = "EMD"
name_suffix = image_id + (count_total_image+1)

# Final Name will be {name_prefix + name_suffix}


start = timer()
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "q": items,
    "tbm": "isch",
    "hl": "en",
    "ijn": "0",
}

html = requests.get("https://www.google.com/search",params=params, headers=headers)
soup = BeautifulSoup(html.text, 'lxml')

def get_images_data():

    #------------- Get Metadata Title and Link ----------------------#
    #print('\nGoogle Images Metadata:')
    for index in range(0, 1):
        for google_image in soup.select('.isv-r.PNCib.MSM1fd.BUooTd'):
            title = google_image.select_one(
                '.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')['title']
            source = google_image.select_one('.fxgdke').text
            link = google_image.select_one(
                '.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')['href']

            # print(f'{title}\n{source}\n{link}\n')

            # this steps could be refactored to a more compact
            all_script_tags = soup.select('script')

            # -Link 1
            matched_images_data = ''.join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))

            # "Expecting property name enclosed in double quotes"
            matched_images_data_fix = json.dumps(matched_images_data)
            matched_images_data_json = json.loads(matched_images_data_fix)

            # -Link 2
            matched_google_image_data = re.findall(
                r'\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",', matched_images_data_json)

            # -Link 3
            matched_google_images_thumbnails = ', '.join(re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',str(matched_google_image_data))).split(', ')



    #------------- Get Google Image Thumbnails links ----------------------#
    # print('Google Image Thumbnails:')  # in order
    for index in range(0, 1):
        for fixed_google_image_thumbnail in matched_google_images_thumbnails:

            # -Link 4
            google_image_thumbnail_not_fixed = bytes(
                fixed_google_image_thumbnail, 'ascii').decode('unicode-escape')

            # after first decoding, Unicode characters are still present. After the second iteration, they were decoded.
            google_image_thumbnail = bytes(google_image_thumbnail_not_fixed, 'ascii').decode('unicode-escape')

            # print(google_image_thumbnail)

            # removing previously matched thumbnails for easier full resolution image matches.
            removed_matched_google_images_thumbnails = re.sub(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', '', str(matched_google_image_data))

            # -Link 5 #-Link 6
            matched_google_full_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]", removed_matched_google_images_thumbnails)



    #------------- Get Full Resolution Images links ----------------------#
    print('\nImage Link:')  # in order
    for index in range(0, 1):
        for index, fixed_full_res_image in enumerate(matched_google_full_resolution_images):
            
            # -Link 7
            original_size_img_not_fixed = bytes( fixed_full_res_image, 'ascii').decode('unicode-escape')

            original_size_img = bytes(original_size_img_not_fixed, 'ascii').decode('unicode-escape')
            
            # This loop is used to download single image only.
            for images_download in range(0, 1):

                # Printing Downloadable "Full Resolution Images" Links
                print(original_size_img)


                #----- Download original images ----------
                for index in range(0, 1):
                    print(f'\nDownloading image no {total_images+1}')
                    opener = urllib.request.build_opener()
                    opener.addheaders = [
                        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
                    urllib.request.install_opener(opener)

                    
                    
                    
                    urllib.request.urlretrieve(original_size_img, f'{folder}{name_prefix}{name_suffix}.jpg')
                                                                # "image/product_336.jpg"   Dry Run By Prashant Kumar
                                                                # "image/EMD158630.jpg"     Dry Run By Prashant Kumar

                    # list to store file lines
                    lines = []
                    # read file
                    with open(r"med_images.txt", 'r') as fp:
                        # read an store all lines into list
                        lines = fp.readlines()

                    # Write file
                    print("Please wait finishing...")
                    with open(r"med_images.txt", 'w') as fp:
                        # iterate each line
                        for number, line in enumerate(lines):
                            # delete line 0. or pass any Nth line you want to remove
                            # note list index starts from 0
                            if number not in [0]:
                                fp.write(line)
                    #time.sleep(1)
                    print("\n################################")
                    print("\nCompleted Successfully!",getpass.getuser(),"\n")
                    print("################################\n")

                    print("===================================")
                    print ("\n",data,"\n")
                    print("===================================\n\n")

                    # if 5+5 == 10:
                    #     alpha.loop()
                    #     print("True")
                    
                    
                
            break


end = timer()
second = "s"
print("Searching time:", round(end - start,2),second)


#------------------------------- Refrence Links -------------------------------#
'''
Refrence Links mentioned above also

GitHub Clone Link: git clone https://github.com/03prashantpk/Python-multiple-image-downloader

Created by - Prashant Kumar
'''


