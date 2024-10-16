import requests
import bs4
import pandas as pd



url = 'http://apis.data.go.kr/openapi/service/ElevatorOperationService/getOperationInfoList?serviceKey=FdZ%2BYFNFFCi%2FRJ0pFSzDx2uu6VMCGkzBCrVaFikqQb7Gd6Cxpz%2BqKm80th92%2FE9KOI3LicXYK1NRNsXLTvqOpQ%3D%3D&pageNo=1&numOfRows=10000&buld_address=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EA%B0%95%EB%82%A8%EA%B5%AC'
params = {
    'serviceKey': 'FdZ+YFNFFCi/RJ0pFSzDx2uu6VMCGkzBCrVaFikqQb7Gd6Cxpz+qKm80th92/E9KOI3LicXYK1NRNsXLTvqOpQ==', 
    'pageNo': '1', 
    'numOfRows': '200000',
    'buld_address': '서울특별시 강남구'
    
}

response = requests.get(url, params=params)
content = response.text

# 응답 내용 출력
print("응답 내용:\n", content)

# XML 파싱
soup = bs4.BeautifulSoup(content, 'lxml-xml')
items = soup.find_all('item')

if not items:
    print("조회된 데이터가 없습니다.")
else:
    # 데이터 추출
    row_list = []
    name_list = []
    value_list = []

    for i, item in enumerate(items):
        columns = item.find_all()
        for j, column in enumerate(columns):
            if i == 0:
                name_list.append(column.name)
            value_list.append(column.text)
        row_list.append(value_list)
        value_list = []

    # DataFrame 생성
    elevator_df = pd.DataFrame(row_list, columns=name_list)
    print(elevator_df.head())
    elevator_df.to_csv('elevator_df.csv', encoding='utf-8-sig')
