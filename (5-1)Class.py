
# 클래스

# 클래스는 왜 필요한가?
# 프로그래머들이 가장 많이 사용하는 프로그래밍 언어 중 하나인 C 언어에는 클래스가 없다. 이 말은 굳이 크래스가 없어도 프로그램을 충분히 만들 수 있다는 뜻이다.
# 파이썬으로 잘 만든 프로그램을 살펴보아도 클래스를 사용하지 않고 작성한 것들이 상당히 많다.
# 클래스는 지금까지 공부한 함수나 자료형처럼 프로그램 작성을 위해 꼭 필요한 요소는 아니다.

# 하지만 프로그램을 작성할 때 클래스를 적재적소에 사용하면 프로그래머가 얻을 수 있는 이익을 상당하다.
# 예제를 통해 한번 생각해 보자.

# 우리 모두 계산기를 사용해 보았을 것이다.
# 계산기에 숫자 3을 입력하고 +기호를 입력한 후 4릅 입력하면 결과값으로 7을 보여 준다.
# 다시 한 번 +기호를 입력한 후 3을 입력하면 기존 결과값 7에 3을 더해 10을 보여 준다.
# 즉 계산기는 이전에 계산한 결과값을 항상 메모리 어딘가에 저장하고 있어야 한다.

# 이런 내용을 우리가 앞에서 리뷰한 함수를 이용해 구현해 보자. 계산기의 "더하기" 기능을 구현한 파이썬 코드는 다음과 같다.
result = 0

def add(num):
    global result
    result += num
    return result
print(add(3))
print(add(4))
# ※ add함수는 매개변수 num에 받은 값을 이전에 계산한 결과값에 더한 후 돌려주는 함수이다.

# 이전에 계산한 결과값을 유지하기 위해서  result 전역 변수(global)를 사용했다. 프로그램을 실행하면 예상한 대로 다음과 같은 결과값이 출력된다.
# 3
# 7

#그런데 만일 한 프로그램에서 2대의 계산기가 필요한 상황이 발생하면 어떻게 해야 할까?
# 각 계산기는 각각의 결과값을 유지해야 하기 때문에 위와 같이 add함수 하나만으로는 결과값을 따로 유지할 수 없다.

# 이런 상황을 해결하려면 다음과 같이 함수를 각각 따로 만들어야 한다.
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# 똑같은 일을 하는 add1과 add2 함수를 만들었고 각 함수에서 계산한 결과값을 유지하면서 저장하는 전역변수 result1, result2가 필요하게 되었다.
# 결과값은 의도한 대로 출력된다.
# 3
# 7
# 3
# 7
# 3
# 10

# 계산기 1의 결과값이 계산기 2에 아무 영향을 끼치지 않음을 확인할 수 있다. 하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해진다면 어떻게 해야 할까?
# 그때마다 전역 변수와 함수를 추가할 것인가?
# 여기에 빼기나 곱하기 등의 기능을 추가해야 한다면 상황은 점점 더 어려워질 것이다.

# 아직 클래스에 대해 리뷰하지 않았지만, 위와 같은 경우에 클래스를 사용하면 다음과 같이 간단하게 해결할 수 있다.

# ※ 다음 예시 클래스를 아직 이해하지 못해도 된다. 곧 자세하게 리뷰 할 것이다. 여기에서는 클래스 개념만 이해하면 된다.
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
# 프로그램을 실행하면 함수 2개를 사용했을 때와 동일한 결과가 출력된다.
# 3
# 7
# 3
# 7
# 3
# 10

# Calculator 클래스로 만든 별개의 계산기 cal1, cal2(파이썬에서는 이것을 객체라고 부른다)가 각각의 역할을 수행한다.
# 그리고 계산기(cal1, cal2)의 결과값 역시 다른 계산기의 결과값과 상관없이 독립적인 값을 유지한다.
# 클래스를 사용하면 계산기 대수가 늘어나더라도 객체를 생성만 하면 되기 때문에 함수를 사용하는 경우와 달리 매우 간단해진다.
# 만약 빼기 기능을 더하려면 Calculator 클래스에 다음과 같은 빼기 기능 함수를 추가해 주면 된다.
def sub(self, num):
    self.result -= num
    return self.result
# 클래스의 이점은 단순히 이것만이 아니다.
# 하지만 이것 하나만으로도 "도대체 왜 클래스가 필요한 것일까?" 라는 근본적인 물음에 대한 해답이 되었을 것이다.

# 클래스와 객체
# 클래스를 쉽게 설명하면,
# 과자틀 -> 클래스(class)
# 과자 틀에 의해서 만들어진 과자 -> 객체(object)
# 여기에서 설명할 클래스는 과자 틀과 비슷하다. 클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면이고(과자 틀), 객체(object)란 클래스로 만든 피조물(과자 틀을 사용해 만든 과자)를 뜻한다.

# 클래스로 만든 객체에는 중요한 특징이 있다. 바로 객체마다 고유한 성격을 가진다는 것이다.
# 과자 틀로 만든 과자에 구멍을 뚫거나 조금 베어 먹더라도 다른 과자에는 아무 영향이 없는 것과 마찬가지로 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.

# 다음은 파이선 클래스의 가장 간단한 예이다.
class Cookie:
    pass
# 위의 클래스는 아무 기능도 갖고 있지 않은 껍질뿐인 클래스이다.
# 하지만 이렇게 껍질뿐인 클래스도 객체를 생성하는 기능이 있다.
# "과자 틀"로 "과자"를 만드는 것처럼 말이다.

# 객체는 클래스로 만들며 1개의 클래스는 무수히 많은 객체를 만들어 낼 수 있다.
# 위에서 만든 Cookie 클래스의 객체를 만드는 방법은 다음과 같다.
a = Cookie()
b = Cookie()

# Cookie()의 결과값을 돌려받은 a와 b가 바로 객체이다. 마치 함수를 사용해서 그 결과값을 돌려받는 모습과 비슷하다.

# [객체와 인스턴스의 차이]
# 클래스로 만든 객체를 인스턴스라고도 한다. 그렇다면 객체와 인스턴스의 차이는 무엇일까?
# 이렇게 생각해 보자. a = Cookie() 이렇게 만든 a는 객체이다.
# 그리고 a 객체는 Cookie의 인스턴스이다. 즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.
# "a는 인스턴스" 보다는 "a는 객체"라는 표현이 어울리며 "a는 Cookie의 객체"보다는 "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.

# 사칙연산 클래스 만들기

# 클래스를 어떻게 만들지 먼저 구상하기
# 클래스는 무작정 만드는 것보다 클래스로 만든 객체를 중심으로 어떤 식으로 동작하게 할것인지 미리 구상을 한 후에 생각한 것들을 하나씩 해결하면서 완성해 나가는 것이 좋다.

# 사칙연산을 가능하게 하는 FourCal 클래스가 다음처럼 동작한다고 가정해 보자.

# 먼저 a = FourCal()를 입력해서 a라는 객체를 만든다.
# a = FourCal()

# 그런다음 a.setdata(4, 2)처럼 입력해서 숫자 4와 2를 a에 지정해주고
# a.setdata(4, 2)

# a.add() 를 수행하면 두 수를 합한 결과 (4 + 2)를 돌려주고
# print(a.add())

# a.mul()을 수행하면 두 수를 곱한 결과(4 * 2)를 돌려주고
# print(a.mul())

# a.sub()를 수행하면 두 수를 뺀 결과(4 - 2)를 돌려주고
# print(a.sub())

# a.div()를 수행하면 두 수를 나눈 결과 (4 / 2)를 돌려준다.
# print(a.div())
# 이렇게 동작하는 FourCal클래스를 만드는 것이 바로 우리의 목표이다.


# 클래스 구조 만들기
# 자, 그러면 지금부터 앞에서 구상한 것처럼 동작하는 클래스를 만들어 보자.
# 제일 먼저 할 일은 a = FourCal() 처럼 객체를 만들 수 있게 하는 것이다.
# 일단은 아무 기능이 없어도 되기 때문에 매우 간단하게 만들 수 있다.
class FourCal:
    pass
# 현재 상태에서 FrouCal 클래스는 아무 변수나 함수도 포함하지 않지만 우리가 원하는 객체 a를 만들 수 있는 기능은 가지고 있다. 확인해 보자.
# ※ pass는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용한다.

a = FourCal()
print(type(a))
# 위와 같이 a = FourCal()로 a 객체를 먼저 만들고 그 다음에 type(a)로 a 객체가 어떤 타입인지 알아보았다.
# 역시 객체 a가 FourCal 클래스의 객체임을 알 수 있다.
# ※ type 함수는 파이썬이 자체로 가지고 있는 내장 함수로 객체 타입을 출력한다.

# 객체에 숫자 지정할 수 있게 만들기
# 하지만 생성된 객체 a는 아직 아무런 기능도 하지 못한다.
# 이제 더하기, 나누기, 곱하기, 빼기 등의 기능을 하는 객체를 만들어야 한다.
# 그런데 이러한 기능을 갖춘 객체를 만들려면 우선 a객체에 사칙연산을 할 때 사용할 2개의 숫자를 먼저 알려주어야 한다.
# 다음과 같이 연산을 수행할 대상(4, 2)을 객체에 지정할 수 있게 만들어 보자.
# a.setdata(4, 2)

# 위 문장을 수행하려면 다음과 같이 소스 코드를 작성해야 한다.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
# 앞에서 만든 FourCal 클래스에서 pass문장을 삭제하고 그 대신 setdata 함수를 만들었다.
# 클래스 안에 구현된 함수는 다른 말로 메서드(Method)라고 부른다.
# 앞으로 클래스 내부의 함수는 항상 메서드 라고 표현할 것이다. 메서드라는 용어를 기억해 두자.

# 일반적인 함수를 만들 때 다음과 같이 작성한다.

# def 함수명(매개변수):
#     수행할 문장
#     ...

# 메서드도 클래스에 포함되어 있다는 점만 제외하면 일반 함수와 다를 것이 없다.

# setdata 메서드를 다시 보면 다음과 같다
def setdata(self, first, second): #1. 메서드의 매개변수
    self.first = first #2. 메서드의 수행문
    self.second = second #2. 메서드의 수행문

# 1. setdata 메서드의 매개변수
# setdata 메서드는 매개변수로 self, first, second 3개 입력값을 받는다. 그런데 일반 함수와는 달리 메서드의 첫 번째 매개변수 self는 특별한 의미를 가진다.

# 다음과 같이 a 객체를 만들고 a 객체를 통해 setdata 메서드를 호출해 보자.
a = FourCal()
a.setdata(4, 2)
# ※ 객체를 통해 클래스의 메서드를 호출하려면 a.setdata(4, 2)와 같이 도트(.) 연산자를 사용해야 한다.

# 그런데 뭔가 좀 이상하지 않은가? setdata  메서드에는 self, first, second 총 3개의 매개변수가 필요한데 실제로는  setdata(4, 2)처럼 2개 값만 전달했다. 왜그럴까?
# 그 이유는 a.setdata(4, 2)처럼 호출하면 setdata 메서드의 첫 번쨰 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달되기 때문이다.

# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 slef를 사용한다.
# 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용한 것이다. 물론 self말고 다른 이름을 사용해도 상관없다.

# ※ 메서드의 첫 번째 매개변수를 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징이다. 예를 들어 자바 같은 언어는 첫 번째 매개변수 self가 필요없다.

# [메서드의 또 다른 호출 방법]
# 잘 사용하지는 않지만 다음과 같이 클래스를 통해 매서드를 호출하는 것도 가능하다.
a = FourCal()
FourCal.setdata(a, 4, 2)

# 위와 같이 클래스 이름, 메서드 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해 주어야 한다.
# 반면에 다음처럼 객체.메서드 형태로 호출할 때는 self를 반드시 생략해서 호출해야 한다.
a = FourCal()
a.setdata(4, 2)

# 2. setdata 메서드의 수행문
# 이제 setdata 메서드의 수행문에 대해 알아보자
def setdata(self, first, second):  #1. 메서드의 매개변수
    self.first = first  #2. 메서드의 수행문
    self.second = second  #2. 메서드의 수행문

# a.setdata(4, 2)처럼 호출하면 sedata 메서드의 매개변수 first, second에는 각각 값 4와 2가 전달되어 setdata 메서드의 수행문은 다음과 같이 해석된다.
# self.first = 4
# self.second = 2

# self는 전달된 객체 a이므로 다시 다음과 같이 해석된다.
# a.first = 4
# a.second = 2

# a.first = 4 문장이 수행되면 a 객체에 객체변수 first가 생성되고 값 4가 저장된다.
# 마찬가지로 a.second = 2 문장이 수행되면 a 객체에 객체변수 second가 생성되고 값 2가 저장된다.
# ※ 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.

# 다음과 같이 확인해 보자.
a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)
# a 객체에 객체변수 first와 second가 생성되었음을 확인할 수 있다.

# 이번에는 다음과 같이 a, b객체를 만들어 보자.
a = FourCal()
b = FourCal()
# 그리고 a 객체의 객체변수 first를 다음과 같이 생성한다.
a.setdata(4, 2)
print(a.first)
# 이번에는 b객체의 객체변수 first를 다음과 같이 생성한다.
b.setdata(3, 7)
print(b.first)

# 자 이제 아주 중요한 질문을 한 가지 하겠다.
# 위와 같이 진행하면 b객체의 객체변수 first에는 값 3이 저장된다는 것을 확인 할 수 있었다.
# 그렇다면  a객체의 first는 3으로 변할까? 아니면 기존 값 4를 유지할까?
print(a.first)
# a객체의 first값은 b객체의 first값에 영향받지 않고 원래 값을 유지하고 있음을 확인할 수 있다.
# 이 예제를 통해 강조하고싶은 점이 바로 이것이다.
# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.

# id 함수를 사용하면 객체변수가 독립적인 ㄱ밧을 유지한다는 점을 좀 더 명확하게 증명해 보일 수 있다. 다음과 같이 따라해 보자.
# ※ id함수는 객체의 주소를 돌려주는 파이썬 내장 함수이다.
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
print(id(a.first))
print(id(b.first))
# a객체의 first 주소 값과 b객체의 first 주소 값이 서로 다르므로 각각 다른 곳에 그 값이 저장된다는 것을 알 수 있다.
# 객체변수는 그 객체의 고유 값을 저장할 수 있는 공간이다.
# 객체 변수는 다른 객체들에 영향받지 않고 독립적으로 그 값을 유지한다는 점을 꼭 기억하자.
# 클래스에서는 이 부분을 이해하는 것이 가장 중요하다.

# 다음은 현재까지 완성된 FourCal 클래스이다.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

# 지금까지 살펴본 내용이 바로 위 4줄을 설명하기 위함이다.
# 위에서 설명한 것들이 이해가 되지 않는다면 다시 한 번 읽어보기 바란다.

# 더하기 기능 만들기
# 2개의 숫자 값을 설정해 주었으니 2개의 숫자를 더하는 기능을 방금 만든 클래스에 추가해 보자. 다음과 같이 더하기 기능을 갖춘 클래스를 만들어야 한다.
# a = FourCal()
# a.setdata(4, 2)
# print(a.add())
# 이 연산이 가능하도록 다음과 같이 FourCal 클래스를 만들어 보자.

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

# 새롭게 추가된 것은 add 메서드이다. 이제 클래스를 사용해 보자.
a = FourCal()
a.setdata(4, 2)
# 위와 같이 호출하면 앞에서 살펴보았듯이 a객체의 first, second 객체변수에는 각각 값4와 2가 저장될 것이다.
# 이제 메서드를 호출해 보자.
print(a.add())
# a.add()라고 호출하면 add메서드가 호출되어 값 6이 출력될 것이다.
# 어떤 과정을 거쳐 값 6이 출력되는지 add메서드를 따로 떼어 내서 자세히 살펴보자.
def add(self):
    result = self.first + self.second
    return result
# add 메서드의 매개변수는 slelf이고 반환 값은 result이다. 반환 값인 result를 계산하는 부분은 다음과 같다.
# result = self.first + self.second
# a.add()와 같이 a 객체에 의해 add 메서드가 수행되면 add 메서드의 self에는 객체 a가 자동으로 입력되므로 위 내용은 다음과 같이 해석한다.
result = a.first + a.second
# 위 내용은 a.add() 메서드 호출 전에 a.setdata(4, 2)가 먼저 호출되어 a.first = 4, a.second = 2라고 이미 설정되었기 떄문에 다시 다음과 같이 해석한다.
result = 4 + 2
# 따라서 다음과 같이 a.add()를 호출하면 6을 돌려준다.
print(a.add())
# 여기까지 모두 이해한 사람이라면 클래스에 대해 80% 이상을 안 것이다.

# 곱하기, 빼기, 나누기 기능 만들기
# 이번에는 곱하기, 빼기, 나누기 등을 할 수 있게 프로그램을 만들어 보자.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
# mul, sub, div 모두 add 메서드에서 배운 것과 동일한 방법이니 따로 설명하지는 않겠다.
# 정말로 모든 것이 제대로 동작하는지 확인해 보자.
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
print(a.add())
print(a.mul())
print(a.sub())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
# 여기까지 우리가 목표로 한 사칙연산 기능을 가진 클래스를 만들어 보았다.

# 생성자(Constructor)
# 이번에는 우리가 만든 FourCal클래스를 다음과 같이 사용해 보자.
# a = FourCal()
# a.add()
# 위의 코드를 실행하면 오류가 발생한다.
# Traceback (most recent call last):
#   File "C:/git clone file/Python-Basic-Grammar/(5-1)Class.py", line 365, in <module>
#     a.add()
#   File "C:/git clone file/Python-Basic-Grammar/(5-1)Class.py", line 336, in add
#     result = self.first + self.second
# AttributeError: 'FourCal' object has no attribute 'first'
# 오류내용은 위와 같다.
# Four Cal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add메서드를 수항하면,  "AttributeError: 'FourCal' object has no attribute 'first'" 오류가 발생한다.
# setdata 메서드를 수행해야 객체 a의 객체변수 first와 second가 생성되기 때문이다.

# 이렇게 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다.
# 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 매서드를 의미한다.

# 파이썬 메서드 이름으로  __init__를 사용하면 이 메서드는 생성자가 된다. 다음과 같이 FourCal 클래스에 생성자를 추가해 보자.
# ※ __init__ 메서드의 init 앞뒤로 붙은 __는 언더스코어(_) 두 개를 붙여 쓴 것이다.
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# 새롭게 추가된 생성자 __init__ 메서드만 따로 뗴어내서 살펴보자.
# def __init__(self, first, second):
#     self. first = first
#     self.second = second

# __init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다.
# 단 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.

# 이제 다음처럼 예제를 수행해 보자.
# a = FourCal()
# 위의 코드를 실행시키면,
# Traceback (most recent call last):
#   File "C:/git clone file/Python-Basic-Grammar/(5-1)Class.py", line 411, in <module>
#     a = FourCal()
# TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'
# 에러가 발생한다.
# a = FourCal()을 수행할 때 생성자 __init__이 호출되어 위와 같은 오류가 발생했다.
# 오류가 발생한 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문이다.

# 위 오류를 해결하려면 다음처럼 first와 second에 해당되는 값을 전달하여 객체를 생성해야 한다.
a = FourCal(4, 2)
# 위와 같이 수행하면 __init__ 메서드의 매개변수에는 각각 오른쪽과 같은 값이 대입된다.

# 매개변수	값
# self	생성되는 객체
# first	    4
# second	2

# ※ __init__ 메서드도 다른 메서드와 마찬가지로 첫 번쨰 매개변수 self에 생성되는 객체가 자동으로 전달된다는 점을 기억하자
# 따라서  __init__ 메서드가 호출되면 setdata 메서드를 호출했을 때와 마찬가지로 first와 second라는 객체변수가 생성될 것이다.
# 다음과 같이 객체변수의 값을 확인해 보자.
a = FourCal(4, 2)
print(a.first)
print(a.second)
# add 나 div등의 메서드도 잘 동작하는지 확인해 보자.
a = FourCal(4, 2)
print(a.add())
print(a.div())
# 이상 없이 잘 동작하는 것을 확인할 수 있다.

# 클래스의 상속
# 상속(Inheritance)이란 "물려받다"라는 뜻으로, "재산을 상속받다"라고 할 때의 상속과 같은 의미이다.
# 클래스에도 이 개념을 적용할 수 있다. 어떤 클래슬르 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.
# 이번에는 상속 개념을 사용하여 우리가 만든 FourCal 클래스에 a^b(a의 b제곱)을 구할 수 있는 기능을 추가해 보자.

# 앞에서 FourCal클래스는 이미 만들어 놓았으므로 FourCal클래스를 상속하는 MoreFourCal클래스는 다음과 같이 간단하게 만들 수 있다.
class MoreFourCal(FourCal):
    pass
# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
# class 클래스 이름(상속할 클래스 이름)
# MoreFourCal 클래스는 FourCal클래스를 상속했으므로 FourCal클래스의 모든 기능을 사용할 수 있어야 한다.

# 다음과 같이 확인해 보자.
a = MoreFourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
# 상속받은 FourCal클래스의 기능을 모두 사용할 수 있음을 확인할 수 있다.

# 왜 상속을 해야 할까?
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용된다.
# "클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?"라는 의문이 들 수도 있다.
# 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.

# 이제 원래 목적인 a의 b제곱(a^b)을 계산하는 MoreFourCal 클래스를 만들어 보자.
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

# pass문장은 삭제하고 위와 같이 두 수의 거듭제곱을 구할 수 있는 pow 메서드를 추가해 주었다. 그리고 다음과 같이 pow 메서드를 수행해 보자.
a = MoreFourCal(4, 2)
print(a.pow())
# MoreFourCal 클래스로 만든 a 객체에 값 4와 2를 설정한 후 pow 메서드를 호출하면 4의 2제곱 (4^2)인 16을 돌려주는 것을 확인할 수 있다. 

# 상속은 MoreFourCal 클래스처럼 기존 클래스(FourCal)는 그대로 놔둔 채 클래스의 기능을 확장시킬 때 주로 사용한다.

# 메서드 오버라이딩
