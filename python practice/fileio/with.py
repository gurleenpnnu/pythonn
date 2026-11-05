# f = open("file.txt")
# print(f.read())
# f.close()

# this is also written awith "with statement"
with open("file.txt") as f:
    print(f.read())