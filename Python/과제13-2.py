def security(password):
    if(len(password)>=9):
        print("Your Password: Good")
    elif(len(password)>=5):
        print("Your Password: Normal")
    else:
        print("Your Password: Bad")


pw = input("비밀번호를 입력하시오: ")
security(pw)
