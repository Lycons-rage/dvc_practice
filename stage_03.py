with open("artifact.txt", "r+" ) as f:
    text = f.read()

with open("artifact.txt", "w+") as f:
    f.write(text+". Adding one more line and end of stage 03")

with open("artifact.txt", "r+" ) as f:
    text = f.read()

print(text)