#  <문자열처리함수>

python = "Python is Amazing"

# 소문자변환 함수
print(python.lower())

# 대문자변환 함수
print(python.upper())

# 대문자인지 확인하는 함수
print(python[0].isupper())
print(python[1].isupper())

# 문자열 길이 반환 함수
print(len(python))

# 문자 바꾸는 함수
print(python.replace("Python", "Java"))

# 문자가 몇 번째 위치하고 있는지 알려주는 함수
index = python.index("n")
print(index)

index = python.index("n", index + 1) # 특정 위치 뒤부터 찾기
print(index)

print(python.find("n"))

# find vs index
#print(python.index("Java")) => 없으면 오류 발생
#print(python.find("Java")) => 없으면 -1 반환

#문자열에 특정 문자가 몇번 들어가는지 알려주는 함수
print(python.count("n"))