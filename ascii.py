import subprocess
import time
import cv2
import numpy as np

#character sets
ascii_set = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\\\"^`\". "
set_2 = "Ñ@#W$9876543210?!abc;:+=-,._               "
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

cam = cv2.VideoCapture(0)
new_width = 150


def convert(gray, characters, resized):
    for row in resized:
        for pixel in row:
            k = int(np.floor(pixel / 256 * len(set_2)))
            characters += set_2[len(set_2) - 1 - k]

    count = len(characters)
    ascii_image = "\n".join([characters[index:(index + new_width)] for index in range(0, count, new_width)])
    return ascii_image


def main():
    while True:
        _, img = cam.read()
        characters = ""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape
        resized = cv2.resize(gray, (new_width, int(((h / w) * new_width * 0.5))))
        ascii_image = convert(gray, characters, resized)
        #for _ in range(number):
            #sys.stdout.write("\x1b[1A")
        print(ascii_image)

        time.sleep(1 / 60)
        #faster than os.system
        subprocess.Popen("cls", shell=True)


if __name__ == '__main__':
    main()
    