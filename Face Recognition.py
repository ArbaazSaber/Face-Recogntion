import face_recognition as fr
import cv2 as cv
import os
import fnmatch
from PIL import Image

dir_path = 'D:/Face Recognition/New'
count = len(fnmatch.filter(os.listdir(dir_path), '*.*'))
count_face = 1

def encode_faces(folder):
    list_people_encoding = []
    
    for filename in os.listdir(folder):
        known_image = fr.load_image_file(f'{folder}{filename}')
        known_encoding = fr.face_encodings(known_image)[0]
        
        list_people_encoding.append((known_encoding, filename))
        
    return list_people_encoding

def find_target_faces():
    face_locations = fr.face_locations(target_image)
    print(face_locations)
    list_people_encoding = encode_faces('Known/')
    if not list_people_encoding:
        for location in face_locations:
            save_face_(location)
    
    for person in list_people_encoding:
        encoded_face = person[0]
        filename = person[1]
        
        is_target_face = fr.compare_faces(encoded_face, target_encoding, tolerance=0.6)
        print(f'{is_target_face} {filename}')
        if face_locations:
            
            face_number = 0
            for location in face_locations:
                if is_target_face[face_number]:
                    label = filename
                    # save_face_(location)
                    create_frame(location, label)
                    
                face_number+=1
    
def save_face_(location):
    top, right, bottom, left = location
    
    im1 = org_img.crop((left, top, right, bottom))
    im1.save("Known/Face.jpg")
    # count_face = count_face + 1

# This function is for Demonstration purposes only

def create_frame(location, label):
    top, right, bottom, left = location
    
    cv.rectangle(target_image, (left, top), (right, bottom), (255,0,0), 2)
    cv.rectangle(target_image, (left, bottom+20), (right, bottom), (255,0,0), cv.FILLED)
    cv.putText(target_image, label, (left+3,bottom+14), cv.FONT_HERSHEY_DUPLEX, 0.4, (255,255,255), 1)

def render_image():
    rgb_img = cv.cvtColor(target_image, cv.COLOR_BGR2RGB)
    cv.imshow('Face Recognition', rgb_img)
    
    cv.waitKey(0)
    
for i in range(1,15):
    load_image  = f"New/Frame " + str(i) + ".jpg"
    print(load_image)
    org_img = Image.open(load_image)
    target_image = fr.load_image_file(load_image)
    target_encoding = fr.face_encodings(target_image)
    
    if target_encoding:    
        find_target_faces()
        render_image()