from PIL import Image
import face_recognition
import os

cdir = 'frames'
os.mkdir('images')

counter = 0
for video in os.listdir(cdir):
    best_image = None

    biggest_x = 0
    biggest_y = 0

    for filename in os.listdir(cdir + '/' + video):
        fn = cdir + '/' + video + '/' + filename

        print('Next image: {}', fn)

        # Load the jpg file into a numpy array
        image = face_recognition.load_image_file(fn)

        face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0)

        print("I found {} face(s) in this photograph.".format(len(face_locations)))

        for face_location in face_locations:

            # Print the location of each face in this image
            top, right, bottom, left = face_location
            print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

            x = right - left
            y = bottom - top

            if x > biggest_x and y > biggest_y:
                print("bigger face found")

                biggest_x = x
                biggest_y = y

                # You can access the actual face itself like this:
                best_image = image[top:bottom, left:right]

    if best_image is not None:
        pil_image = Image.fromarray(best_image).resize((32, 32)).resize((150, 150))
        pil_image.save('images/' + video + ".jpg")