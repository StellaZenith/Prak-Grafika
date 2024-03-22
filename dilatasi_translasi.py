import numpy as np
import cv2

jendela = np.zeros((500, 500, 3), dtype='uint8')
jendela [:] = (255, 255, 255)

ungu = 128,0,128

#Membuat kotak
kotak = cv2.rectangle(jendela, (125, 125), (375, 375), ungu, -1)

#translasi,
M = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
#translasi = cv2.warpAffine(kotak, M, (kotak.shape[1], kotak.shape[0]))
#Dilasi
dilasi = cv2.warpAffine(kotak, M, (1000, 1000))

#Mengeluarkan output
cv2.imshow("Translasi", dilasi)
#cv2.imshow("Translasi", translasi)
cv2.imshow("Canvas", jendela)
cv2.waitKey(0)
