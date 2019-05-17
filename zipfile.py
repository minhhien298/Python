import os
import zipfile

fantasy_zip = zipfile.ZipFile('./input/home-data-for-ml-course/melb_dataABC.zip', 'w')

for folder, subfolders, files in os.walk('./input/melbourne-housing-snapshot/'):

    for file in files:
        if file.endswith('.csv'):
            fantasy_zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), './input/melbourne-housing-snapshot/'),
                              compress_type=zipfile.ZIP_DEFLATED)

fantasy_zip.close()
