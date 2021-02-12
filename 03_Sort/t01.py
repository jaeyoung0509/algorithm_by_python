lists = []
lists.append(("홍길동" , 95))
lists.append(("이순신" , 77))
lists.sort(key = lambda  stu : stu[1] ,reverse=True)
print(lists)