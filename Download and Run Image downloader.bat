@Echo OFF
Echo ==========================================
Echo       Developed by - Prashant Kumar
Echo ==========================================

pause

@echo off
git clone https://github.com/03prashantpk/Python-multiple-image-downloader.git

Echo OFF
Echo Press ENTER to Start Downloading Images...
pause

@echo off
python Python-multiple-image-downloader/main.py %*
pause