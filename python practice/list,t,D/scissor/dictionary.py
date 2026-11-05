marks = {
    "harshu": 100,
    "shubu": 92,
    "gulu":100
}

print(marks["harshu"])
print(marks.keys())
print(marks.items())
marks.update({"harshu":99})
print(marks)
# dictionary is unordered
# it is mutable
# it is indexed
print(marks.get("harshu2"))#prints None
print(marks["harshu2"])#prints an error
