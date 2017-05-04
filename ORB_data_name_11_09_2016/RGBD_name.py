text_file = open("rgbd.txt", "w")

for x in range(1, 2318):
	if x<10:
		text_file.write("00000%s color/00000%s.png 00000%s depth/00000%s.png\n" % (x, x, x, x) )
	elif x<100:
		text_file.write("0000%s color/0000%s.png 0000%s depth/0000%s.png\n" % (x, x, x, x) )
	elif x<1000:
		text_file.write("000%s color/000%s.png 000%s depth/000%s.png\n" % (x, x, x, x) )
	elif x<10000:
		text_file.write("00%s color/00%s.png 00%s depth/00%s.png\n" % (x, x, x, x) )
	elif x<100000: 
		text_file.write("0%s color/0%s.png 0%s depth/0%s.png\n" % (x, x, x, x) )
	else:
		text_file.write("%s color/%s.png %s depth/%s.png\n" % (x, x, x, x) )
text_file.close()
