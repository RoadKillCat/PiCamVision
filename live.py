import picamera,time,subprocess,sys
prev_w = 600
prev_h = int(prev_w * 3/4)
with picamera.PiCamera() as c:
    c.resolution = (2592, 1944)
    r = c.start_preview()
    r.fullscreen = False
    w,h = map(int, subprocess.check_output('xrandr').split(b'\n')[-2].split()[0].split(b'x'))
    r.window = (w-prev_w, h-prev_h, prev_w, prev_h)
    input('press ENTER to exit')
