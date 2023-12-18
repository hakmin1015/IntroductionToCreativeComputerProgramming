age = int(input("나이를 입력하세요: "))

if(age<4):
    print("면제")
elif(age<8):
    print("1000원")
elif(age<19):
    print("2000원")
elif(age<60):
    print("5000원")
else:
    print("면제")
