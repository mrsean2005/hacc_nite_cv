import cv2
import numpy as np
from PIL import Image
from reportlab.pdfgen import canvas

p1 = (0, 0)
pts = []


def mouseClick(event, xPos, yPos, flags, param):
    global dp1

    if event == cv2.EVENT_LBUTTONDOWN:
        p1 = (xPos, yPos)
        p1 = [p1[0], p1[1]]
        print(p1)
        pts.append(p1)


path = "input.jpg"
frame = cv2.imread(path)
cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', mouseClick)
frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
frame = cv2.resize(frame, (1600, 900))

while True:
    cv2.imshow('FRAME', frame)

    if len(pts) >= 4:
        pts_src = np.float32(pts)

        orientation = input(
            "Enter 'v' for vertical or 'h' for horizontal (default is vertical): ").lower()

        if orientation == 'h':
            output_size = (3508, 2480)
        else:
            output_size = (2480, 3508)

        pts_dst = np.float32([[0, 0], [output_size[0], 0], [
                             output_size[0], output_size[1]], [0, output_size[1]]])

        matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)
        warped = cv2.warpPerspective(frame, matrix, output_size)

        warped_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        _, thresholded = cv2.threshold(
            warped_gray, 120, 255, cv2.THRESH_BINARY)
        eroded = cv2.erode(thresholded, (3, 3), iterations=1)

        cv2.imshow('Warped', thresholded)

        break

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.imwrite('output_high_res_thresholded.jpg', eroded)

pdf_path = 'output_high_res_thresholded.pdf'
img = Image.open('output_high_res_thresholded.jpg')

pdf = canvas.Canvas(pdf_path, pagesize=(img.width, img.height))
pdf.drawInlineImage('output_high_res_thresholded.jpg', 0, 0)
pdf.save()

print(f"PDF saved at {pdf_path}")

cv2.destroyAllWindows()
