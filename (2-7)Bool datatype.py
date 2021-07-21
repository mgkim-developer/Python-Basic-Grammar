
# 불 자료형이란?
# 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다. 불 자료형은 다음 2가지 값만을 가질 수 있다.
# True - 참
# False - 거짓

# ※ True나 False는 파이썬의 예약어로 ture, false와 같이 사용하지 말고 첫 문자를 항상 대문자로 사용해야 한다.

# 다음과 같이 변수 a에는 True를, 변수 b에는 False를 지정해 보자.
a = True
b = False
# 따옴표로 감싸지 않은 문자열을 변수에 지정해서 오류가 발생할 것 같지만 잘 실행된다.
# type 함수를 변수 a와 b에 사용하면 두 변수의 자료형이 bool로 지정된 것을 확인 할 수 있다.
print(type(a))
print(type(b))
#  ※type(x)는 자료형을 확인하는 파이썬의 내장 함수이다.

#  불 자료형은 조건문의 반환 값으로도 사용된다. 조건문에 대해서는  if문에서 자세히 배우겠지만 잠시 살펴보고 넘어가자.

print(1 == 1)
# 1 == 1 은 "1과 1이 같은가?"를 묻는 조건문이다. 이런 조건문은 결과로 True 또는 False에 해당하는 불 자료형을 돌려준다. 1과 1은 같으므로 True를 돌려준다.
print(2 > 1)
# 2는 1보다 크기 때문에 2 > 1 조건문은 True를 돌려준다.
print(2 < 1)
# 2는 1보다 작지 않기 때문에 2 < 1 조건문은 False를 돌려준다.

# 자료형의 참과 거짓
# 자료형에 참과 거짓이 있다? 조금 이상하게 들리겠지만 참과 거짓은 분명히 있다. 이는 매우 중요한 특징이며 실제로도 자주 쓰인다.
# 자료형의 참과 거짓을 구분하는 기분은 다음과 같다.
# 값	참 or 거짓
# "python"	참
# ""	거짓
# [1, 2, 3]	참
# []	거짓
# ()	거짓
# {}	거짓
# 1	참
# 0	거짓
# None	거짓

# 문자열, 리스트 튜플, 딕셔너리 등의 값이 비어있으면 (" ", [ ], ( ), { })거짓이 된다.
# 당연히 비어있지 않으면 참이 된다. 숫자에서는 그 값이 0일 떄 거짓이 된다. 위표를 보고면 None이 있는데, 이것에 대해서는 뒷부분에서 배우니 아직은 신경 쓰지 말자. 그저 None은 거짓을 뜻한다는 것만 알아두자.

# 다음 예를 보고 참과 거짓이 프로그램에서 어떻게 쓰이는지 간단히 알아보자.
a = [1, 2, 3, 4]
while a:
    print(a.pop())
# 먼저 a = [1, 2, 3, 4] 리스트를 하나 만들었다.

# while문은 03장에서 자세히 다루겠지만 간단히 알아보면 다음과 같다. 조건문이 참인 동안 조건문 안에 있는 문장을 반복해서 수행한다.

# while 조건문:
#     수행할 문장

# 즉 위 예를 보면 a가 참인 경우에 a.pop( )을 계속 실행하라는 의미이다. a.pop()함수는 리스트 a의 마지막 요소를 끄집어내는 함수이므로 리스트 안에 요소가 존재하는 한 (a가 참인 동안) 마지막 요소를 계속해서 끄집어 낼 것이다.
# 결국 더 이상 끄집어낼 것이 없으면 a가 빈르스트 ([ ])가 되어 거짓이 된다.
# 따라서 while문에서 조건이 거짓이 되므로 중지된다.
# 위에서 본 예는 파이썬 프로그래밍에서 매우 자주 사용하는 기법 중 하나이다.

# 위 예가 너무 복잡하다고 생각하는 독자는 다음 예를 보면 쉽게 이해될 것이다.

if [ ]:
    print("참")
else:
    print("거짓")
# if문에 대해서 잘 모르는 독자라도 위의 문장을 해석하는 데는 무리가 없을 것이다.
# ※ if 문에 대해서는 03장에서 자세히 다룬다.
# []는 앞의 표에서 볼 수 있듯이 비어 있는 리스트이므로 거짓이다. 따라서 "거짓"이란 문자열이 출력된다.

if [1, 2, 3]:
    print("참")
else:
    print("거짓")
# 위 코드를 해석해 보면 다음과 같다.
# 만약 [1, 2, 3]이 참이면 "참"이라는 문자열을 출력하고 그렇지 않으면 "거짓"이라는 문자열을 출력하라.
# 위 코드의 [1, 2, 3]은 요솟값이 있는 리스트이기 때문에 참이다. 따라서 "참"을 출력한다.

# 불 연산
# 자료형에 참과 거짓이 있음을 이미 알아보았다. bool 내장 함수를 사용하면 자료형의 참과 거짓을 식별할 수 있다.
# 다음 예제를 따라 해 보자.
print(bool('python'))
# 'python'문자열은 빈 문자열이 아니므로 bool 연산의 결과로 불 자료형인 True를 돌려준다.
print(bool(" "))
# " " 문자열은 빈 문자열이므로 bool 연산의 결과로 불 자료형인 False를 돌려준다.
# 위에서 알아본 몇 가지 예제를 더 수행해 보자.
print(bool([1, 2, 3]))
print(bool([ ]))
print(bool(0))
print(bool(3))
# 위에서 알아본 것과 동일한 참과 거짓에 대한 결과를 돌려주는 것을 확인할 수 있다.

# 지금까지 파이썬의 가장 기본이 되는 자료형인 숫자, 문자열, 리스트, 튜플, 딕셔너리, 집합, 불에 대해서 알아보았다.
# Review complete


