import pandas as pd
import xmltodict

# XML 데이터
xml_data = '''
<response>
<header>
<resultCode>00</resultCode>
<resultMsg>NORMAL SERVICE.</resultMsg>
</header>
<body>
<items>
<item>
<address1>서울시 강남구 삼성동 169-19</address1>
<address2>청담주상복합홍보관 (삼성동)</address2>
<applcBeDt>20240707</applcBeDt>
<applcEnDt>20250706</applcEnDt>
<buldNm>청담주상복합 홍보관</buldNm>
<elevatorNo>0140444</elevatorNo>
<elvtrAsignNo>1</elvtrAsignNo>
<elvtrDetailForm>VVVF</elvtrDetailForm>
<elvtrDiv>엘리베이터</elvtrDiv>
<elvtrForm>권상식</elvtrForm>
<elvtrKindNm>승객용</elvtrKindNm>
<elvtrSttsNm>운행중</elvtrSttsNm>
<frstInstallationDe>20210707</frstInstallationDe>
<inspctInsttNm>서울강남지사</inspctInsttNm>
<installationDe>20210707</installationDe>
<installationPlace>1-1</installationPlace>
<liveLoad>1000</liveLoad>
<mnfcturcpnynm>(주)송산특수엘리베이터</mnfcturcpnynm>
<ratedCap>13</ratedCap>
<ratedSpeed>1</ratedSpeed>
<shuttleFloorCnt>4</shuttleFloorCnt>
<sido>서울</sido>
<sigungu>강남구</sigungu>
</item>
</items>
<numOfRows>1</numOfRows>
<pageNo>1</pageNo>
<totalCount>42</totalCount>
</body>
</response>
'''

# XML 데이터를 딕셔너리로 변환
data = xmltodict.parse(xml_data)

# 필요한 데이터 추출 (엘리베이터 정보)
elevator_info = data['response']['body']['items']['item']

# DataFrame으로 변환
df = pd.DataFrame([elevator_info])  # 리스트로 감싸야 DataFrame이 제대로 생성됩니다.

# CSV 파일로 저장
df.to_csv('elevator_data.csv', index=False, encoding='utf-8-sig')

print("CSV 파일이 생성되었습니다: elevator_data.csv")
