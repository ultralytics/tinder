import os

import matplotlib.pyplot as plt
from skimage import io
from tqdm import tqdm

import features
import tinder_api

# Get tokens
host = 'https://api.gotinder.com'  # thanks to this line you do not need to import config.py or tinder_config_ex.py
fb_access_token = tinder_api.config.fb_access_token
fb_user_id = tinder_api.config.fb_user_id
tinder_api.get_auth_token(fb_access_token, fb_user_id)

# Get your profile photos
plotFlag = True
print('\nYour profile photos:')
myself = tinder_api.get_self()
for index, p in enumerate(myself['photos']):
    print(p['url'])
    img = io.imread(p['url'])[:, :, ::-1]
    if plotFlag:
        plt.figure(figsize=(12, 12)) if index == 0 else None
        plt.subplot(3, 3, index + 1).imshow(img[:, :, ::-1])
        plt.axis('off')

# Get your matches
match_info = features.get_match_info()

download_match_images = False
# Download all match images
if download_match_images:
    print('\nDownloading match images...')
    os.system('rm -rf data && mkdir data')
    for i in tqdm(range(len(match_info))):
        name = match_info[i]['name']
        photos = match_info[i]['photos']
        for j, photo in enumerate(photos):
            label = name + '_m' + str(i) + '_' + str(j)
            os.system('wget ' + photo + ' -q -O data/' + label + '.jpg')

exit()

# Get Tinder Recommendations of people around you
# recommendations = tinder_api.get_recommendations()
recommendations = tinder_api.get_recs_v2()

# select one recommended individual
testid = recommendations['data']['results'][0]['user']['_id']
print(testid)

# Retrieve profile from id
testperson = tinder_api.get_person(testid)
testperson

# Like a user
# tinder_api.like('5a10ae3c8802dc4401463712')

# message a match
tinder_api.send_msg('59ff7c30117d37c0572338d55a10ae3c8802dc4401463712', 'Hi, boy! Gloria Tinder-Robot here')
