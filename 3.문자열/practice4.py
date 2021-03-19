# <문자열포맷>

#print("a" + "b")
#print("a", "b")  외에 다른 거 알아보기

# 방법 1
print("나는 %d살입니다." %20) # 정수
print("나는 %s을 좋아해요." %"파이썬") # 문자열(String)
print("Apple은 %c로 시작해요." %"A") # 문자(char)
print("나의 성은 %s로 시작해요" %"P") #문자를 문자열로 처리
print("오늘은 %s일 입니다." % 1) # 정수를 문자열로 처리 
print("오늘은 %s년 %s월 입니다." % (2021,3)) 
print("나의 이니셜은 각각 %s, %s, %s입니다." %("P","S","H"))
print("내가 태어난 월은 %s월이고, 별자리는 %s입니다." % ("20", "염소자리") )

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4 (v3.6 이상~)
age = 21
color = "파랑"
print(f"나는 {age}살이며, {color}색을 좋아해요.")