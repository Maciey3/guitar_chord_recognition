from detection import Detection

test = Detection('videos/C_G_D.mp4', reflection=True)
test.resize((1200, 600))
test.show(display_guitar=False, display_fingers=True)
