import cv2
import numpy as np

def process_frame(detector, img, count, direction, formVal, cap, pushup_count):  
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        elbow = detector.findAngle(img, 11, 13, 15)
        shoulder = detector.findAngle(img, 13, 11, 23)
        hip = detector.findAngle(img, 11, 23, 25)

        per = np.interp(elbow, (90, 160), (0, 100))
        bar = np.interp(elbow, (90, 160), (height - 50, 50))

        remark = "" 
        if elbow > 160 and shoulder > 40 and hip > 160:
            formVal = 1

        if formVal == 1:
            if per == 0:
                if elbow <= 90 and hip > 160:
                    remark = "Up"
                    if direction == 0:
                        count += 0.5
                        direction = 1
                        if remark == "Up":
                            pushup_count += 1
                else:
                    remark = "Fix Form"

            if per == 100:
                if elbow > 160 and shoulder > 40 and hip > 160:
                    remark = "Down"
                    if direction == 1:
                        count += 0.5
                        direction = 0
                else:
                    remark = "Fix Form"

        cv2.rectangle(img, (0, 0), (width, 70), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (width // 2 - 30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

        cv2.rectangle(img, (0, height - 160), (200, height), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (50, height - 90), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)

        cv2.rectangle(img, (width - 500, 0), (width, 100), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, remark, (width - 490, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    return img, count, direction, formVal, pushup_count
