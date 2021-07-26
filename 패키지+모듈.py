#패키지 == 모듈의 합 == 라이브러리
#현재 디렉토리에 animal 클래스 생성
# animal -> cat,dog 모듈 생성
# cat과 dog는 hi를 할수있다.
#패키지 == 폴더 (내부에 __init__.py 파일을 생성해야한다.)
# from animal import Dog # animal 패키지에서 dog라는 모듈을 갖고와
# from animal import Cat # animal 패키지에서 cat이라는 모듈을 갖고와
# d = Dog.Dog()
# d.hi()

from animal import * # animal 패키지에 있는 모든 모듈을 갖고옴 * 사용시 바로 object를 생성할수 있다.
d = Dog()
d.hi()