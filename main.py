import cv2

import pyOptris as optris
from pyOptris import ColouringPalette


DEFAULT_LINUX_PATH="/usr/lib/libirdirectsdk.so"
optris.load_DLL(dll_path=DEFAULT_LINUX_PATH)

# USB connection initialisation 
optris.usb_init("22014241.xml")

optris.set_palette(ColouringPalette.RAINBOW)

w, h = optris.get_palette_image_size()
print("{} x {}".format(w, h))

while True:
    # Get the palette image (RGB image)
    frame = optris.get_palette_image(w, h)
    cv2.imshow("IR streaming", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

optris.terminate()
cv2.destroyAllWindows()