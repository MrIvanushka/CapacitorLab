import pathlib
import shutil
import os
import requests

path = str(pathlib.Path().absolute()) + '\\Maps'
print(path)

try:
    shutil.rmtree(path)
except OSError:
    print ("Deletion of the directory %s failed" % path)
else:
    print ("Successfully deleted the directory %s" % path)

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)

# https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/2020/0906/AQUA_MODIS.20200906.L3m.DAY.SST.sst.4km.NRT.nc.png

Resolution = ['4km', '9km'] 

for key in Resolution:
    ResPath = path + '\\' + key
    try:
        os.mkdir(ResPath)
    except OSError:
        print ("Creation of the directory %s failed" % ResPath)
    else:
        print ("Successfully created the directory %s" % ResPath)

    for Day in range(31):
        name = str(Day) + '.png'
        if Day // 10:
            Day1 = str(Day)
        else:
            Day1 = '0' + str(Day)
        Website = 'https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/2020/09' + Day1 + '/AQUA_MODIS.202009' + Day1 + '.L3m.DAY.SST.sst.' + key + '.NRT.nc.png'
        r = requests.get(Website, allow_redirects = True)
        Etalon = requests.get("https://ru.stackoverflow.com/")
        if str(r) != '<Response [200]>':
            print ("The content of %s September doesn't exist" % Day)
        else:
            open(ResPath + '/' + name, 'wb').write(r.content)
            print(Website)
        
        
        