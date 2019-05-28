import cv2
import os

SAVE_DIR = "images_1day_graph"

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter(f"{SAVE_DIR}/video.avi", fourcc, 30.0, (1200, 700))


for i in range(1906):
    img_path = f"{SAVE_DIR}/{i}.png"
    print(img_path)
    frame = cv2.imread(img_path)
    out.write(frame)

out.release()