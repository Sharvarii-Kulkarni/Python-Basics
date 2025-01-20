f = open("input.txt","w")
f.write("Sharvari")
f = open("input.txt","r")
content = f.read()
rev = content[::-1]
f1 = open("reversed.txt","w")
f1.write(rev)