import cv2

#カメラの設定　デバイスIDは0
cap = cv2.VideoCapture(0)
print(cap)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)


#繰り返しのためのwhile文
while True:
    #カメラからの画像取得
    ret, frame = cap.read()
    print(ret)
    if ret is False:
        print("終了")
        break

    #カメラの画像の出力
    cv2.imshow('camera' , frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#メモリを解放して終了するためのコマンド
cap.release()
cv2.destroyAllWindows()