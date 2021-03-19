# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) https://www.google.co.kr
# 조건1 : https://www. 부분은 제외 => www.google.co.kr
# 조건2 : 그 다음 점(.) 이후 부분은 제외 => google
# 조건3 : 남은 글자 중 처음 세자리(goo) + 글자 갯수(6) + 글자내 'e' 갯수(1) + "!" 로 구성 

# 출력 문장  : 생성된 비밀번호 : goo61!

url = "https://www.google.co.kr"
rule1 = url.replace("https://www.","") 
rule2 = rule1[:rule1.index(".")]
rule3 = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"

print("생성된 비밀번호 : {}".format(rule3))