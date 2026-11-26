import cv2
import matplotlib.pyplot as plt
ImagePath = 'Baby.jpg'
Image = cv2.imread(ImagePath)
ImageRGB = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
Height, Width, _ = ImageRGB.shape
Rectangle1Width, Rectangle1Height = 150, 150
TopLeft1 = (20, 20)
BottomRight1 = (TopLeft1[0] + Rectangle1Width, TopLeft1[1] + Rectangle1Height)
cv2.rectangle(ImageRGB, TopLeft1, BottomRight1, (0, 255, 255), 3)
Rectangle2Width, Rectangle2Height = 200, 150
TopLeft2 = (Width - Rectangle2Width - 20, Height - Rectangle2Height - 20)
BottomRight2 = (TopLeft2[0] + Rectangle2Width, TopLeft2[1] + Rectangle2Height)
cv2.rectangle(ImageRGB, TopLeft2, BottomRight2, (255, 0, 255), 3)
Center1X = TopLeft1[0] + Rectangle1Width // 2
Center1Y = TopLeft1[1] + Rectangle1Height // 2
Center2X = TopLeft2[0] + Rectangle2Width // 2
Center2Y = TopLeft2[1] + Rectangle2Height // 2
cv2.circle(ImageRGB, (Center1X, Center1Y), 15, (0, 255, 0), -1)
cv2.circle(ImageRGB, (Center2X, Center2Y), 15, (0, 0, 255), -1)
cv2.line(ImageRGB, (Center1X, Center1Y), (Center2X, Center2Y), (0, 255, 0), 3)
Font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(ImageRGB, ' Region 1! ', (TopLeft1[0], TopLeft1[1] - 10), Font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(ImageRGB, ' Region 2! ', (TopLeft2[0], TopLeft2[1] - 10), Font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(ImageRGB, ' Center 1! ', (Center1X - 40, Center1Y + 40), Font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(ImageRGB, ' Center 2! ', (Center2X - 40, Center2Y + 40), Font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
ArrowStart = (Width - 50, 20)
ArrowEnd = (Width - 50, Height - 20)
cv2.arrowedLine(ImageRGB, ArrowStart, ArrowEnd, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(ImageRGB, ArrowEnd, ArrowStart, (255, 255, 0), 3, tipLength=0.05)
HeightLabelPosition = (ArrowStart[0] - 150, (ArrowStart[1] + ArrowEnd[1]) // 2)
cv2.putText(ImageRGB, f' Height : {Height}px.(Pixels)! ', HeightLabelPosition, Font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)
plt.figure(figsize=(12, 8))
plt.imshow(ImageRGB)
plt.title(' Annotated Image with Regions, Centers, and Bi-Directional Height Arrows! ')
plt.axis('off')
plt.show()
