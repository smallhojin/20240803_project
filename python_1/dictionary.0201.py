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
"""
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
"""
"""
#처음에 가지고 있는돈 50000,10000,5000원 고정
user_input = input("음료를 선택하여 주세요")
if user_input == "coke":
    print("가격은 1500원 입니다")
    num_drink = int(input("몇개를 구매하실 건가요?"))
    user_input_2 = int(input("얼마를 가지고 계신가요?"))
    if user_input_2 == 50000:
        if num_drink <= 33:
            print("거스름돈은", int(50000 - 1500 * num_drink), "원 입니다")
        else :
            print("돈이 부족합니다")
    if user_input_2 == 10000:
        if num_drink <= 6:
            print("거스름돈은", int(10000 - 1500 * num_drink), "원 입니다")
        else :
            print("돈이 부족합니다")
    if user_input_2 == 5000:
        if num_drink <= 3:
            print("거스름돈은",int(5000-1500*num_drink),"원 입니다")
        else :
            print("돈이 부족 합니다.")
elif user_input == "soft drink":
    print("가격은 1000원 입니다")
    num_drink = int(input("몇개를 구매하실 건가요?"))
    user_input_2 = int(input("얼마를 가지고 계신가요?"))
    if user_input_2 == 50000:
        print("거스름돈은",int(50000-1500*num_drink),"원 입니다")
"""
class VendingMachine:
    def __init__(self):
        # 자판기 음료 목록과 가격 설정
        self.drinks = {
            '콜라': 1500,
            '사이다': 1200,
            '환타': 1300,
            '커피': 2000,
            '물': 1000
        }

    def display_drinks(self):
        # 음료 목록과 가격 출력
        print("음료 목록과 가격:")
        for drink, price in self.drinks.items():
            print(f"{drink}: {price}원")

    def purchase_drink(self):
        # 음료 선택 및 수량, 가격 확인
        self.display_drinks()

        # 음료 선택
        drink_choice = input("구매할 음료를 선택하세요: ")

        # 선택한 음료가 유효한지 확인
        if drink_choice not in self.drinks:
            print("선택한 음료는 자판기에 없습니다. 다시 시도하세요.")
            return

        # 수량 입력
        while True:
            try:
                quantity = int(input(f"{drink_choice}의 수량을 입력하세요 (1 이상): "))
                if quantity < 1:
                    print("수량은 1 이상이어야 합니다. 다시 입력하세요.")
                else:
                    break
            except ValueError:
                print("유효한 수량을 입력하세요.")

        # 가격 확인 및 계산
        total_price = self.drinks[drink_choice] * quantity
        print(f"{drink_choice} {quantity}개의 가격은 {total_price}원입니다.")

        # 사용자가 지불할 금액 입력
        while True:
            try:
                paid_amount = int(input(f"{total_price}원을 지불하세요: "))
                if paid_amount < total_price:
                    print(f"금액이 부족합니다. {total_price}원을 지불해야 합니다.")
                else:
                    break
            except ValueError:
                print("유효한 금액을 입력하세요.")

        # 거스름돈 계산
        change = paid_amount - total_price
        if change > 0:
            print(f"거스름돈은 {change}원입니다.")
        print("구매가 완료되었습니다. 즐거운 하루 되세요!")


# 자판기 객체 생성 및 사용
vending_machine = VendingMachine()
vending_machine.purchase_drink()


print_menu()
drink_key = select_drink()
if drink_key != -1:
    buy_drink(drink_key)

def select_drink():
    global inventory

    drink = int(input("메뉴를 선택하세요"))

    if drink == 1:
        drink_key = 'coke'
       # inventory.update({'coke': inventory['coke'] + 1})
    elif drink == 2:
        inventory['chill sung'] = inventory['chill sung'] + 1
    elif drink == 3:
        inventory['chocolate milk'] = inventory['chocolate milk'] + 1
    elif drink == 4:
        inventory['strewberry milk'] = inventory['strewberry milk'] + 1
    elif drink == 5:
        inventory['banana milk'] = inventory['banana milk'] + 1


    if inventory[drink_key] == 0:
        print("선택한 음료의 수량이 부족합니다.")
        return -1
    else:
        inventory[drink_key] =inventory[drink_key] -1
        return drink_key
def buy_drink(drink_key: int):
    coin = 0
    while price[drink_key] > coin:
        print("금액을 입력하세요")
        coin = coin + int(input(">>"))

    print(coin - price[drink_key], "원을 반환합니다")