# <사전>

# ex) 목욕탕에서 유재석씨는 캐비넷 3번 열쇠를, 김태호씨는 100번 열쇠를 받았다.
cabinet = {3:"유재석", 100: "김태호"}

# 값 가져오는 방법 1 ( [] 사용 ) 
print(cabinet[3])
print(cabinet[100])

# 값 가져오는 방법 2 (.get 사용)
print(cabinet.get(3))

# 1번, 2번 차이점 : 번호가 비어있을 때 1번은 오류 발생, 2번은 None 처리 
#print(cabinet[5])
print(cabinet.get(5))
print("오류 안나면 출력 되는 문구")

# 기본값 설정
print(cabinet.get(5 , "사용 가능"))

# 특정 키가 있는지 확인
print(3 in cabinet)
print(5 in cabinet)

# String도 키로 가능
cabinet = {"A-3":"유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님 추가 ( 업데이트, 추가 )
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님 ( 삭제 )
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# 둘다 출력
print(cabinet.items())

# 모든 값 지우기
cabinet.clear()
print(cabinet)