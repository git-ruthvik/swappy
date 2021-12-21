import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)
startingdist = None

while True:
    ret, img = cap.read()
    hands, img = detector.findHands(img)

    if len(hands) == 2:
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            if startingdist is None:
                length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
                startingdist = length
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
            diff = startingdist - length
            if abs(diff) > 100:
                print("Zoom in")
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break