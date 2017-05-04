text_file = open("rgb.txt", "w")

for x in range(000013, 003020):
	if x<10:
		text_file.write("00000%s color/00000%s.png\n" % (x, x) )
	elif x<100:
		text_file.write("0000%s color/0000%s.png\n" % (x, x) )
	elif x<1000:
		text_file.write("000%s color/000%s.png\n" % (x, x) )
	elif x<10000:
		text_file.write("00%s color/00%s.png\n" % (x, x) )
	elif x<100000:
		text_file.write("0%s color/0%s.png\n" % (x, x) )
	else:
		text_file.write("%s color/%s.png\n" % (x, x) )
text_file.close()
