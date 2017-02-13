# NTFS file system only
# [filename]:[stream]
# default stream is $DATA

fh = open("file.txt:myfile", "w")
fh.write("this is a test")
fh.close()

fh = open("file.txt:myfile", "r")
data = fh.read(100)
print(data)