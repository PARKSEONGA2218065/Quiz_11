class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

# 음료 메뉴 및 객체 초기화
coffee = Beverage("커피", 3000)
green_tea = Beverage("녹차", 2500)
ice_tea = Beverage("아이스티", 3000)

selected_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")

if selected_beverage == "커피":
    selected_object = coffee
elif selected_beverage == "녹차":
    selected_object = green_tea
elif selected_beverage == "아이스티":
    selected_object = ice_tea
else:
    print("잘못된 음료명입니다.")
    exit()

quantity = int(input(f"{selected_beverage}의 수량을 입력하세요: "))

# 총 가격 계산 및 출력
total_cost = selected_object.calculate(quantity)
print(f"{selected_beverage} {quantity}잔 - 총 가격: {total_cost}원")
