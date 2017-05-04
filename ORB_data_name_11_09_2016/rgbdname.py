text_file = open("rgbd.txt", "w")

for x in range(100000, 100876):
	text_file.write("%s rgb_png/%s.png\n %s depth_png/%s.png\n " % (x, x, x, x) )
text_file.close()