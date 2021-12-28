
from os import close
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed
from random import random
from time import process_time, sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
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

import urllib.request
import csv
from urllib.request import urlopen

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


data_list1=[]
data_list=[]
image_count=1

# header = ['Index','name', 'joined_date', 'headers', 'likes','follwers','website','time_of_post','image_text','likes_on_post','comments','share','Image_name','Website Link']


# with open('test.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
    # writer.writerow(header)
df=pd.read_csv('facebook_list_Dec21.csv')    
for i in range(1,2):
    url=df['urls'][i]

 
# Account level Info

# For login 

    driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    driver.get('https://www.facebook.com/login/')
    time.sleep(6)
    # driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div[1]/a').click()

    time.sleep(3)
                                #  '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/input'
    driver.find_element_by_id('email').send_keys('boram8235@gmail.com')
    driver.find_element_by_id('pass').send_keys('ckaclrlaqkq1!')
    driver.find_element_by_id('pass').send_keys(Keys.ENTER)
    time.sleep(4)
    driver.get(url)
    time.sleep(10)
    for i in range(0,10):        
        try:
            driver.find_element_by_xpath("//*[contains(text(), 'See more')]").click() 
        except:
            pass  
    try:     
    
        name=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/h2/span')
    except:
    # /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/h1
        name=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/h1')

    data_list1.append(name.text)
    # print(name.text)
    try:
        joined_date=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[5]/div/div/div/span/div[2]/span').text
    except:
        joined_date="no join date"
    data_list1.append(joined_date)
    # print(joined_date.text)
    actions = ActionChains(driver)

    time.sleep(5)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    
    header_list=[]
    try:
        account_level_info_div=soup.find('div',{'class':'datstx6m cbu4d94t j83agx80'})
    except:
        account_level_info_div=soup.find('div',{'class':'sjgh65i0 cbu4d94t j83agx80'})
            
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'See more')]").click()   
    except:
        pass
    # try:
    head_text=account_level_info_div.find_all('div',{'style':'text-align: start;'})
    for h in head_text:
        # print(h.text)
        header_list.append(h.text)
    # except:
    #     header_list.append("No header")
                





# taijpn5t cbu4d94t j83agx80

    data_list1.append(header_list)
    # data_list1.append(header2.text)

    # print(header1.text+header2.text)
    try:
        like_follow_div=account_level_info_div.find_all('div',{'class':'taijpn5t cbu4d94t j83agx80'})
        data_list1.append(like_follow_div[0].text)
        data_list1.append(like_follow_div[1].text)
    except:
        
        data_list1.append('No Like info given')
        data_list1.append('No follow info given')
    try:
        website=account_level_info_div.find_all('span',{'class':'d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v b1v8xokw py34i1dx'})
        for w in website:
            if "http" in w.text:
                data_list1.append(w.text)
    except:
        data_list1.append('No Website given')
                    
        # else:
    # print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
            # data_list1.append("NO Website")
    # for i in range(0,10):        
    #     try:
    #         driver.find_element_by_xpath("//*[contains(text(), 'See more')]").click() 
    #     except:
    #         pass  
##############################   post information ##############3333
    img_list=[]
    for _ in range(1):
            # actions.send_keys(Keys.SPACE).perform()
            # try:
                # for _ in range(17):
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(1)
            # except:
            #     pass

    time.sleep(5)
    soup=BeautifulSoup(driver.page_source,'html.parser')

    all_post_div=soup.find_all('div',{'role':'article'})
    
    
    for single_post_div  in all_post_div:
        try:
    
            try:
                for i in range(0,8):        
                    driver.find_element_by_xpath("//*[contains(text(), 'See more')]").click() 
            except:
                pass   
            image_text=single_post_div.find('div',{'class':'ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a'})
            one_image_link=single_post_div.find('img',{'class':'i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm bixrwtb6'})
            if one_image_link is not  None:
                if one_image_link.get('src') not in img_list:
                    img_list.append(one_image_link.get('src'))
                    
                    time_of_post=single_post_div.find_all('div',{'class':'qzhwtbm6 knvmm38d'})[1]
                    # print(time_of_post.text)
                    data_list.append(time_of_post.text.replace("-",""))
                    # print(image_text.text.strip(),"IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIiiiiiiiiiiiiiiiiiii")
                    data_list.append(image_text.text)
                    likes=single_post_div.find('span',{'class':'pcp91wgn'})
                    if likes is not None :
                        # print(likes.text)
                        like=likes.text
                    else:
                        like="NO like "
                    # try:
                                                                            
                    comments_section=single_post_div.find('div',{'class':'bp9cbjyn j83agx80 pfnyh3mw p1ueia1e'})
                    if comments_section is not None:
                        comments=comments_section.find_all('div',{'class':'gtad4xkn'})
                        for c in comments :
                            if "Comments" in c.text:
                                comment=c.text
                            else:
                                comment="No Comment" 
                    else:
                            comment="No Comment"    
                    
                    comments_section=single_post_div.find('div',{'class':'bp9cbjyn j83agx80 pfnyh3mw p1ueia1e'})
                    if comments_section is not None:
                        comments=comments_section.find_all('div',{'class':'gtad4xkn'})
                        for c in comments :
                            if "Shares" in c.text:
                                share=c.text
                            else:
                                share="No share" 
                    else:
                        share="No share" 
                                    
                        


                        

                    # time.sleep(5)
                    # one_image_link=single_post_div.find('img',{'class':'i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm bixrwtb6'}).get('src')
                    req = urllib.request.Request(one_image_link.get('src'), headers={'User-Agent': '*'})
                    response = urllib.request.urlopen(req)
                    html = urllib.request.urlopen(req).read()
                    with open('{}'.format(url.split('/')[-1])+str(+image_count)+'.jpeg', 'wb') as f:
                        f.write(html)
                        image_name="{}".format(url.split('/')[-1])+str(+image_count)

                        data_list.append(like)
                        data_list.append(comment)
                        data_list.append(share)

                        data_list.append(image_name)
                        data_list.append(driver.current_url)
                        data=data_list1+data_list
                        data_frame=pd.DataFrame([data])

                        data_frame.to_csv('test.csv',mode="a" ,header=False)    
                        # print(data) 
                        image_count=image_count+1

                        data_list.clear()   
                        print('done') 
                else:
                    pass   

        except:
            pass    
    # for _ in range(20):
    #         actions.send_keys(Keys.SPACE).perform()
data_list1.clear()                      



