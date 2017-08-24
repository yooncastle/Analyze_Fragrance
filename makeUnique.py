'''This is the code for adding additonal crawled fragrance informations to existing csv file'''

import csv
import sys

def makeunique() :
  f1 = open('fragInfos.csv', 'r',encoding='utf-8')
  f2 = open('fragInfoUnique.csv', 'a',encoding='utf-8')
  reader = csv.reader(f1)
  writer = csv.writer(f2)
  #52 varities of frags
  frags = ['woody', 'balsamic', 'powdery', 'warm spicy', 'citrus', 'rose', 'fruity', 'fresh spicy', 'sweet', 'amber', 'floral', 'aromatic', 'ozonic', 'green', 'musky', 'aquatic', 'yellow floral', 'cacao', 'fresh', 'white floral', 'vanilla', 'herbal', 'aldehydic', 'tropical', 'leather', 'salty', 'coca-cola', 'gourmand', 'honey', 'sour', 'marine', 'earthy', 'patchouli', 'terpenic', 'animalic', 'smoky', 'soapy', 'tuberose', 'soft spicy', 'tobacco', 'coffee', 'narcotic', 'oud', 'conifer', 'caramel', 'coconut', 'cherry', 'cinnamon', 'nutty', 'bitter', 'almond', 'savory']
  headers = ['number', 'brand', 'name', 'woody', 'balsamic', 'powdery', 'warm spicy', 'citrus', 'rose', 'fruity', 'fresh spicy', 'sweet', 'amber', 'floral', 'aromatic', 'ozonic', 'green', 'musky', 'aquatic', 'yellow floral', 'cacao', 'fresh', 'white floral', 'vanilla', 'herbal', 'aldehydic', 'tropical', 'leather', 'salty', 'coca-cola', 'gourmand', 'honey', 'sour', 'marine', 'earthy', 'patchouli', 'terpenic', 'animalic', 'smoky', 'soapy', 'tuberose', 'soft spicy', 'tobacco', 'coffee', 'narcotic', 'oud', 'conifer', 'caramel', 'coconut', 'cherry', 'cinnamon', 'nutty', 'bitter', 'almond', 'savory','love', 'like', 'dislike', 'winter', 'spring', 'summer', 'autumn', 'day', 'night']
  writer.writerow(headers)
  number = 381
  for row in reader :
    rowWrite = []
    rowWrite.append(number)
    rowWrite.append(row[1]) #write brand
    rowWrite.append(row[2]) #write name
    for i in range(len(frags)) :
      rowWrite.append(0)
    for index in range(3,14,2) :
      if row[index] in frags :
        place = frags.index(row[index])
        #print(row[index],"meets with ： ",i,"counts with ：",row[index+1])
        rowWrite[place+3] = row[index+1]
    for i in range(9) :
      rowWrite.append(row[15+i])
    
    writer.writerow(rowWrite)
    number = number + 1
  
  f1.close()
  f2.close()

#main starts here
makeunique()

