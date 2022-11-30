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

The ODK forms for collecting leaf images of Irish Potatoes and Common Beans are illustrated here below:

![forms](https://github.com/devdatanalytics/ai4afsmust/blob/main/img/odkforms.png)

## 2. Data Pre-processing
The code files used for initial data pre-processing include:

* [`download_files.py`](https://github.com/devdatanalytics/ai4afsmust/blob/main/dataCollection/download_imgfiles.py): used Google Drive Downloader to download the crop leaf images from URLs captured by ODK.
The leaf image is saved as a URL on Google sheet when the file is uploaded from the ODK form on the app.
For example, a file with URL `https://drive.google.com/open?id=1_vNgNDJxyh4QLe1vkoD0I34A-j8AU8jK` is downloaded to a file named `1_vNgNDJxyh4QLe1vkoD0I34A-j8AU8jK.jpg`

* [`rename_img.py`](https://github.com/devdatanalytics/ai4afsmust/blob/main/dataCollection/rename_img.py): used to rename files in a given folder in the format `classnameFilenumber.extension`. The code renames a file with name `1_vNgNDJxyh4QLe1vkoD0I34A-j8AU8jK.jpg` to `healthy25.jpg`. The code also produces a `.csv` file that tracks the new and old filenames. The format of the `csv` file is indicated below: 


| new_filename	| old_filename|
|--------------|--------------|
| healthy1.jpg	| 1jR4L3QMFN_wGes5NSpECjf819i4BLhxC |
| healthy2.jpg	| 1zIcpXRMPUf-KcPwI53ohi1QIRdxR9Kc7 |
| healthy3.jpg	| 1jEN6zBL_0RRMHanGRik54HK75GOhu1YF |
| .             |  . |
| .             |  . |
| .             |  . |
| healthy25.jpg |  1_vNgNDJxyh4QLe1vkoD0I34A-j8AU8jK |