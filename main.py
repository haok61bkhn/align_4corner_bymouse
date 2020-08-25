import cv2
from align import Alignment
X=Alignment()
def read(path):
    img=cv2.imread(path)
    height=img.shape[0]
    width=img.shape[1]
    ratio=height/width
    return cv2.resize(img,(int(500*ratio),500))


def draw_rec(event, x, y, flags, param):
    global ix, iy, ex, ey, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        ex, ey = x, y
        


def get_crop_size(image):
    cv2.namedWindow('draw_rectangle')
    cv2.setMouseCallback('draw_rectangle', draw_rec, image)
    print("Choose your area of interest!")
    while 1:
        cv2.imshow('draw_rectangle', image)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('a'):
            cv2.destroyAllWindows()
            break
def align(img):
    img0=img.copy()
    get_crop_size(img)
    x1=ix
    y1=iy
    img=cv2.circle(img,(ix,iy),3,(255, 0, 0),3)
    get_crop_size(img)
    x2=ix
    y2=iy
    img=cv2.circle(img,(ix,iy),3,(255, 0, 0),3)
    get_crop_size(img)
    x3=ix
    y3=iy
    img=cv2.circle(img,(ix,iy),3,(255, 0, 0),3)
    get_crop_size(img)
    x4=ix
    y4=iy
    img=cv2.circle(img,(ix,iy),3,(255, 0, 0),3)
    return X.align(img0,[(x1,y1),(x2,y2),(x3,y3),(x4,y4)])




if __name__ == "__main__":
    path="img/045234789.jpg"
    img=read(path)
    # cv2.imwrite("test.jpg",align(img))
    cv2.imshow("test",align(img))
    cv2.waitKey(0)
    
