
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