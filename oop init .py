# class User:
#     pass
#
# user_1 = User()  #객체를 새로 정의하려면 () 를 당연히 붙혀야함
# #속성추가하는방법
# user_1.id = "001"
# user_1.username="yerin"
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username="jack"

#user 마다 속성을 이렇게 추가하기엔 좀 번거로움. 그럴땐 객체 초기화 init

class User:

    def __init__(self, user_id, username):  #이 함수에는 user_id 와 username 두가지 파라미터가 꼭 들어가야 한다.
        self.id = user_id       # user_id 가 self.id 로 이름이 변경된걸 잘 기억해야 한다.
        self.username = username
        self.followers = 0 #기본값을 넣음, 위에 파라미터 필요x

user_1 = User("001","yr")
print(user_1.id) #출력시에 self.id 에서 self 만 이름을 바꿔준다
print(user_1.followers)