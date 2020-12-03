import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from pyvirtualdisplay import Display
import csv




def scraper():
    field_names= ['name', 'link', 'id', 'tags']
    classical = []
    challenge = []
    partial = []
    tutorial = []
    riddle = []
    basics = []
    final = []
    default = "https://www.spoj.com"

    display = Display(visible=0, size=(800, 800))  
    display.start()
    driver = webdriver.Chrome()
    driver.get("https://www.spoj.com/problems/classical/")
    ele_classical = str((driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/ul/li[15]/a").get_attribute('href')))
    #print(ele_classical)
    driver.quit()

    driver = webdriver.Chrome()
    driver.get("https://www.spoj.com/problems/challenge/")
    ele_challenge = str((driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/ul/li[8]/a").get_attribute('href')))
    #print(ele_challenge)
    driver.quit()

    driver = webdriver.Chrome()
    driver.get("https://www.spoj.com/problems/partial/")
    ele_partial = str((driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/ul/li[8]/a").get_attribute('href')))
    #print(ele_partial)
    driver.quit()

    driver = webdriver.Chrome()
    driver.get("https://www.spoj.com/problems/tutorial/")
    ele_tutorial = str((driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/ul/li[15]/a").get_attribute('href')))
    #print(ele_tutorial)
    driver.quit()

    # riddles only has one page so no selenium required

    driver = webdriver.Chrome()
    driver.get("https://www.spoj.com/problems/basics/")
    ele_basics = str((driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/ul/li[10]/a").get_attribute('href')))
    #print(ele_basics)
    driver.quit()


    #classical problems
    print("Classical")
    i = 0
    while True:
        url = "https://www.spoj.com/problems/classical/sort=0,start=" + str(50*i)
        i += 1
        print(i)
        if int(url[53:]) > int(ele_classical[53:]):
            break
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        for td in soup.find_all("td", {"align" : "left"}):
            anchor = td.find("a")
            text = anchor.text
            print(text)
            href = anchor['href']
            id = href[10:]
            urlprob = default + href
            r1 = requests.get(urlprob)
            soup1 = BeautifulSoup(r1.content, 'html5lib')
            holder = soup1.find("div", {"id" : "problem-tags"})
            tags = []
            tags.append('classical')
            if holder:
                if holder.find_all("a") and holder:
                    for a in holder.find_all("a"):
                        tags.append(a.text[1:])
            classical.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            final.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            

    # with open("spoj.json", "w") as spoj_data:
    #     json.dump(classical, spoj_data, indent=4, sort_keys=True)

    #challenge problems
    i = 0
    print("challenge")
    while True:
        url = "https://www.spoj.com/problems/challenge/sort=0,start=" + str(50*i)
        i += 1
        print(i)
        if int(url[53:]) > int(ele_challenge[53:]):
            break
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        for td in soup.find_all("td", {"align" : "left"}):
            anchor = td.find("a")
            text = anchor.text
            print(text)
            href = anchor['href']
            id = href[10:]
            urlprob = default + href
            r1 = requests.get(urlprob)
            soup1 = BeautifulSoup(r1.content, 'html5lib')
            holder = soup1.find("div", {"id" : "problem-tags"})
            tags = []
            tags.append('challenge')
            if holder:
                if holder.find_all("a") and holder:
                    for a in holder.find_all("a"):
                        tags.append(a.text[1:])
            challenge.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            final.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            

    # with open("spoj.json", "w") as spoj_data:
    #      json.dump(challenge, spoj_data, indent=4, sort_keys=True)



    # #partial problems
    i = 0
    print("partial")
    while True:
        url = "https://www.spoj.com/problems/partial/sort=0,start=" + str(50*i)
        i += 1
        print(i)
        if int(url[51:]) > int(ele_partial[51:]):
            break
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        for td in soup.find_all("td", {"align" : "left"}):
            anchor = td.find("a")
            text = anchor.text
            print(text)
            href = anchor['href']
            id = href[10:]
            urlprob = default + href
            r1 = requests.get(urlprob)
            soup1 = BeautifulSoup(r1.content, 'html5lib')
            holder = soup1.find("div", {"id" : "problem-tags"})
            tags = []
            tags.append('partial')
            if holder:
                if holder.find_all("a") and holder:
                    for a in holder.find_all("a"):
                        tags.append(a.text[1:])
            partial.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            final.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            

    # with open("spoj.json", "w") as spoj_data:
    #      json.dump(partial, spoj_data, indent=4, sort_keys=True)

    # #tutorial problems
    i = 0
    print("tutorial")
    while True:
        url = "https://www.spoj.com/problems/tutorial/sort=0,start=" + str(50*i)
        i += 1
        print(i)
        if int(url[52:]) > int(ele_tutorial[52:]):
            break
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        for td in soup.find_all("td", {"align" : "left"}):
            anchor = td.find("a")
            text = anchor.text
            print(text)
            href = anchor['href']
            id = href[10:]
            urlprob = default + href
            r1 = requests.get(urlprob)
            soup1 = BeautifulSoup(r1.content, 'html5lib')
            holder = soup1.find("div", {"id" : "problem-tags"})
            tags = []
            tags.append('tutorial')
            if holder:
                if holder.find_all("a") and holder:
                    for a in holder.find_all("a"):
                        tags.append(a.text[1:])
            tutorial.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            final.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            

    # with open("spoj.json", "w") as spoj_data:
    #      json.dump(tutorial, spoj_data, indent=4, sort_keys=True)

    # #basics problems
    i = 0
    print("basics")
    while True:
        url = "https://www.spoj.com/problems/basics/sort=0,start=" + str(50*i)
        i += 1
        print(i)
        if int(url[50:]) > int(ele_basics[50:]):
            break
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        for td in soup.find_all("td", {"align" : "left"}):
            anchor = td.find("a")
            text = anchor.text
            print(text)
            href = anchor['href']
            id = href[10:]
            urlprob = default + href
            r1 = requests.get(urlprob)
            soup1 = BeautifulSoup(r1.content, 'html5lib')
            holder = soup1.find("div", {"id" : "problem-tags"})
            tags = []
            tags.append('basics')
            if holder:
                if holder.find_all("a") and holder:
                    for a in holder.find_all("a"):
                        tags.append(a.text[1:])
            basics.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            final.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
            

    # with open("spoj.json", "w") as spoj_data:
    #      json.dump(basics, spoj_data, indent=4, sort_keys=True)

    #riddle problems
    print("riddles")
    url = "https://www.spoj.com/problems/riddle/sort=0,start=0"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    for td in soup.find_all("td", {"align" : "left"}):
        anchor = td.find("a")
        text = anchor.text
        print(text)
        href = anchor['href']
        id = href[10:]
        urlprob = default + href
        r1 = requests.get(urlprob)
        soup1 = BeautifulSoup(r1.content, 'html5lib')
        holder = soup1.find("div", {"id" : "problem-tags"})
        tags = []
        tags.append('riddle')
        if holder:
            if holder.find_all("a") and holder:
                for a in holder.find_all("a"):
                    tags.append(a.text[1:])
        riddle.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
        final.append({'name' : text,'link' : default + href,'id' : id,"tags" : tags})
        

    with open('spoj.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(final)