# <세트>

# 세트란? 집합, 중복이 안되고 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

mudo = {"유재석", "박명수", "정형돈"}
runningman = set({"유재석", "김종국"})

# 교집합 출력
print (mudo & runningman)
print (mudo.intersection(runningman))

# 합집합 출력
print (mudo | runningman)
print (mudo.union(runningman))

# 차집합 출력
print (mudo - runningman)
print (mudo.difference(runningman))

# 런닝맨 멤버 추가 ( 값 추가 )
runningman.add("송지효")
print(runningman)

# 무도 하차 ( 값 제거 )
mudo.remove("정형돈")
print(mudo)