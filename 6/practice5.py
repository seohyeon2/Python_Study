# <가변인자>

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") # end => 줄바꿈 대신 " "로 바꿈
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석",20,"파이썬","자바","C","C++","C#")
profile("김태호",25,"코틀린","스위프트","","","")

def profile1(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile1("유재석",20,"파이썬","자바","C","C++","C#","자바스크립트")
profile1("김태호",25,"코틀린","스위프트")