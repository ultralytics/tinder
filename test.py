import tinder_api
import fb_auth_token
import features
import os

host = 'https://api.gotinder.com'  # thanks to this line you do not need to import config.py or tinder_config_ex.py

# Enter your facebook email
fb_username = 'glenn.jocher@gmail.com'
# Enter your facebook password
fb_password = ''

# fb_access_token = fb_auth_token.get_fb_access_token(fb_username, fb_password)
# fb_user_id = fb_auth_token.get_fb_id(fb_access_token)
fb_access_token = tinder_api.config.fb_access_token
fb_user_id = tinder_api.config.fb_user_id

tinder_api.get_auth_token(fb_access_token, fb_user_id)

print(fb_access_token)
print(fb_user_id)

myself = tinder_api.get_self()
for p in myself['photos']:
    print(p['url'])

# Get your matches
match_info = features.get_match_info()

# # Download all match images
# os.system('rm -rf data && mkdir data')
# for i in range(len(match_info)):
#     name = match_info[i]['name']
#     photos = match_info[i]['photos']
#     for j, photo in enumerate(photos):
#         label = name + '_m' + str(i) + '_' + str(j)
#         os.system('wget ' + photo + ' -O data/' + label + '.jpg')
#         print(photos[j])


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
