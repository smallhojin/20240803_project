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


inventory = {'콜라':10, '사이다':10, '초코 우유':10, '데미 소다':10, '바나나 우유':10, '웰치스':10, '물':10}
price = {'콜라':1500, '사이다':1500, '초코 우유':1000, '데미 소다':1200, '바나나 우유':1000, '웰치스':1300, '물':500}

mode = "manager"

def print_menu():
    print("menu를 출력합니다.")
    for i in inventory.keys():
        print(i, "가격:", price[i], " 잔여수량:", inventory[i])

def buy_drink():
    print("음료를 선택하고, 구매합니다.")

def switch_mode():
    print("모드를 전환합니다.")
    global mode
    if mode == "manager":
        mode = "user"
    else:
        mode = "manager"

def manager_login():
    print("관리자 모드에 진입합니다.")
def pass_word():
    input('관리자 비번을 입력해 주세요')
    pword = input
def print_function():
    print("관리자가 사용가능한 기능을 출력합니다.")
    print("1. 음료를 등록하기")
    print("2. 음료를 추가하기")
    print("3. 음료를 빼기")
    print("4. 음료를 삭제하기")
    print("5. 사용자 모드로 전환")

def change_price():
    print("음료의 가격을 변경합니다.")

def add_drink():
    print("음료를 추가합니다.")

def register_drink():
    print("음료를 등록합니다.")

def delete_drink():
    print("음료를 삭제합니다.")

def extract_drink():
    print("음료를 뺍니다.")

while True:
    if mode == "manager":
        pass_word()
        if pw == '12345678':
            manager_login()
            user_input = int(input("메뉴를 선택하세요"))

            if user_input == 1:
                register_drink()
            elif user_input == 2:
                add_drink()
            elif user_input == 3:
                extract_drink()
            elif user_input == 4:
                delete_drink()
            elif user_input == 5:
                switch_mode()

    else:
        print_menu()
        user_input = input("메뉴를 선택하세요")