import cv2
wajahDir ='datawajah'

cam = cv2.VideoCapture(0)
cam.set(3, 648) #ubah lebar cam
cam.set(4, 488) #ubah tinggi cam
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeDetector = cv2.CascadeClassifier("haarcascade_eye.xml")
faceID = input("Masukan Face ID yang akan direkam datanya [kemudian tekan enter]: ")
print("Tatap wajah anda ke depan dalam webcam tunggu proses pengambilan data wajah selesai.")
ambilData = 1
while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
        namaFile = 'wajah.'+str(faceID)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite(wajahDir+'/'+namaFile,frame)
        ambilData += 1
        roiAbuAbu = abuAbu[y:y+h,x:x+w]
        roiWarna = frame[y:y+h,x:x+w]
        eyes = eyeDetector.detectMultiScale(roiAbuAbu)
        for (xe, ye, we, he) in eyes:
            cv2.rectangle(roiWarna,(xe,ye),(xe+we,ye+he),(0,255,0),3)

    cv2.imshow('frame',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
    elif ambilData>30:
        break
print("pengambilan data selesai")
cam.release()
cv2.destroyAllWindows()