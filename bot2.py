from lib2to3.pgen2 import driver
import os 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from importlib.resources import path
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys   import Keys
from random import randint
import pandas as pd




BASE_DIR=os.path.dirname(os.path.abspath(__file__))
FOX_DIR=os.path.join(BASE_DIR,'geckodriver.exe')
AD_URL='https://www.instagram.com/'

class BOT:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=FOX_DIR)

    def loginlink (self):
       self.driver.get(AD_URL)
       sleep(5)
       #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()

    def userpasskey(self):
        user_id=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))
        user_id.click()
        user_id.send_keys('learntestpython123')

       # user_password =self.driver.find_element_by_css_selector('div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        user_password=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))
        user_password.click()
        user_password.send_keys('22815905258')

        btn = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.bkEs3')))
        btn.click()
        sleep(10)

        notnow=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button.sqdOP:nth-child(1)')))
        notnow.click()
       
        notnow2=WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button._a9--:nth-child(2)')))
        notnow2.click()

    def like_photo(self,hashtag,steps):
        hashtag_url='https://www.instagram.com/explore/tags/'+hashtag
        self.driver.get(hashtag_url)
        sleep(5)   

        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article'))).click()
        i = 1
        while i <= steps:
            sleep(3)
            like=WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'._aamw > button:nth-child(1)')))
            like.click()
            sleep(5)
            
            nextpost=WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'._aaqg > button:nth-child(1)')))
            nextpost.click()
            i = i+1

    def fallow(self):
        hashtag_list = ['bug']

        prev_user_list = [] # if it's the first time you run it, use this line and comment the two below
        #prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
        #prev_user_list = list(prev_user_list['0'])

        new_followed = []
        tag = -1
        followed = 0
        likes = 0
        comments = 0

        for hashtag in hashtag_list:
            tag += 1
            self.driver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
            sleep(5)
            #first_thumbnail = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.,'//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')))
            first_thumbnail=WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'._aaq8 > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')))
            first_thumbnail.click()
            sleep(randint(1,2))    
            try: 
                    
                for x in range(1,5):
                    username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,('._aaqt > div:nth-child(1) > div:nth-child(1)')))).text
                    if username not in prev_user_list:
                            # If we already follow, do not unfollow

                        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button._acan:nth-child(2) > div:nth-child(1) > div:nth-child(1)'))).text == 'Follow':

                            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button._acan:nth-child(2) > div:nth-child(1) > div:nth-child(1)'))).click()
                            sleep(3)
                            
                            new_followed.append(username)
                            followed += 1
                            button_like = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'._aamw > button:nth-child(1)')))
                            button_like.click()
                            likes += 1
                              # Comments and tracker
                            comm_prob = randint(1,10)
                            print('{}_{}: {}'.format(hashtag, x,comm_prob))
                            if comm_prob > 7:
                                comments += 1
                                webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                                comment_box = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea')

                                if (comm_prob < 7):
                                    comment_box.send_keys('بهبه عجب آموزشی!')
                                    sleep(1)
                                elif (comm_prob > 6) and (comm_prob < 9):
                                    comment_box.send_keys('خسته نباشید :)')
                                    sleep(1)
                                elif comm_prob == 9:
                                    comment_box.send_keys('خدا قوت!!')
                                    sleep(1)
                                elif comm_prob == 10:
                                    comment_box.send_keys('مطلب مفیدی بود! :)')
                                    sleep(1)
                                # Enter to post comment
                                comment_box.send_keys(Keys.ENTER)
                                sleep(randint(22,28))


                        nextpost=WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'._aaqg > button:nth-child(1)'))).click()   
                        sleep(randint(3,9))
                    else:
                        #webdriver.find_element_by_link_text('Next').click()
                        nextpost=WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'._aaqg > button:nth-child(1)'))).click()
                        sleep(randint(10,13))
            except:
                continue 
        for n in range(0,len(new_followed)):
            prev_user_list.append(new_followed[n])
            
        updated_user_df = pd.DataFrame(prev_user_list)
       # updated_user_df.to_csv('{}_users_followed_list.csv'.format(str("%Y%m%d-%H%M%S")))
        print('Liked {} photos.'.format(likes))
        print('Commented {} photos.'.format(comments))
        print('Followed {} new people.'.format(followed))   
                    
       
if __name__=='__main__':
    bt=BOT()
    
    bt.loginlink()
    bt.userpasskey()
    #bt.like_photo('python',3)
    bt.fallow()