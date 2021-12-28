
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed
from random import random
from time import process_time, sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

import csv
import re
from openpyxl import load_workbook
import urllib.request
from datetime import datetime
from urllib.request import urlopen
 

import random



user_name=["ckaclrlaqkq1"]
#user_name=["ckaclrlaqkq1","chamchigimbob","chamcigimbob2","chamchigimbob3"]
# print(user_name)


random.shuffle(user_name)
# print(random.choices(user_name))




df=pd.read_csv('new.csv')
# print(df['Instagram Account'])
for i in range(0,1):


# for i in range(3,5):
    print(i,"no of kink")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/accounts/login/?next=%2F&source=logged_out_half_sheet')
    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys( random.choice(user_name))
    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input'))).send_keys('ckaclrlaqkq2@')
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.ENTER)
    time.sleep(10)
    # driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
    # url=df['Instagram Account'][i]
    url="https://www.instagram.com/healesvilletoyota/"
    driver.get(url)
    time.sleep(10)
    soup=BeautifulSoup(driver.page_source ,'html.parser')


    # find div of profile ..

    div_of_profile=soup.find('section',{'class':'wW3k-'})
    name=div_of_profile.find('h2')
    list_of_follwers=div_of_profile.find_all('li')

    posts=list_of_follwers[0]
    image_count=1


    followers=list_of_follwers[1]
    following=list_of_follwers[2]
    data_list=[]

    div_of_bio=soup.find('div',{'class':'QGPIr'})

    actions = ActionChains(driver)


    image_count=1

    card_list=[]


    for _ in range(5):
            actions.send_keys(Keys.SPACE).perform()  # moving slider
            
            time.sleep(3)        
    all_cards=driver.find_elements_by_class_name('eLAPa')
    for one_card in all_cards:
        try:
            if one_card not in card_list:
                driver.execute_script("arguments[0].click();", one_card)
                # one_card.click()
                card_list.append(one_card)


                time.sleep(5)
                soup=BeautifulSoup(driver.page_source,'html.parser')         # get html 
                image_div=soup.find('article',{'role':'presentation'}).find('img').get('src')
                
            
                req = urllib.request.Request(image_div, headers={'User-Agent': '*'})   # Download images 
                response = urllib.request.urlopen(req)
                html = urllib.request.urlopen(req).read()
                a=url.replace("https://instagram.com/","")
                with open(r'{}'.format(str(url.replace("https://www.instagram.com/"," ").replace("?"," ").replace('/',''))+str(+image_count)+'.jpeg'), 'wb') as f:
                    
                    f.write(html)
                    try:
                        saved_image_name=''.format(a.replace("?"," "))+str(+image_count)
                    except:
                        saved_image_name=''.format(a)+str(+image_count)
                    # try:
                        
                    image_text=driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/span')
                    image_texts=image_text.text
                    # except:
                        # image_texts="NO text"
                    try:
                        likes=driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/a')
                        like=likes.text
                
                    except:
                        like="no like"
                

                    comments=driver.find_elements_by_class_name('Mr508')
                
                    data_list.append(url)
                    data_list.append(name.text)
                    data_list.append(div_of_bio.text)
                    data_list.append(following.text)
                    data_list.append(followers.text)
                    data_list.append(posts.text)
                    data_list.append(image_count)
                    data_list.append(saved_image_name)
            
                    
                    posting_time=soup.find('time').get('title')
                    # print(image_texts)
                    
                    if image_texts is not None:
                        data_list.append(image_texts)
                    else:
                        data_list.append("No textq")


                    data_list.append(posting_time)
                    data_list.append(str(datetime.now().strftime("%H:%M:%S")))              
                    data_list.append(like)

                    data_list.append(len(comments))
                
                    data_frame=pd.DataFrame([data_list])
                    # print(data_frame)
                    df_read=data_frame.to_csv('insta4.csv',mode="a" ,header=False )  # making csv
                        


                    data_list.clear()
                    driver.find_element_by_xpath('/html/body/div[6]/div[3]/button').click()
                    image_count = image_count+1
                    print('done one posy')

        except:
            pass
print('done full link')        
driver.close()
    






























