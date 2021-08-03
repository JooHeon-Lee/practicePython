try:
    print("나누기 전용 계산기입니다.")
    nums = []
    num1,num2 = map(int,input("두개의 숫자를 입력하세요").split())
    nums.append(num1)
    nums.append(num2)
    #nums.append(int(nums[0] / nums[1])) # 만약 이부분을 안쓰면 indexError

    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러발생 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # err을 활용해서 에러문장 자체를 출력할수있음
    print(err)
except Exception as err: # value, zero디비전 오류가 아닌 오류( 정확한 에러인지는 Exception as err 사용)
    print("알 수 없는 오류 발생")
    print(err)
