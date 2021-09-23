import cv2

path = "gura.png"

img = cv2.imread(path, 0)

cv2.imshow("img", img)
height, width = img.shape

file = open("file", "w+")

ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def write_char_to_file(grey_val):
    file.write(ascii_chars[int(grey_val / (255/70)) - 1])
    file.write(' ')


for i in range(height):
    for j in range(width):
        write_char_to_file(img[i][j])
    file.write("\n")

key = cv2.waitKey()
if key == "Q":
    cv2.destroyAllWindows()
