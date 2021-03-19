# <표준입출력>

# sep, end
print("파이썬","자바", sep =",")
print("파이썬","자바", sep =" vs ")
print("파이썬","자바", sep =",", end="?")
print("무엇이 더 재밌을까요?")

# sys.stdout, sys.stderr
import sys
print("파이썬","자바", file=sys.stdout) #표준출력
print("파이썬","자바", file=sys.stderr) #표준에러

# ljust, rjust
# ex)시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust: 왼쪽정렬, rjust: 오른쪽정렬

# zfill
# ex)은행 대기순번표
# 001, 002, 003, ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) #빈공간 채우기

# 표준입출력
answer = input("아무 값이나 입력하새요 : ")
print("입력하신 값은 " + answer + "입니다.")