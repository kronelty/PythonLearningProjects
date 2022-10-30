import random
import traceback


randomNumber = random.randint(1, 100)

# print(randomNumber)

# print(random.random())

# print(random.uniform(1, 100))

# print(random.randint(1, 100)) # randrange(1, 101)

# print(random.randrange(1, 100))

# print(random.randrange(100))

# try:
#     print(random.choice({"f902j0": 1, "243rx908umj2": 8349284, "9xnh923xr": 4598762384792349874}))
# except:
#     print(traceback.format_exc())

# try:
#     print(random.choice(set([1, 465, 342, 54, 6, 76, 4567, 5432, 923498457])))
# except:
#     print(traceback.format_exc())


# print("end")

gameCount = 1

while True:
    
    while True:
        try:
            inputNum = int(input("1 ~ 100 사이의 숫자를 입력하세요: "))
            if inputNum >=1 and inputNum <=100:
                break
            else:
                print("잘못된 값입니다.")
        except:
            print("잘못된 값입니다.")
    
    if inputNum > randomNumber:
        print("다운")
    elif inputNum < randomNumber:
        print("업")
    elif inputNum == randomNumber:
        print("축하합니다.", gameCount, "번 만에 맞췄습니다!")
        break
    
    gameCount += 1