# Quiz) 다음과 같은 형태로 1~50주차, 주 1회 보고서 파일을 만드는 프로그램을 작성하시오

# - X 주차 주간보고- 
# 부서:
# 이름:
# 업무 요약:

# 조건1 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만들기

for week in range(1,51):
    with open(str(week) + "주차.txt","w",encoding="utf8") as report_file:
        report_file.write("- {} 주차 주간보고-".format(week))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")