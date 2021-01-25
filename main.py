import lib.image_collector as ic
import lib.arg_handler as ah
import lib.image_manipulator as im
import sys

def main():
    img_files = ic.fetch_from_web()
    im.create_comic(img_files)


if __name__ == "__main__":
    main()