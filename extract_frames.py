import os
import cv2

os.mkdir('frames')

counter = 0
for file in os.listdir("videos"):
    folder = 'frames/' + str(counter)
    counter += 1

    os.mkdir(folder)
    vidcap = cv2.VideoCapture('videos/' + file)
    count = 0
    while True:
        success,image = vidcap.read()
        if not success:
            break
        if (count % 12) == 0:
            cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
        count += 1
    print("{} images are extacted in {}.".format(count,folder))