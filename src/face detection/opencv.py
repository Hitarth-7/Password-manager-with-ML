import cv2
import os
import face_recognition
import pickle

def create_folder(directory_name):
    if os.path.exists(directory_name):
        for file in os.listdir(directory_name):
            file_to_remove = os.path.join(directory_name, file)
            os.remove(file_to_remove)
        os.rmdir(directory_name)

    os.mkdir(directory_name)


def get_user_image(username):
    # Opening webcam
    cap = cv2.VideoCapture(0)

    # Initalising classifiers
    face_cascade = cv2.CascadeClassifier('src/models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('src/models/haarcascade_eye.xml')

    # Creating output directory
    output_directory = "public/user_images"
    create_folder(output_directory)

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detecting faces and eyes
        faces_rect = face_cascade.detectMultiScale(gray_img, scaleFactor=2.0, minNeighbors=5)
        eyes_rect = eye_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=9)
        
        # If one pair of face and eyes are detected then that user's image will be saved
        if len(faces_rect) == 1 and len(eyes_rect) == 1:
            image_path = f"{output_directory}/{username}.jpg"
            cv2.imwrite(image_path, frame)
            break

        cv2.imshow("Webcam Window", frame)


    cap.release()
    cv2.destroyAllWindows()
    
    return image_path


def convert_to_encodings(image_path):

    known_encodings = []
    known_names = []

    image = face_recognition.load_image_file(image_path)

    name = os.path.split(image)[0]

    face_encodings = face_recognition.face_encodings(image)

    for encoding in face_encodings:
        known_encodings.append(encoding)
        known_names.append(name)

    data = {"encodings": known_encodings, "name": known_names}

    with open("public/encodings/face_encodings.pickle", "wb") as file:
        pickle.dump(data, file)



if __name__ == "__main__":
    image_path = get_user_image("Pranjal Mantri")
    convert_to_encodings(image_path)
