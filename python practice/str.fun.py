name= "gurleen"
print(len(name))
print(name.endswith("een"))
print(name.startswith("gur"))
print(name.capitalize())
name_r = name.replace("gurleen","hark")
print(name_r)

#escape sequence character
a = "harry is a good boy \nbut not a bad\t \"boy\""
print(a)

l = "hi this  is a  string"
print(l.replace("  "," "))

#strings are immutable which means you cannot change them by executing operations on them


#5) 
Letter = "\"Dear Harry,\n\t this python course is nice.\n Thanks!\""
print("Letter: ",Letter)