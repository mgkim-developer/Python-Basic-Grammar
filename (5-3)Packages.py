
# 패키지

# 패키지란 무엇인가?
# 패키지(Packages)는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 잇게 해준다.
# 예를 들어 무듈 이름이 A,B인 경우에 A는 패키지 이름이 되고 B는 A 패키지의 B모듈이 된다.

# ※ 파이썬에서 모듈은 하나의 .py 파일이다.

# 파이썬 패키지는 디렉토리와 파이썬 모듈로 이루어지며 구조는 다음과 같다.
# 가상의 game패키지 예

# game/
#     __init__.py
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py

# game, sound, graphic, play는 디렉터리이고 확장자가.py인 파일은 파이썬 모듈이다.
# game 디렉토리가 이 패키지의 루트 디렉토리이고, sound, play는 서브 (디렉토리이다)

# ※  __init__.py 파일은 조금 특이한 용도로 사용하는데 뒤에서 자세하게 다룰 것이다.
# 간단한 파이썬 프로그램이 아니라면 이렇게 패키지 구조로 파이썬 프로그램을 만드는 것이 공동 작업이나 유지 보수 등 여러 면에서 유리하다.
# 또한 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있다.

# 패키지 만들기
# 이제 위 예와 비슷한 game 패키지를 직접 만들어 보며 패키지에 대해서 알아보자.

# 패키지 기본 구성 요소 준비하기
# 1. C:/doit 디렉토리 밑에 game 및 기타 서브 디렉토리를 생성하고 .py 파일들을 다음과 같이 만들어 보자(만약 C:/doit 디렉토리가 없다면 먼저 생성하고 진행하자.)

# C:/doit/game/__init__.py
# C:/doit/game/sound/__init__.py
# C:/doit/game/sound/echo.py
# C:/doit/game/graphic/__init__.py
# C:/doit/game/graphic/render.py

# 2. 각 디렉토리에 __init__.py 파일을 만들어 놓기만 하고 내용은 일단 비워둔다.

# 3. echo.py파일은 다음과 같이 만든다.
# echo.py
def cho_test():
    print("echo")

# 4. render.py 파일은 다음과 같이 만든다.
# redder.py

def render_test():
    print("render")

# 5. 다음 예제를 수행하기 전에 우리가 만든 game 패키지를 참조할 수 있도록 명령 프롬포트 창에서 set 명령어로 PYTHONPATH 환경변수에 C:/doit 디렉토리를 추가한다.
# 그리고 파이썬 인터프리터(Interactive shell)를 실행한다.

# C:\> set PYTHONPATH=C:/doit
# C:\> python
# Type "help", "copyright", "credits" or "license" for more information.
# >>>


# 여기까지 준비가 되었다면 다음을 따라 해 보자.
# 중요 공지
# 아래의 실습은 반드시 명령 프롬포트에서 파이썬 인터프리터를 실행하여 진행해야 한다.

# 패키지 안의 함수 실행하기
