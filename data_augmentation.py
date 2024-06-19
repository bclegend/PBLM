import cv2
import os

save_dir = './preprocess_data/'

image_size =(1024,1024)


if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

for classifi in os.listdir('./data/'):
    print(classifi)
    class_dir =save_dir+classifi+'/'

    if not os.path.isdir(class_dir):
        os.mkdir(class_dir)

    for image in os.listdir('./data/'+classifi):
        print('./data/'+classifi+image)
        img = cv2.imread('./data/'+classifi+'/'+image)
        img = cv2.resize(img,image_size)
        print(img.shape)
        cv2.imwrite(class_dir+image,img)
        # rotate 90 degree
        img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(class_dir+'90'+image,img)
        # rotate 180 degree
        img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(class_dir+'180'+image,img)
        # rotate 90 degree
        img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(class_dir+'270'+image,img)
