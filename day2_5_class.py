class Rectangle:
    count = 0 # 클래스 변수
    # init
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    # 인스턴스 메서드
    def calcArea(self):
        area = self.width * self.height
        return area
    # 정적 메서드 
    @staticmethod
    def isSquare(width, height):
        print('정적 메서드')
        return width == height
    # 클래스 메서드
    @classmethod
    def printCnt(cls):
        print(cls.count)
        cls.count += 1
        return cls.count
# 자체 실행시
if __name__ == '__main__':
    print('main')
    # 인스턴스 화
    myRec = Rectangle(20, 20)
    # 인스턴스 메서드는 인스턴스가 있어야 실행가능
    print(myRec.calcArea())
    # 정적 메서드는 self, cls 없음 그냥 메서드 기능
    print(Rectangle.isSquare(20, 20))
    print(Rectangle.printCnt())
# 다른곳에서 import 했을때
else:
    print('another module')