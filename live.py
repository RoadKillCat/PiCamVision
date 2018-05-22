import picamera, time
with picamera.PiCamera() as c:
    c.resolution = (2592, 1944)
    p = c.start_preview()
    time.sleep(20)
