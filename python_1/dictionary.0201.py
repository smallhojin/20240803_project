d = {"key":"value", 2.3: "value", 5:1, 5:"111"}
print(d)

print(d.keys())
print(d.values())




#자판기 프로그램 짜기
#사용자모드 / 관리자 모드
#사용자 모드: 물건 구매
#관리자 모드: 물건 추가, 물건 가격 변경
"""
#사용자 모드 - 처음에 음료 종류 10가지 제시, 음료를 선택하라는 창 띄우기
           - 사용자가 음료 이름 입력하기
           - 물건이 0개면 해당 항목 사용 불가
           - 다른 항목을 선택해 달라는 창을 띄우기
           - 총 10종류의 물건 중 0개인 항목이 5개가 되면 사용자 모드 사용 불가
           - 관리자 모드로 전환되며 관리자 비번 드는 창으로 전환 
           - 자신이 직접 선택하는 것 말고 자판기가 랜덤으로 선택해 주는 기능 
           - 결재 방식 선택하기(현금, 카드)
#관리자 모드 - 물건 상한선 50개
           - manager치고 비번 치면 관리자 모드로 전환
           - 물건 숫자, 물건 가격 자유롭게 기존 숫자에 추가 및 변경 가능
           - 음료 이름 변경 가능
"""
inventory = {}
