import os
import zipfile
import shutil
all = os.listdir("sample")
for file in all:
    print(file)

for root, folders, files in os.walk("sample"):
 for filename in files:
     if filename.endswith('.xlsx'):
      print("--", root, filename)

from shutil import copyfile

for root, folders, files in os.walk("sample"):
    for filename in files:
        if filename.endswith(".xlsx"):
            copyfile(root + "/" + filename, "Excel/" + filename)


# hutil.make_archive('python', 'zip', "sample")




# zip world -> file , anh -> file , gui email cho ai do
 # day 3 thu muc  , nen lai roi gui 