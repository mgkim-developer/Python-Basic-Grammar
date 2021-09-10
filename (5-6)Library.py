
# 05-6 라이브러리
# 이제 파이썬 프로그래밍 능력을 높여 줄 더 큰 날개를 달아 보자.
# 전 세계의 파이썬 사용자들이 만든 유용한 프로그램을 모아 놓은 것이 바로 파이썬 라이브러리이다.
# "라이브러리"는 "도서관"이라는 뜻 그대로 원하는 정보를 찾아보는 곳이다.
# 모든 라이브러리를 다 알 필요는 없다. 자신이 하는 일에 필요할 때마다 선택해서 사용하면 된다.
# 그러기 위해서는 어떤 라이브러리가 존재하고 어떻게 사용하는지 정도는 알아야 한다.
# 자주 사용되고, 알아두면 좋은 라이브러리를 중심으로 하나씩 살펴보도록 하자.

# sys
# sys 모듈은 파이썬 인터프리터가 제공하는변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
# 명령 행에서 인수 전달하기 - sys.argv

# C:/User/home>python test.py abc pey guido

# 명령 프롬프트 창에서 위 예처럼 test.py 뒤에 또 다른 값을 함꼐 넣어 주면 sys.argv 리스트에 그 값이 추가된다.

# 예제를 따라 하며 확인해 보자. 우선 다음과 같은 파이썬 프로그램을 작성하자. argv_test.py 파일은 C:/doit/Mymod 디렉토리에 저장했다고 가정한다.
# (만약 C:/doit/Mymod 디렉토리가 없다면 먼저 생성하고 진행하자.)

# argv_test.py
# import sys
# print(sys.argv)

# 명령 프롬포트 창에서 Mymod 디렉토리로 들어간 뒤 다음과 같이 실행해 보자.

# C:/doit/Mymod>python argv_test.py you need python
# ['argv_test.py', 'you', 'need', 'python']

# python 명령어 뒤의 모든 것들이 공백을 기준으로 나뉘어서 sys.argv 리스트의 요소가 된다.

# 강제로 스크립트 종료하기 - sys.path

# sys.path는 파이썬 모듈둘이 저장되어 있는 위치를 나타낸다.
# 즉 이 이ㅜ치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다.

# 다음은 그 실행 결과이다.

# >>> import sys
# >>> sys.path
# ['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs',
# 'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages']
# >>>

# 위 예에서 "는 현재 디렉토리를 말한다.

# path_append.py
# import sys
# sys.path.append("C:/doit/mymod")

# 위와 같이 파이썬 프로그램 파일에서 sys.path.append를 사용해 경로 이름을 추가할 수 있다.
# 이렇게 하고 난 후에는 C:/doit/Mymod 디렉토리에 있는 파이썬 모듈을 불러와서 사용할 수 있다.

# ※ 파일 경로를 표시할 떄 명령 프롬프트 창에서는 /, \든 상관없지만, 소스코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다.


# pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여 준다.
# >>> import pickle
# >>> f = open("test.txt", 'wb')
# >>> data = {1: 'python', 2: 'you need'}
# >>> pickle.dump(data, f)
# >>> f.close()

# 다음은 pickle.dump로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예이다.
# >>> import pickle
# >>> f = open("test.txt", 'rb')
# >>> data = pickle.load(f)
# >>> print(data)
# {2:'you need', 1:'python'}

# 위 예에서는 딕셔너리 객체를 사용했지만 어떤 자료형이든 저장하고 불러올 수 있다.

# os
# os 모듈은 환경 변수나 디렉토리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.

# 내 시스템의 환경 변수값을 알고 싶을 때 - os.environ

# 시스템은 제각기 다른 환경 변수 값을 가지고 있는데, os.environ은 현재 시스템의 환경 변수 값을 보여 준다.
# 다음을 따라 해 보자.

# >>> import os
# >>> os.environ
# environ({'PROGRAMFILES': 'C:\\Program Files', 'APPDATA': … 생략 …})
# >>>

# 위 결과값은 필자의 시스템 정보이다. os.environ은 환경 변수에 대한 정보를 딕셔너리 객체로 돌려준다. 자세히 보면 여러 가지 유용한 정보를 찾을 수 있다.
# 돌려받은 객체가 딕셔너리이기 때문에 다음과 같이 호출할 수 있다. 다음은 어떤 시스템의 PATH 환경 변수 내용이다.

# >>> os.environ['PATH']
# 'C:\\ProgramData\\Oracle\\Java\\javapath;...생략...'

# 디렉토리 위치 돌려받기 -os.getcwd
# os.getcwd는 현재 자신의 디렉토리 위치를 돌려준다.

# >>> os.getcwd()
# 'C:\WINDOWS'

# 시스템 명령어 호출하기 - os.system

# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다.
# os.system("명령어")처럼 사용한다.
# 다음은 현재 디렉토리에서 시스템 명령어 dir을 실행하는 예이다.

# >>> os.system("dir")

# 실행한 시스템 명령어의 결과값 돌려받기 - os.popen
# os.popen은 시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 돌려준다.

# >>> f = os.popen("dir")

# 읽어 들인 파일 객체의 내용을 보기 위해서는 다음과 같이 하면 된다.
# print(f.read())

# 기타 유용한 os rhksfus gkatn

# 함수	설명
# os.mkdir(디렉터리)	디렉터리를 생성한다.
# os.rmdir(디렉터리)	디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
# os.unlink(파일)	파일을 지운다.
# os.rename(src, dst)	src라는 이름의 파일을 dst라는 이름으로 바꾼다.\


# shutil
# shutil은 파일을 복사해 주는 파이썬 모듈이다.

# 다음 예시는 src라는 이름의 파일을 dst로 복사한다.
# 만약 dst가 디렉토리 이름이라면 src라는 파일 이름으로 dst디렉토리에 복사하고 동일한 파일 이름이 있을 경우에는 덮어쓴다.

# import shutil
# shutil.copy("src.txt", "dst.txt")

# 위 예를 실행해 보면 src.txt 파일과 동일한 내용의 파일이 dst.txt로 복사되는 것을 확인할 수 있다.


# glob
# 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉토리에 있는 파일 이름 모두를 알아야 할 때가 있다.
# 이럴 때 사용하는 모듈이 바로 glob이다.

# 디렉토리에 있는 파일들을 리스트로 만들기 - glob(pathname)

# glob 모듈은 디렉터리 안의 파일들을 읽어서 돌려준다.
# *, ? 등 메타 문자를 써서 우너하는 파일만 읽어 들일 수도 있다.

# 다음은 C:/doit 디렉토리에 있는 파일 중 이름이 mark로 시작하는 파일을 모두 찾아서 읽어 들이는 예이다.

# >>> import glob
# >>> glob.glob("c:/doit/mark*")
# ['c:/doit\\marks1.py', 'c:/doit\\marks2.py', 'c:/doit\\marks3.py']
# >>>


# time
# 시간과 관련된 time 모듈에는 함수가 굉장히 많다. 그중 가장 유용한 몇 가지만 알아보자.

# time.time
# time.time()은 UTC(Universal Time Coordinated 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 돌려주는 함수이다.
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.
import time
time.time()
print(time.time())

# time.localtime
# time.localtime은 time.time() 이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초,..의 형태로 바꾸어 주는 함수이다.
print(time.localtime(time.time()))

# time.asctime
# 위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
print(time.asctime(time.localtime(time.time())))

# time.ctime
# time.asctime(time.localtime(time.time()))은 time.ctime()을 사용해 간편하게 표시할 수 있다.
# asctime과 다른 점은 ctime은 항상 현재 시간만을 돌려준다는 점이다.
print(time.ctime())

# time.strftime
print(time.strftime('출력할 형식 포맷 코드', time.localtime(time.time())))

# strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.

# 시간에 관계된 것을 표현하는 포맷 코드

# 시간에 관계된 것을 표현하는 포맷 코드
#
# 포맷코드	설명	예
# %a	요일 줄임말	Mon
# %A	요일	Monday
# %b	달 줄임말	Jan
# %B	달	January
# %c	날짜와 시간을 출력함	06/01/01 17:22:21
# %d	날(day)	[01,31]
# %H	시간(hour)-24시간 출력 형태	[00,23]
# %I	시간(hour)-12시간 출력 형태	[01,12]
# %j	1년 중 누적 날짜	[001,366]
# %m	달	[01,12]
# %M	분	[01,59]
# %p	AM or PM	AM
# %S	초	[00,59]
# %U	1년 중 누적 주-일요일을 시작으로	[00,53]
# %w	숫자로 된 요일	[0(일요일),6]
# %W	1년 중 누적 주-월요일을 시작으로	[00,53]
# %x	현재 설정된 로케일에 기반한 날짜 출력	06/01/01
# %X	현재 설정된 로케일에 기반한 시간 출력	17:22:21
# %Y	년도 출력	2001
# %Z	시간대 출력	대한민국 표준시
# %%	문자	%
# %y	세기부분을 제외한 년도 출력	01

# 다음은 time.strftime을 사용하는 예이다.
import time
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

# time.sleep
# time.sleep 함수는 주로 루프 안에서 많이 사용한다. 이 함수를 사용하면 일정한 시간 간격을 두고 로프를 실행할 수 있다.
# 다음 예를 보자.

import time
for i in range(10):
    print(i)
    time.sleep(1)

# 위 예는 1초 간격으로 0부터 9까지의 숫자를 출력한다.
# 위 예에서 볼 수 있듯이 time.sleep 함수의 인수는 실수 형태를 쓸 수 있다.
# 즉 1이면 1초, 0.5면 0.5초가 되는 것이다.

# calendar
# calendar는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.
# calendar.calendar(연도)로 사용하면 그해의 전체 달력을 볼 수 있다.
# 결과값은 달력이 너무 길어 생략하겠다.
import calendar
print(calendar.calendar(2015))

# calendar.prcal(연도)를 사용해도 위와 똑같은 결과값을 얻을 수 있다.
calendar.prcal(2015)

# 다음 예는 2015년 12월의 달력만 보여 준다.
print(calendar.prmonth(2015, 12))

# calendar.weekday
# calendar 모듈의 또 다른 유용한 함수를 보자.
# weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다.
# 월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4, 토요일은 5, 일요일은 6이라는 값을 돌려준다.
print(calendar.weekday(2015, 12, 31))
# 위의 예에서 2015년 12월 31일은 목요일임을 보여준다.

# calendar.monthrange
# monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.
print(calendar.monthrange(2015, 12))
# 위 예는 2015년 12월 1일은 화요일이고, 이 달은 31일까지 있다는 것을 보여 준다.
# 날짜와 관련된 프로그래밍을 할 떄 위 2가지 함수는 매우 유용하게 사용된다.


# random
# random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다. random과 randint에 대해 알아보자.
# 다음은 0.0에서 1.0 사이의 실수 중에서 난수 값을 돌려주는 예를 보여 준다.
import random
print(random.random())

# 다음 예는 1에서 10사이의 정수 중에서 난수 값을 돌려준다.
print(random.randint(1, 10))

# 다음 예는 1에서 55사이의 정수 중에서 난수 값을 돌려준다.
print(random.randint(1, 55))

# random 모듈을 사용해서 재미있는 함수를 하나 만들어 보자.
# random_pop.py
import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ =="__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))
# 위 random_pop 함수는 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 돌려준다.
# 물론 꺼낸 요소는 pop 메서드에 의해 사라진다.

# random_pop 함수는 random 모듈의 choice 함수를 사용하여 다음과 같이 좀 더 직관적으로 만들 수도 있다.
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number
# random.choice 함수는 입력을 받은 리스트에서 무작위로 하나를 선택하여 돌려준다.

# 리스트 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 사용하면 된다.
import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)
# [1, 2, 3, 4, 5] 리스트가 shuffle 함수에 의해 섞여서 print된 것을 볼 수 있다.


# webbrowser