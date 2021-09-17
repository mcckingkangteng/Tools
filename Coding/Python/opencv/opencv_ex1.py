import cv2
img = cv2.imread(r"E:\DJI_kangteng\Coding\Python\opencv\inspire.jpg")
# print(img.shape)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img_threshold = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("img",img)
cv2.imshow("thre",img_threshold)

key = cv2.waitKey(0)
if key==27: #按esc键时，关闭所有窗口
    print(key)
    cv2.destroyAllWindows()
cv2.imwrite(r"E:\DJI_kangteng\Coding\Python\opencv\thre.jpg",img_threshold)

