import os

dir = os.path.dirname('/path/to/folder')

as1 = os.listdir(dir)



dosya = open("liste.txt","w",encoding="utf-8")

for i in as1:
    dosya.write(f"{i}\n")

dosya = open("liste.txt","r",encoding="utf-8") 


liste = dosya.read().split("\n")


