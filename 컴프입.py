#1
from random import randint

#주사위2개의 눈이 같을 확률
total=100000
same=0
for i in range(total):
    first = randint(1, 6)
    second = randint(1, 6)
    if first == second:
        same += 1

#100,000번 던져 두 눈이 같게되는 횟수, 비율
count_same = 0
for s in range(1,100001):
    first_2 = randint(1, 6)
    second_2 = randint(1, 6)
    if first_2 == second_2:
        count_same += 1

print(f"던진 주사위의 횟수: {s}, 두 눈이 같은 횟수: {count_same}")
print(f"두 주사위의 눈이 같을 확률: {same/total}, 두 눈이 같은 비율: {count_same/s}")


#2
bit = input("이진수를 입력하세요: ")
bit_rever = bit[::-1] #계산을 위해 받은거 뒤집기

ten = 0  #ten이 for문 안에 있으니 적용이 안됨
for number in range(0, len(bit)):
    bit_2 = 2**number
    result = bit_2 * int(bit_rever[number])
    ten = ten + result

print(f"{bit}에 대한 10진값: {ten}")


# 3

dec_2 = input("(10진) 자연수를 입력하세요: ")
dec = int(dec_2)
ls = []
while dec > 0: #정수면 계속 돌거야
    ls_2 = dec % 2
    ls.append(ls_2)
    dec = dec // 2

ls.reverse()
ls = "".join(map(str, ls))
print(f"{dec_2}에 대한 2진수: {ls}")



문제 : 
첨부 파일 gettysburg.txt 파일을 사용하여 키(key)가 단어이고 값(value)은 단어가 나타난 줄 번호 리스트인 딕셔너리를 만들고, 
키(key)인 단어의 알파벳 순으로 파일 (data/word_frequency.dat’)에 저장하는 프로그램을 작성하시오.


# 딕셔너리 추가하는법!! 무에서 유를 창조
words_dict = {}
words_dict['word'] = [2]
print(words_dict)


def read_file(filename):
    special_ch = '~`@#$%^.&*,()-_+="<>][;:?' + "'"
    words_dict = {}
    line_num = 0
    with open ('C:/Users/yerin/pythonProject/gettysburg.txt','r') as infile:
        for line in infile:
            line_num += 1
            for ch in special_ch:
                line = line.replace(ch,"")
            words_list = line.split()
            for word in words_list:  # 하나의 line_num 안에서 계속 돔
                word = word.lower()
                if word in words_dict:  # 처음엔 words_dict 는 정의된게 없고
                    words_dict[word].append(line_num)
                else:           # 이부분에서 words_dict 의 내용이 생성이됨
                   words_dict[word] = [line_num]

    return words_dict #모든문장을 한번에 받기위해 줄을 with 과 맞춰준다.

def save_line_num(filename, words_dict):
    with open(filename, 'w') as outfile:
        for word in sorted(words_dict): #오름차순으로 빼서 정리함
            outfile.write(f'{word:12s}:')  # 단어먼저써지고
            for line_num in words_dict[word]:
                outfile.write(f'{line_num}')  # 그옆에 이어서 라인넘버써짐 , (여러개면 여러개써짐)
            outfile.write('\n')  #그리고 줄바꿈

#1. def read_file => 각 line_number 안에서 words_dict 를 반환  EX) words_dict[word] = [line_num]
#2. def save_line_num => 그 words_dict 를 가지고 for문을 이용해 한줄한줄 글로 작성.

if __name__=='__main__':
    input_file = 'C:/Users/yerin/pythonProject/gettysburg.txt'
    output_file = 'C:/Users/yerin/pythonProject/word_frequency_2.dat'
    words_d = read_file(input_file)
    save_line_num(output_file,words_d)

