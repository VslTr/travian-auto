from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random


def f_field(b):
    count1 = 1
    f = {1: 333, 2: 333, 3: 333, 4: 333, 5: 333, 6: 333, 7: 333, 8: 333, 9: 333, 10: 333,
     11: 333, 12: 333, 13: 333, 14: 333, 15: 333, 16: 333, 17: 333, 18: 333}

    for i in range(1, 19):
        t = b.get('https://ts5.anglosphere.travian.com/build.php?id=' + str(i))
        try:
            b1 = b.find_element_by_xpath('//button[@class="textButtonV1 green build"]').text
            sleep(random.randint(2, 5))
            b.find_element_by_id('closeContentButton').click()
            f[i]=int(b1[-1])
            sleep(1)
            count1 += 1
            if count1 == 18: break
        except:
            print(f"no such upgrade field: {str(i)}")
            b.find_element_by_id('closeContentButton').click()
            sleep(random.randint(2, 5))
            f[i]= 999
            count1 += 1
            if count1 == 18: break

    count2 = 0 # Counter of field ready to upgrade
    count3 = 0 # Counter field to upgrade

    for j in f:
        if f[j] < 33: count2 += 1

    if count2 <= 1: count3 = 1

    m = min(f.values())
    print(f'Min: {m}')

    if m < 333:
        for key in f:
            if f[key] == m:
                    print(f"Field:{key} Level:{f[key]}")
                    try:
                        b.get('https://ts5.anglosphere.travian.com/build.php?id=' + str(key))
                        clk = b.find_element_by_xpath('//button[@class="textButtonV1 green build"]')
                        clk.click()
                        count3 += 1
                        sleep(random.randint(2, 10))
                    except:
                        sleep(random.randint(2, 10))
                        count3 += 1
                        break
                    
            if count3 == 2: break

    print(f)
  

def main():

    while True:
        # b = webdriver.Chrome('C:\Projects\github.com\VslTr\python\selenium\chromedriver.exe')
        b = webdriver.Chrome(ChromeDriverManager().install())
        b.get('https://ts5.anglosphere.travian.com//login.php')
        login = b.find_element_by_name("name").send_keys('----')
        sleep(random.randint(2, 5))
        l_pass = b.find_element_by_name("password").send_keys('----')
        sleep(random.randint(2, 5))
        tap = b.find_element_by_css_selector("button").click()
        f_field(b)
        time = random.randint(300, 900)
        print(f"Pause: {time} s")
        print(" ")
        b.quit()

        for i in range(time + 1):
            print(time - i, end='')
            print('\r', end='')
            sleep(1)



if __name__ == "__main__":
    main()

