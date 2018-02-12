import cv2,os

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

isim =input('Kayıt için Boşluksuz! \nAdınızı,Soyadınızı yazın = ')
resimsayisi = 0
sayi=input("kayıt numarası = ")
os.mkdir("ResimDatasi/"+str(sayi)+".)"+""+isim)
a=(sayi+".)"+isim)
while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)#yüzü gören çerçeve ayarları
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        #çekilen resmi +1 arttır.
        resimsayisi+=1
        # çekilen resimlerin kaydedileceği yolu belirtelim.
        cv2.imwrite("ResimDatasi/"+a+'/'+'.' + str(resimsayisi) +".jpg", gray[y:y + h, x:x + w])
        cv2.imshow('cerceve', img)#çerçevemiz..

    if resimsayisi== 20: # resim sayisi 20 olunca durdur.
        break

cam.release()
cv2.destroyAllWindows()