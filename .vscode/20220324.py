#1
letters = 'python'
print(letters[0], letters[2])
#2
string = "PYTHON"
rev = ' '
for a in string:
    rev = a + rev
print(f'reverse : {rev}')
#3
url = "http://sharebook.kr"
url_index = url.split('.')
print(url_index[-1])
#4
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
#5
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))
#6
score = input("score :")
score = int(score)
if 81 <= score:
    print("A")
elif 61 <= score:
    print("B")
elif 41 <= score:
    print("C")
elif 21 <= score:
    print("D")
else:
    print("E")
#7
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
#8
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
종목명 = input("종목명 : ")
if 종목명 in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
#9
리스트 = [100, 200, 300]
for a in 리스트:
    print( a +10 )
#10
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for a in 리스트:
    print(len(a))