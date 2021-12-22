import requests # request img from web
import shutil # save img locally

url = input('Please enter an image URL (string):') #prompt user for img url
file_name = input('Save image as (string):') #prompt user for file_name

res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')
