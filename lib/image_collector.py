from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import lib.webdriver_config as wd
import time
from random import choice
import base64
import requests
import os
import shutil

tmp_folder = 'tmp/'

def fetch_from_web(amnt=2):
    purge_tmp()
    filenames = []
    for i in range(0,amnt):
        img_req = requests.get("https://thispersondoesnotexist.com/image", stream=True)
        filename = f"tmp/img_{i}.jpg"
        with open(filename,"wb") as imgfile:
            imgfile.write(img_req.content)
        filenames.append(filename)
        if i<amnt:
            time.sleep(2)
    return filenames

def purge_tmp():
    file_path = None
    for filename in os.listdir(tmp_folder):
        file_path = os.path.join(tmp_folder, filename)
    if file_path is None: return
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
