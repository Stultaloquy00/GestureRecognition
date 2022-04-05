from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=200)
camera.annotate_text = "HEWWO"
camera.annotate_text_size = 160
camera.annotate_background =  Color('blue')
sleep(10)
camera.stop_preview()