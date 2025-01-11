import cv2

coordinates = []

def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: 
        coordinates.append((x, y))
        print(f"Clicked at: {x}, {y}")

image = cv2.imread('assignment-001-given.jpg')

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Image', get_coordinates)


cv2.imshow('Image', image)

cv2.waitKey(0)

cv2.destroyAllWindows()

print("Coordinates clicked:", coordinates)
