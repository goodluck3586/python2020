#region 5. 온라인 장바구니
# 데이터: 장바구니 리스트
# 입력: 없음
# 출력: 장바구니 안의 정보와 총 지불 금액
#endregion

# Basket 클래스 정의
class Basket:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.prices = []
        self.quantity = []
        self.total = 0
        self.noitems = 0
    
    # item 추가
    def add(self, item, price, qty):
        self.items.append(item)
        self.prices.append(price)
        self.quantity.append(qty)
        self.total += price * qty
        self.noitems += 1

    # item 삭제
    def delete(self, item, qty):
        # 전체 item 개수만큼 반복
        for i in range(self.noitems):
            if item == self.items[i]:               # 해당 아이템을 찾으면
                self.quantity[i] -= qty             # 전체 아이템 개수 - 삭제 개수
                self.total -= self.prices[i] * qty  # 총액 삭감

                # 모든 아이템이 삭제된 경우
                if self.quantity[i] == 0:           
                    self.noitems -= 1       # 아이템 개수 1 감소
                    del self.items[i]       
                    del self.quantity[i]
                    del self.prices[i]
                break

    # 모든 아이템 출력
    def printItems(self):
        print(f"{self.id}의 장바구니")
        for i in range(self.noitems):
            print(self.items[i], self.prices[i], self.quantity[i])
        print(f'** total = {self.total}, noitems = {self.noitems}')

cjBasket = Basket("영희")
jsBasket = Basket("철수")

cjBasket.add("바나나", 5000, 2)
cjBasket.add("우유", 2500, 1)
jsBasket.add("라면", 5900, 1)
jsBasket.add("커피", 5000, 2)

cjBasket.printItems()
jsBasket.printItems()




















