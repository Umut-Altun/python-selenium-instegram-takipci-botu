from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = ""
password = ""

class Instegram:
#---- 1.bolum ----
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def kullaniciGiris(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, "._acan._acap._acas._aj1-").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,"button[type='button']").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'._a9-z').find_element(By.CSS_SELECTOR,"._a9--._a9_0").click()
        time.sleep(3)
#---- 2.bolum ----
    def takipciAl(self):
        self.driver.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR,".x78zum5.x1q0g3np.xieb3on").find_element(By.TAG_NAME,"a").click()
        time.sleep(3)

        users = self.driver.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")

        for user in users:
            text = user.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade").text
            print(text)

    def tumTakipcileriAl(self):
        self.driver.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR,".x78zum5.x1q0g3np.xieb3on").find_element(By.TAG_NAME,"a").click()
        time.sleep(3)
        
        fallowerList = self.driver.find_element(By.CSS_SELECTOR,"div[role=dialog]")
        fallowerCount = len(fallowerList.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
        print(f"Gelen takıpcı sayısı: {fallowerCount}")

        while True:
            fallowerList.click()
            scroll_count = 4  
            for i in range(scroll_count):
                # Sayfada aşağıya doğru kaydırmak için PAGE_DOWN tuşuna basıyoruz
                self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
            
            newCount  = len(fallowerList.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
            if fallowerCount != newCount:
                fallowerCount = newCount
                print(f"toplam takıpcı sayısı: {newCount}")
                time.sleep(1)
            else:
                break


        fallower = fallowerList.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        for user in fallower:
            text = user.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade").text
            print(text)
#---- 3.bolum ----
    def takipEt(self,insUser):
        self.driver.get(f"https://www.instagram.com/{insUser}/")
        time.sleep(3)

        fallowButton = self.driver.find_element(By.CSS_SELECTOR,("._aacl._aaco._aacw._aad6._aade"))
        # print(fallowButton.text)
        # time.sleep(1)
        if fallowButton.text != "Takiptesin":
            fallowButton.click()
        else:
            print("Zaten Takıp Edılıyor !")
            
    def takipBirak(self,insUser):
        self.driver.get(f"https://www.instagram.com/{insUser}/")
        time.sleep(3)
        fallowButton = self.driver.find_element(By.CSS_SELECTOR,("._aacl._aaco._aacw._aad6._aade"))
        if fallowButton.text != "Takip Et":
            fallowButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div/div/div/span/span').click()
            time.sleep(2)
        else:
            print("Zaten Takıpte Degilsin !")
#---- 4.bolum ----
    def takipciKaydet(self):
        self.driver.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR,".x78zum5.x1q0g3np.xieb3on").find_element(By.TAG_NAME,"a").click()
        time.sleep(3)
        
        fallowerList = self.driver.find_element(By.CSS_SELECTOR,"div[role=dialog]")
        fallowerCount = len(fallowerList.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
        print(f"Gelen takıpcı sayısı: {fallowerCount}")

        while True:
            fallowerList.click()
            scroll_count = 12  
            for i in range(scroll_count):
                # Sayfada aşağıya doğru kaydırmak için PAGE_DOWN tuşuna basıyoruz
                self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
            
            newCount  = len(fallowerList.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
            if fallowerCount != newCount:
                fallowerCount = newCount
                print(f"toplam takıpcı sayısı: {newCount}")
                time.sleep(1)
            else:
                break

        users = fallowerList.find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        
        fallowerList = []
        for user in users:
            fallowerName = user.find_element(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade").text
            fallowerList.append(fallowerName)
        
        with open("takipciler.txt","w",encoding="utf-8") as file:
            for fallower in fallowerList:
                file.write(fallower + "\n")

    def cikis(self):
        self.driver.quit()

ınstgrm = Instegram(username,password)
ınstgrm.kullaniciGiris()
ınstgrm.takipciAl()
ınstgrm.tumTakipcileriAl()
ınstgrm.takipEt("huawei")
ınstgrm.takipBirak("huawei")
ınstgrm.takipciKaydet()
ınstgrm.cikis()
