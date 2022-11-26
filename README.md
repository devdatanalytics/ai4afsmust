## ai4afsmust
# Development of Machine Learning Models for Early Detection of Crop Diseases Based on Crop Imagery Data

This code base contains the code used in data collection and to pre-process leaf images that will be taken at small-scale crop farms in southern highlands of Tanzania. The two main crops are Common beans and Irish potatoes. 

The four classes of __Common beans__ are:
- Healthy (`healthy`)
- Bean rust (`rust`)
- Bean anthracnose (`anthra`) 
- Other (`other`)

The four classes of __Irish potatoes__ are: 
- Healthy (`healthy`)
- Early blight (`earlyblt`)
- Late blight (`lateblt`) 
- Other (`other`).


## 1. Data collection tool
The data collection tool is the Open Data Kit ([ODK](https://getodk.org/)) app on Android smartphones.
Data storage is on Google drive.  


## 2. Data Pre-processing
The code files used for initial data pre-processing include:

* [`download_files.py`](https://github.com/devdatanalytics/ai4afsmust/blob/main/dataCollection/download_imgfiles.py): used Google Drive Downloader to download fecal images dataset from URLs captured by ODK.


* [`rename_img.py`](https://github.com/devdatanalytics/ai4afsmust/blob/main/dataCollection/rename_img.py): used to rename files in a given folder in the format `classname.filenumber.extension` e.g. healthy25.jpg and produces a `.csv` file containing a list of new filename and old filename.