
import urllib.request
req = urllib.request.Request('https://www.induna.com/uploaded_images/dvd_vcd_master/medium/02_06_58_0_Bollywood_DVD_Bluray_AudioCD.jpg')
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)