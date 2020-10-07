from selenium import webdriver
import time

def fField(b):
    # for i in range(11):
    i = "1"
    t = b.get('https://tse.europe.travian.com/build.php?id='+i)
    print(t)
    b1 = b.find_element_by_class_name("section1")
    print(f"!!! {b1}")

def main():
    b = webdriver.Chrome('/home/vyacheslavtr/MyPython/selenium/chromedriver')
    b.get('https://tse.europe.travian.com/login.php')
    login = b.find_element_by_name("name").send_keys('trg')
    time.sleep(0.5)
    l_pass = b.find_element_by_name("password").send_keys('QWWQtrg')
    time.sleep(0.5)
    # print(login, l_pass)
    tap = b.find_element_by_css_selector("button").click()
    # b.get('https://tse.europe.travian.com/hero.php?t=3') # Преключения
    fField(b)
    time.sleep(10)
    #tap = browser.find_element_by_class_name("textButtonV1 green ").click()
    b.close
    

    

if __name__ == "__main__":
    main()

#     <a id="button5f7a049b73ef4" class="layoutButton buttonFramed withIcon round adventure green   " href="/hero.php?t=3">
# 					<svg viewBox="0 0 19.75 20" class="adventure"><g class="outline">
#   <path d="M7.82 5L11 8.14 9.22 9.92 6 6.74 2.86 9.92 1.08 8.14 4.26 5 1.08 1.78 2.86 0 6 3.18 9.22 0 11 1.78zm6.83 9.92a2.56 2.56 0 1 0 2.56 2.56 2.56 2.56 0 0 0-2.56-2.6zm-3.55 2.6s-2-.26-4.21-.73A14.89 14.89 0 0 1 2.6 15.4c.55-.37 2.13-1.1 6.49-2 7.6-1.58 10.69-3.1 10.66-5.25 0-1.86-2.44-2.86-4.26-3.45a30.7 30.7 0 0 0-3.58-.9l-.42 2.32c2.85.52 5.31 1.47 5.84 2.06-.32.35-1.82 1.48-8.72 2.91-6.27 1.3-8.68 2.53-8.61 4.39C.06 17 1.8 18 5.83 19c2.46.57 4.87.88 5 .9z"></path>
# </g><g class="icon">
#   <path d="M7.82 5L11 8.14 9.22 9.92 6 6.74 2.86 9.92 1.08 8.14 4.26 5 1.08 1.78 2.86 0 6 3.18 9.22 0 11 1.78zm6.83 9.92a2.56 2.56 0 1 0 2.56 2.56 2.56 2.56 0 0 0-2.56-2.6zm-3.55 2.6s-2-.26-4.21-.73A14.89 14.89 0 0 1 2.6 15.4c.55-.37 2.13-1.1 6.49-2 7.6-1.58 10.69-3.1 10.66-5.25 0-1.86-2.44-2.86-4.26-3.45a30.7 30.7 0 0 0-3.58-.9l-.42 2.32c2.85.52 5.31 1.47 5.84 2.06-.32.35-1.82 1.48-8.72 2.91-6.27 1.3-8.68 2.53-8.61 4.39C.06 17 1.8 18 5.83 19c2.46.57 4.87.88 5 .9z"></path>
# </g></svg>
# 		</a>