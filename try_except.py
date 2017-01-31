try:
    fhandle = open("file.txt", "w")
    fhandle.write("this is some content")
    print("Written to file")
except IOError as e:
    print("Exception caught:", e)
except Exception as e:
    print("Another error happened", e)
else:
    print("file written successfully")
    fhandle.close()
