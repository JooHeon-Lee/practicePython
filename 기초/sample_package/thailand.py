class ThailandPackage:
    def detail(self):
        print("[==========태국======]")

if __name__ == "__main__": # name이 main이면
    print("Thailand 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할 떄만 실행돼요")
    t = ThailandPackage()
    t.detail()
else:
    print("Thailand 외부에서 모듈 호출")