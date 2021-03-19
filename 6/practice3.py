# <기본값>

def profile1(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name,age,main_lang))

profile1("유재석",20,"파이썬")
profile1("김태호",21,"자바")

# 같은 학교, 같은 학년, 같은 반, 같은 수업일 경우 (중복될 경우 => 기본값 설정)

def profile2(name, age=17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name,age,main_lang))

profile2("유재석")
profile2("김태호")