import os

dir = os.path.dirname('C://Users/saykı/Desktop/Code/Pyhton Klasör/Python_Camping/selenium/Discord/sounnds/as')

as1 = os.listdir(dir)

deneme = 'C:/Users/saykı\Desktop\Code\Pyhton Klasör\Python_Camping\selenium\Discord\sounnds\6 Litre Pırıl 10 Liraydı.mp3'



dosya = open("liste.txt","w",encoding="utf-8")

for i in as1:
    dosya.write(f"{i}\n")

dosya = open("liste.txt","r",encoding="utf-8") 


liste = dosya.read().split("\n")


