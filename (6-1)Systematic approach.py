
# 06-1 내가 프로그램을 만들 수 있을까?

# 프로그램을 막 시작하려고 하는 사람이 제일 처음 부딪히게 되는 벽은 아마 다음과 같지 않을까?

# "문법도 이제 조금 알겠고, 대부분 이해했다. 이러한 지식을 이용해서 내가 도대체 어떤 프로그램을 만들 수 있을까?"

# 이럴 떄는 "어떤 프로그램을 짜야겠어!"라는 생각보다는 다른사람들이 만든 프로그램 파일을 자세히 들여다보고 분석하는 데서 시작하는 것이 좋다.
# 그러다 보면 다른 사람들의 생각도 읽을 수 있고, 거기에 더해 뭔가 새로운 아이디어가 떠오를 수도 있다.
# 하지만 이때 가장 중요한 것은 자신의 수준에 맞는 소스를 찾는 일이다.
# 그래서 6장에서는 아주 쉬운 예제부터 시작해서 차츰 수준을 높여 실용적인 예제까지 다루려고 노력할 것이다.
# 물론 배운 내용을 어떻게 활용하는지는 리뷰를 보는 여러분에게 달려있다.

# 나는 예전에 프로그래밍을 막 시작한 친구에게 구구단 프로그램을 짜 보라고 한 적이 있다.
# 쉬운 과제이고 파이썬 문법도 다 공부한 사람이었는데 프로그램을 어떻게 만들어야 할지 전혀 갈피를 잡지 못했다.
# 그래서 나는 다음과 같은 해결책을 알려 주었다.

# 프로그램을 만들려면 가장 먼저 "입력"과 "출력"을 생각하라.

# 가령 구구단 프로그램 중 2단을 만든다면 2를 입력값으로 주었을 때 어떻게 출력되어야 할지 생각해 보라고 했다.
# 그래도 그림이 그려지지 않는 것 같아 직접 연습장에 적어 가며 설명해 주었다.

# ● 함수 이름은? GuGuDan로 짓자
# ● 입락받는 값은? 2
# ● 출력하는 값은? 2단(2, 4, 6, 8, ..., 18)
# ● 결과는 어떤 형태로 저장하지? 연속된 자료형이니까 리스트!

# 다같이 따라해보길 바란다.

# 1. 먼저 에디터를 열고 다음과 같이 입력한다. GuGuDan이라는 함수에 2를 입력값으로 주면 result라는 변수에 결과값을 넣으라는 뜻이다.
# result = GuGuDan(2)

# 2. 이제 결과값을 어떤 형태로 받을 것인지 고민해 보자. 2단이니까 2, 4, 6,...18까지 갈 것이다.
# 이런 종류의 데이터는 리스트 자료형이 딱이다.
# 따라서 result = [2, 4, 6, 8, 10, 12, 14, 16, 18] 같은 결과를 얻는 것이 좋겠다는 생각을 먼저 하고 나서 프로그래밍을 시작하는 것이 필요하다.
# 이런 식으로 머릿속에 그림이 그려지기 시작하면 의외로 생각이 가볍게 좁혀지는 것을 느낄 수 있을 것이다.

# 3. 어떻게 만들지 생각해 봤으니 1번에서 입력한 문장은 주석처리 하고, 진짜 프로그램을 짜 보자.
# 일단 이름을 GuGuDan으로 지은 함수를 다음과 같이 만든다.
def GuGuDan(n):
    print(n)

GuGuDan(2)
# 위와 같은 함수를 만들고 GuGuDan(2)처럼 실행하면 2를 출력하게 된다.
# 즉 입력값으로 2가 잘 들어오는지 확인하는 것이다.

# 4. 이제 결과값을 담을 리스트를 하나 생성하자. 앞에서 작성한 print(n)은 입력이 잘 되는지 확인하기 위한 것이었으므로 지워도 좋다.
def GuGu(n):
    print(n)
# 5. 다음으로
