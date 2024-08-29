import cv2
import numpy as np

# resim oluştur
img = np.zeros((512,512,3), np.uint8) # siyah bir resim
print(img.shape)

cv2.imshow("Siyah", img)

# çizgi
# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(img, (100,100), (100,300), (0,255,0), 3) # BGR = (0,255,0)
cv2.imshow("Cizgi", img)

# dikdörtgen
# (resim, başlangıç, bitiş, renk )
cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Dikdortgen", img)

# çember
# (resim, merkez, yarı çap, renk)
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Cember", img)

# metin
# (resim, başlangıç noktası, font, kalınlığı, renk)
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)