class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 일] 방콕, 파타야 패키지 여행 ")

if __name__=="__main__":
    print("Thailand 묘듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to=ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")