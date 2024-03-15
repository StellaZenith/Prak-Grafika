import numpy as np
import cv2

#membuat canvas
jendela = np.zeros((500, 500, 3), dtype='uint8')
jendela [:] = (255, 255, 255)

#Membuat garis
cv2.line(jendela, (0, 500), (250, 250), (190, 2, 247), 10)

#warna yang diperlukan
green = (0, 255, 0)
red = (0,0,255)
biru = (255, 0, 0)

#Membuat kotak
cv2.rectangle(jendela, (125, 125), (375, 375), (10,20,30), 10)
#Membuat lingkaran
cv2.circle(jendela, (250, 250), 100, (182,291,299), -1)

#titik koordinat
k1 = (125, 250)
k2 = (125, 375)
k3 = (375, 375)
cv2.circle(jendela, k1, 10, green, -1)
cv2.circle(jendela, k2, 10, red, -1)
cv2.circle(jendela, k3, 10, biru, -1)

#Membuat segitiga
titik_segitiga = np.array([k1, k2, k3])
cv2.drawContours(jendela, [titik_segitiga], 0, (120, 109, 80), -1)

#Mengeluarkan output
cv2.imshow("Canvas", jendela)
cv2.waitKey(0)
