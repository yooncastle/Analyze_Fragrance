from bs4 import BeautifulSoup
from urllib.request import *
from urllib.request import Request, urlopen
import csv
import time

def getInfos (url,perfumeNo) :
  fragList = list() 
  countList = list()
  req = Request(url,headers={'User-Agent': 'your bot 0.1'})
  webpage = urlopen(req).read()
  soup = BeautifulSoup(webpage, 'html.parser')

  #Get Brand name -> brand
  brand = soup.find('span',{"itemprop":"brand"})
  brand = brand.find('span',{"itemprop":"name"})
  brand = brand.get_text()
  
  #Get Perfume name -> perfume
  perfume = soup.find('div',{"xmlns":"http://www.w3.org/1999/html"})
  perfume = perfume.find('h1',{"style":"clear: left;"})
  perfume = perfume.find('span',{"itemprop":"name"})
  perfume = perfume.get_text()
  
  #Get Fragrances -> fragList, countList
  fList = soup.find('div',{"style":"background-color: #ffffff; z-index: 10; position: relative;"})
  nameList = fList.find_all('span')
  divList = fList.find_all('div')
  for div in divList :
      if(div.div) :
          count = div.div['style'].split(": ")
          count = count[1].split("px;")[0]
          countList.append(count) 

  for name in nameList :
      frag = name.get_text()
      frag = frag.replace(',',"")
      if frag == "main accords" :
          continue
      fragList.append(frag)
 
  while(len(fragList)<6) :
    fragList.append("")
    countList.append("")

  #Get votes -> heightList
  voteList = soup.find('div',{"id":"diagramresult"})
  heightList = list()
  titleList = ["clsloveD","clslikeD","clsdislikeD","clswinterD","clsspringD","clssummerD","clsautumnD","clsdayD","clsnightD"]
  for vote in range(0,9) :
    style = voteList.find('div',{"id":titleList[vote]})['style'].split(": ")
    height = style[2].split("px;")[0]
    heightList.append(height)

  people = soup.find('b',{"id":"peopleD"})
  people = people.get_text()
  print(people)

  perfumeList = list()
  perfumeList.append(perfumeNo)
  perfumeNo = perfumeNo + 1
  perfumeList.append(brand)
  perfumeList.append(perfume)
  for count in range(len(fragList)) :
    perfumeList.append(fragList[count])
    perfumeList.append(countList[count])

  #perfumeList = perfumeList + fragList
  #perfumeList = perfumeList + countList
  perfumeList = perfumeList + heightList
  perfumeList = perfumeList.append(people)
  #print(perfumeList)
  return perfumeList

def geturls() :
  with open('./fragInfos.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    perfumeList = list()
    perfumeInfo = list()
    perfumeNo = 1
    abcs = ["-1/#A","-2/#B","-3/#C","-4/#D","-5/#F","-6/#I","-7/#L","-8/#M","-9/#O","-10/#R","-11/#T"]
    count = 1
    for abc in abcs :
      url = "https://www.fragrantica.com/designers"+abc
      req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
      webpage = urlopen(req).read()
      soup = BeautifulSoup(webpage, 'html.parser')
      brands = soup.find('div',{"id":"col1"})
      brands = brands.find_all('div',{"class":"nduList"})
      for brand in brands :
        link = brand.find('a')['href']
        url = "https://www.fragrantica.com"+link
        req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        perfumeList = soup.find_all('div',{'class':'perfumeslist'})
        for perfume in perfumeList :
          count = count + 1
          if count < 44 :
              break
          perfume = perfume.find('a')['href']
          url = "https://www.fragrantica.com"+perfume
          info = getInfos(url,perfumeNo)
          print(info)
          perfumeInfo.append(info)
          perfumeNo = perfumeNo + 1

          f = open('./fragInfos.csv','a')
          writer = csv.writer(f)
          writer.writerow(info)
          f.close()

          time.sleep(15)
          if perfumeNo % 10 == 0 :
            time.sleep(20)
          if perfumeNo % 10 == 5 :
            time.sleep(20)
       
    #for per in perfumeInfo :
#      writer.writerow(per)
 
  return perfumeInfo
      
#main starts here
perfumeList = geturls()
print(perfumeList)
