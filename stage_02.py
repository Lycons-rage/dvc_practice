with open("artifact.txt", "r") as f:
    text = f.read()

print(text)

# this establishes a dependency between stage_01 and stage_02, stage_01 has to be executed first before executing stage_02