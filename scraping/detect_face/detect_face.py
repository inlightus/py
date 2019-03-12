import os, glob
import cv2

names = [name.split("/")[1] for name in glob.glob("data/*")]

out_dir = "./facedata/"
os.makedirs(out_dir, exist_ok=True)

for name in names:
    images = glob.glob("./data/" + name + "/*.jpg")

    os.makedirs(out_dir + name, exist_ok=True)

    for i, image in enumerate(images):
        image = cv2.imread(image)
        if image is None:
            print("Can't open the image: ", i)
            continue
        image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")

        face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=2, minSize=(64, 64))
        
        if len(face_list) > 0:
            for rect in face_list:
                x, y, width, hegiht = rect
                image = image[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
                if image.shape[0] < 64:
                    continue
                image = cv2.resize(image, (64, 64))

                filename = os.path.join(out_dir + "/" + name, str(i) + ".jpg")
                cv2.imwrite(str(filename), image)
                print(str(i) + " is saved successfully!")
        else:
            print("No face has detected.")

            continue
        print(image.shape)
