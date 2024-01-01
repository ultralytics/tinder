import glob
import os
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from tqdm import tqdm

import features
import tinder_api

# Get tokens
host = "https://api.gotinder.com"  # thanks to this line you do not need to import config.py or tinder_config_ex.py
fb_access_token = tinder_api.config.fb_access_token
fb_user_id = tinder_api.config.fb_user_id
tinder_api.get_auth_token(fb_access_token, fb_user_id)

# Create user directory
user_dir = "data/" + features.config.fb_username.split("@")[0] + "/"
os.system("rm -rf " + user_dir + " && mkdir " + user_dir)
print("\nCreated User Directory: " + user_dir)

# Get your profile photos
plotFlag = False
print("\nYour profile photos:")
myself = tinder_api.get_self()
for index, p in enumerate(myself["photos"]):
    print(p["url"])
    if plotFlag:
        img = io.imread(p["url"])[:, :, ::-1]
        plt.figure(figsize=(12, 12)) if index == 0 else None
        plt.subplot(3, 3, index + 1).imshow(img[:, :, ::-1])
        plt.axis("off")

# Get your matches
match_info = features.get_match_info()

# Download all match images
download_match_images = True
if download_match_images:
    print("\nDownloading match images...")
    match_dir = user_dir + "match_images/"
    yolo_dir = user_dir + "match_images_yolo/"
    crop_dir = user_dir + "match_images_crop/"

    os.makedirs(match_dir)
    os.makedirs(crop_dir)

    n = 5  # len(match_info)
    for i in tqdm(range(n)):
        name = match_info[i]["name"]
        photos = match_info[i]["photos"]
        for j, photo in enumerate(photos):
            label = name + "_m" + str(i) + "_" + str(j)
            os.system("wget " + photo + " -q -O " + match_dir + label + ".jpg")

    # Pass images through yolov3
    print("\nAnalyzing match images with YOLOv3...")
    sys.path.append("../yolov3")
    import detect as detect

    detect.opt.conf_thres = 0.60
    detect.opt.image_folder = sys.path[0] + "/" + match_dir
    detect.opt.output_folder = sys.path[0] + "/" + yolo_dir
    detect.opt.txt_out = True
    detect.main(detect.opt)

    # Remove images of none or multiple people
    txt_files = sorted(glob.glob("%s/*.txt" % yolo_dir))
    for txt_file in txt_files:
        labels = np.loadtxt(txt_file, dtype=np.float32).reshape(-1, 6)
        labels = labels[labels[:, 4] == 0]

        if labels.shape[0] == 1:  # if only 1 person in image
            img_name = txt_file[:-4].split("/")[-1]
            box = labels[0].astype("int")
            h, w = box[3] - box[1], box[2] - box[0]
            area = w * h

            if (w > 150) and (h > 150) and (area > 30e3):
                img = cv2.imread(match_dir + img_name)
                cv2.imwrite(crop_dir + img_name, img[box[1] : box[3], box[0] : box[2]])

exit()

# Get Tinder Recommendations of people around you
# recommendations = tinder_api.get_recommendations()
recommendations = tinder_api.get_recs_v2()

# select one recommended individual
testid = recommendations["data"]["results"][0]["user"]["_id"]
print(testid)

# Retrieve profile from id
testperson = tinder_api.get_person(testid)
testperson

# Like a user
# tinder_api.like('5a10ae3c8802dc4401463712')

# message a match
tinder_api.send_msg("59ff7c30117d37c0572338d55a10ae3c8802dc4401463712", "Hi, boy! Gloria Tinder-Robot here")
