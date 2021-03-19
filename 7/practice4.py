# <pickle>

# pickle이란? 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장하는 것

import pickle

# 파일 생성(데이터 저장)
'''
profile_file = open("profile.pickle", "wb") #b는 binary, 인코딩따로 안해줘도 됨
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()
'''

# 파일 불러오기
profile_file = open("profile.pickle", "rb") #b는 binary, 인코딩따로 안해줘도 됨
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()