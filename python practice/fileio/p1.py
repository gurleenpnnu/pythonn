f= open("poem.txt")
content = f.read()

if("twinkle" in content):
    print("the word twinle is present")

else:
    print("not presenttt")

f.close()