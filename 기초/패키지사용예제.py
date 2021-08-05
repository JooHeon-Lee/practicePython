# import sample_package.thailand as p
# trip = p.ThailandPackage()
# trip.detail()

# from sample_package.thailand import ThailandPackage
# t = ThailandPackage()
# t.detail()

# from sample_package import vietnam
# t = vietnam.VietnamPackage()
# t.detail()

# __init__에서 방법1 사용시
# from sample_package import *
# v = VietnamPackage()
# t = ThailandPackage()
# v.detail()
# t.detail()

# __init__에서 방법2 사용시
from sample_package import *
v = vietnam.VietnamPackage()
t = thailand.ThailandPackage()
v.detail()
t.detail()

import inspect # 파일 위치 알아내는 모듈
import random
print(inspect.getfile(random)) # 파일위치 알아낼수 있음
print(inspect.getfile(thailand)) # 추후에 파이썬 lib폴더에 넣으면 다른 프로젝트에서도 사용가능