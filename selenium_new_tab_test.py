from selenium import webdriver
# import JavascriptExecutor

chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver_dir)
driver.get("http://yahoo.com")

# 새로운 탭 생성
driver.execute_script("window.open()")
tabs = driver.window_handles

print(tabs)

# 새로운 탭을 구글홈페이지로 전환
# 현재 떠져있는 창이 두번째 창이라도
# driver.get 등의 driver메소드는 원래의 첫번째 창에 적용이 됨
# 그래서 switch_to를 해줘야 함
driver.switch_to.window(tabs[-1])
driver.get("http://google.com")


driver.close()

# 첫번째 창으로 다시 돌아옴
driver.switch_to.window(tabs[0])
driver.get('https://google.com')
