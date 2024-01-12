import cv2

import pyOptris as optris
from pyOptris import ColouringPalette

#サーモグラフィ

DEFAULT_LINUX_PATH="/usr/lib/libirdirectsdk.so"
optris.load_DLL(dll_path=DEFAULT_LINUX_PATH)

# USB connection initialisation 
optris.usb_init("22014241.xml")

optris.set_palette(ColouringPalette.ALARM_BLUE_HI)

# w, h = optris.get_palette_image_size()
w, h = optris.get_thermal_image_size()
print("{} x {}".format(w, h))


while True:
    thermal_frame = optris.get_thermal_image(width=w,height=h)
    processed_thermal_frame = (thermal_frame[40][40] - 1000.0) / 10.0
    print(processed_thermal_frame)

    # Get the palette image (RGB image)
    frame = optris.get_palette_image(w, h)
    # _, frame = optris.get_thermal_palette_image(t_width=w,t_height=h,p_width=w,p_height=h)
    if frame is None:
        break    
    cv2.imshow("IR streaming", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

optris.terminate()
cv2.destroyAllWindows()