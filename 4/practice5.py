# <자료구조의 변경>

# ex) 커피숍 메뉴의 구조를 바꿔보자
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))