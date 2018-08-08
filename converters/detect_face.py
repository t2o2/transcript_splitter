from os import listdir
from os.path import isfile, join
from PIL import Image
import face_recognition
import re


frame_folder = 'frames'
frame_files = [f for f in listdir(frame_folder) if isfile(join(frame_folder, f))]

for frame in frame_files:
    match = re.match('frame_(?P<id>\d+)s\.png', frame)
    if not match:
        print('Error frame file not found: {}'.format(frame))
        continue
    frame_id = match.groups('id')[0]
    image = face_recognition.load_image_file(join(frame_folder, frame))
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
    print("Frame {}s has {} face(s).".format(frame_id, len(face_locations)))

    # Extract all faces within a frame
    frame_face_count = 0
    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save('faces/face_{}s_{}.jpg'.format(frame_id, frame_face_count))
        frame_face_count += 1
