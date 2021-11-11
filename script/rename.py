import os


files = os.listdir('.')

for filename in files:
    portion = os.path.splitext(filename)
    if portion[1] == ".mkv":
        newname = portion[0] + ".mp4"
        os.rename(filename, newname)
