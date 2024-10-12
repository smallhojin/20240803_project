# 사용자에게 수학 점수를 입력받아 상,중,하 반으로 나누기
# 상 - 90점 이상

size = int(input("수학 시험 점수를 입력해 주세요"))
print(size)

if 0 <= size <= 100 :
    if size >= 90:
        print("당신은 상반으로 가십시오")
    elif size >= 70:
        print("중반으로 가십시오")
    elif size >= 70:
        print("중반으로 가십시오")
else:
    print("점수를 올바르게 입력해 주세요")





