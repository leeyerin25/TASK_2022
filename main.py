
# import mypy
class Product:

    discount_rate = 0.1 #Product 인스턴스에서 공유가능

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def get_price(self):
        return int((1 - self.discount_rate) * self.__price * self.__quantity)

    def __str__(self):
        return f'{self.__name:30s}\t{self.__price:5d}원{self.__quantity:3d}개'


class ShoppingCart:
    def __init__(self):
        self.__shop_list = []

    def add(self, pdt):
        self.__shop_list.append(pdt)

    def delete(self, pdt, qty):
        #updated = False
        for p in self.__shop_list: #shop_list 들어오는 상품 하나하나 검색함
            if p.name == pdt.name: #그 들어온 상품하나하나의 이름이 가지고 있는 pdt 와 같을때!
                p.quantity = p.quantity - qty
                #updated = True
                if p.quantity <= 0:
                    self.__shop_list.remove(p)
                    break



    def total_price(self):
        '''총가격을 계산해줌'''
        total = 0
        for product in self.__shop_list:
            total += Product.get_price(product)
        return int(total)
        #소수점 안나오는법??

    def billing(self):
        '''영수증을 출력해준다'''
        result = f'구입 품목: \n\n'
        for product in self.__shop_list:
            result += f'{product.name:20s} {product.quantity:10d}개\t {Product.get_price(product)} \n'
        result += f'{45 * "-"}\n'
        result += f'{"합계":35s} {self.total_price()} \n'
        return result


    def __str__(self):
        info = f'{"구매 품목이름":33s} {"단가":8s} {"수량":5s} \n'
        for shop in self.__shop_list:
            info += f'{shop}\n'
        return info
        # shop_list 에 여러 상품이 들어가게끔 코딩


if __name__ == '__main__':
    # 상품먼저 정의
    product1 = Product('제주 삼다수 그린2L', 1200, 5)
    product2 = Product('신라면(120g*5입)', 4100, 2)
    product3 = Product('CJ 햇반(210g*12입)',  13980, 1)
    product4 = Product('몽쉘크림(12입)', 4780, 1)
    products = [product1, product2, product3, product4]

    '''문제 2번'''
    # 쇼핑카트 클래스를 객체로 생성
    shopping = ShoppingCart()
    # add 이용하여 shoplist 에 품목 집어넣기
    for product in products:
        shopping.add(product)
    print(shopping)

    ''' 문제 3번 '''
    # 제품삭제
    shopping.delete(product4, 1)

    # 제품추가
    shopping.add(Product('해태 구운감자(135g*5입)', 3580, 2))
    print(shopping)


    ''' 문제 4번 '''
    print(shopping.billing())











