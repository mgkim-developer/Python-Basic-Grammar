
# 5-4 예외 처리

# 프로그램을 만들다 보면 수없이 많은 오류를 만나게 된다.
# 물론 오류가 발생하는 이유는 프로그램이 잘못 동작하는 것을 막기 위한 파이썬의 배려이다.
# 하지만 때때로 이러한 오류를 무시하고 싶을 때도 있다.
# 이를 위해 파이썬은 try, except를 사용해서 예외적으로 오류를 처리할 수 있게 해준다.

# 오류는 어떤 때 발생하는가?

# 오류를 처리하는 방법을 알기 전에 어떤 상황에서 오류가 발생하는지 한번 알아보자.
# 오타를 입력했을 때 발생하는 구문 오류 같은 것이 아닌 실제 프로그램에서 자주 발생하는 오류를 중심으로 살펴본다.

# 먼저 디렉토리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류이다.

# >>> f = open("나없는파일", 'r')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'

# 위 예에서 볼 수 있듯이 없는 파일을 열려고 시도하면 FileNotFoundError 오류가 발생한다.

# 이번에는 0으로 다른 숫자를 나누는 경우를 생각해 보자. 이 역시 자주 발생하는 오류이다.

# >>> 4 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

# 4를 0으로 나누려니까 ZeroDivisionError 오류가 발생한다.

# 마지막으로 한 가지 예를 더 들어보자. 다음 오류는 정말 빈번하게 일어난다.

# >>> a = [1,2,3]
# >>> a[4]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

# a는 리스트 [1, 2, 3]인데, a[4]는 a 리스트에서 얻을 수 없는 값이다. 따라서 IndexError 오류가 발생한다.
# 파이썬은 이런 오류가 발생하면 프로그램을 중단하고 오류 메시지를 보여준다.


# 오류 예외 처리 기법

# try, except문
# 다음은 오류 처리를 위한 try, except문의 기본 구조이다.


# try:
#
#     ...
# except [발생 오류[as 오류 메시지 변수]]:
#     ...

# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.
# 하지만 try 블록에서 오류가 발생하지 않는다면 ecept 블록은 수행되지 않는다.

# except 구문을 자세히 살펴보자

# except [발생 오류 [as 오류 메시지 변수]]:

# 위 구문을 보면 [ ] 기호를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있따는 관례 표기법이다.
# 즉 except 구문은 다음 3가지 방법으로 사용할 수 있다.

# 1. try, except만 쓰는 방법

try:
    ...
except:
    ...

# 이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.

# 2. 발생 오류만 포함한 except문

# try:
#     ...
# except 발생 오류:
#     ...

# 이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except블록을 수행한다는 뜻이다.

# 3. 발생 오류와 오류 메시지 변수까지 포함한 except문

# try:
#     ...
# except 발생 오류 as 오류 메시지 변수:
#     ...

# 이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.
# 이 방법의 예를 들어 보면 다음과 같다.

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# 위처럼 4를 0으로 나누려고 하면 ZeroDivisionError가 발생하여 except 블록이 실행되고 변수 e에 담기는 오류 메시지를 다음과 같이 출력한다.

# 결과값: division by zero


# try .. finally