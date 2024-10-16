
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# 웹 드라이버 시작
driver = webdriver.Chrome()

# 지정한 URL 열기
url = "https://www.elevator.go.kr/opn/info/ComElvtrNumAddrNewL01.do?wccPrm=s4KKuwE0iGU1yIU4iiDy8szxnle2xBwCP3D6%2BkLV0ec1vPOpgHCBxDqbgOfO2SK8bGiX1ESoVkt%2FaL4yb0gqToYg3N6Ukosx82foxtB3eShYX1jfri%2Bxbt2D4A8YVwf22VgS38exaw6e%2BoxGE4J1ig%3D%3D"
driver.get(url)
time.sleep(5)

# CSS 선택자를 사용하여 요소 선택 (서울시)
option_selector = "#sido > option:nth-child(2)"
option_element = driver.find_element(By.CSS_SELECTOR, option_selector)
time.sleep(2)
option_element.click()

time.sleep(2)
# CSS 선택자를 사용하여 요소 선택 (강남구)
option_selector = "#sigungu > option:nth-child(2)"
option_element = driver.find_element(By.CSS_SELECTOR, option_selector)
time.sleep(2)
option_element.click()

time.sleep(2)

# CSS 선택자를 사용하여 요소 선택 (강남대로)
option_selector = "#address1"
option_element = driver.find_element(By.CSS_SELECTOR, option_selector)
time.sleep(1)
option_element.click()
time.sleep(2)
# '강남대로'라는 글을 입력
option_element.send_keys('강남대로')
time.sleep(1)

# CSS 선택자를 사용하여 요소 선택 ('검색')
option_selector = "#btnSearch"
option_element = driver.find_element(By.CSS_SELECTOR, option_selector)
time.sleep(1)
option_element.click()

time.sleep(3)

# CSS 선택자를 사용하여 요소 선택 ('승강기 번호 추적 & 리스트로 저장')
option_selector = "#tbody_selectList > tr:nth-child(1) > td:nth-child(1) > a"
option_element = driver.find_element(By.CSS_SELECTOR, option_selector)
time.sleep(1)


# 승강기 번호 추출
elevator_numbers = [elem.text for elem in option_element]

# DataFrame 생성
df = pd.DataFrame(elevator_numbers, columns=['승강기번호'])

# CSV 파일로 저장
df.to_csv('elevator_numbers.csv', index=False, encoding='utf-8-sig')



# 필요에 따라 브라우저를 종료하려면
time.sleep(2)
driver.quit()
