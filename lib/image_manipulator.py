import subprocess
import os
from PIL import Image as image
import lib.dialog_creator as dg

def crop_images(imgs):
    for img in imgs:
        with image.open(img,"r") as imgfile:
            width, height = imgfile.size
            if width >= height:
                width = height
            else:
                height = width 
            subprocess.run(["mogrify","-crop", f"{width}x{height}+0+0",img])

def create_comic(filenames):
    img1 = ""
    img2 = ""
    if len(filenames) >= 2:
        img1 = filenames[0]
        img2 = filenames[1]
    else:
        return "Too few images"
    horizontal_mirror(img2)
    dialog_strings = dg.generate_comic_dialog()
    panels = [img1, img2, img1, img2]
    panels = attach_dialog_to_panels(dialog_strings, panels)
    final_img = join_comic_panels(panels)
    attach_watermark("vainskynetjutut <3", final_img)


def horizontal_mirror(img):
    if os.path.isfile(img):
        subprocess.run(["mogrify","-flop", img])
    else:
        print(f"Nothing to mirror, the path {img} contains no file.")

def attach_dialog_to_panels(dialog, panels):
    filenames = []
    if len(dialog) != len(panels):
        return f"MISMATCH! {len(dialog)} dialog strings, but {len(panels)} panels"
    for i in range(0, len(dialog)):
        filenames.append(attach_single_dialog_string(dialog[i], panels[i], f"tmp/final_{i}.jpg"))
    return filenames

def attach_single_dialog_string(d_string, panel, filename):
    subprocess.run(["convert", panel, "-gravity", "north", "-stroke", "#000C", "-strokewidth", "10", "-font", "courier", "-pointsize", "80", "-annotate", "+0+52", d_string, "-stroke",  "none", "-fill", "white", "-annotate", "+0+50", d_string, filename])
    return filename

def join_comic_panels(panels):
    filename = "results/finalcomic.png"
    if len(panels) < 4:
        return "too few panels"
    subprocess.run(["montage", panels[0], panels[1], panels[2], panels[3], "-geometry", "+2+2", filename])
    return filename

def attach_watermark(d_string, filename):
    subprocess.run(["convert", filename, "-gravity", "southeast", "-stroke", "#000C", "-strokewidth", "3", "-font", "courier", "-pointsize", "40", "-annotate", "-35+0", d_string, "-stroke",  "none", "-fill", "white", "-annotate", "-35+0", d_string, filename])