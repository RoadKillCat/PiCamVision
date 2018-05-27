import picamera, time, subprocess
s = 600
with picamera.PiCamera() as c:
    c.resolution = (2592, 1944)
    r = c.start_preview()
    r.fullscreen = False
    try:
        w,h = map(int, subprocess.check_output('xrandr').split(b'\n')[-2].split()[0].split(b'x'))
        r.window = (w-s,h-s,s,s)
    except FileNotFoundError:
        print('cannot get screen resolution so cannot position feed')
    print('Press ENTER to exit')
    input()
