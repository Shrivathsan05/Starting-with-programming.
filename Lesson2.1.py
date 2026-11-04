import cv2
BabyImage = cv2.imread('Baby.png')
cv2.namedWindow(' Loaded Baby Image ', cv2.WINDOW_NORMAL)
cv2.resizeWindow(' Loaded Baby Image ', 800, 500)
cv2.imshow(' Loaded Baby Image ', BabyImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f" Baby Image Dimensions : {BabyImage.shape} ")