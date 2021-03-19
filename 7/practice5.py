# <with>

# 피클 사용한 with
'''
import pickle

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))
'''

# 피클 사용 안한 with : 파일 생성 (파일 쓰기)
'''
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
'''

#피클 사용 안한 with : 파일 불러오기 (파일 읽기)
with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())