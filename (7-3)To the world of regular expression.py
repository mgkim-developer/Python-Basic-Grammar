
# 정규 표현식의 세계로

# 이제 07-2에서 배우지 않은 몇몇 메타 문자의 의미를 살펴보고 그룹(Group)을 만드는 법, 전방 탐색 등 더욱 강력한 정규 표현식에 대해서 살펴보자.

# 메타문자
# 아직 살펴보지 않은 메타 문자에 대해서 모두 살펴보자.
# 여기에서 다룰 메타 문자는 앞에서 살펴본 메타 문자와 성격이 조금 다르다.
# 앞에서 살펴본 +, *, [], {} 등의 메타문자는 매치가 진행될 때 현재 매치되고 있는 문자열의 위치가 변경된다.(보통 소비된다고 표현한다)
# 하지만 이와 달리 문자열을 소비시키지 않는 메타 문자도 있다.
# 이번에는 이런 문자열 소비가 없는(zerowidth assertions) 메타 문자에 대해 살펴보자.


# |
# | 메타 문자는 or 과 동일한 의미로 사용된다.
# A|B 라는 정규식이 있다면 A 또는 B라는 의미가 된다.
import re

p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)


# ^
# ^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다.
# 앞에서 살펴본 컴파일 옵션 re.MULTILINE을 사용할 경우에는 여러 줄의 문자열일 때 각 줄의 처음과 일치하게 된다.

# 다음 예를 보자.

print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# ^Life 정규식은 Life 문자열이 처음에 온 경우에는 매치하지만 처음 위치가 아닌 경우에는 매치되지 않음을 알 수 있다.


# $
# $ 메타 문자는 ^ 메타 문자와 반대의 경우이다. 즉 $는 문자열의 끝과 매치함을 의미한다.
# 다음 예를 보자.

print(re.search('shrot$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# short$ 정규식은 검색할 문자열이 short로 끝난 경우에는 매치되지만 그 이외의 경우에는 매치되지 않음을 알 수 있다.
# ※ ^ 또는 $ 문자를 메타 문자가 아닌 문자 그 자체로 매치하고 싶은 경운에는 \^, \$로 사용하면 된다.


# \A
# \A 는 문자열의 처음과 매치됨을 의미한다.
# ^ 메타 문자와 동일한 의미이지만 re.MULTILINE 옵션을 사용할 경우에는 다르게 해석된다.
# re.MULTILINE 옵션을 사용할 경우 ^은 각 줄의 문자열의 처음과 매치되지만 \A는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.


# \Z
# \Z 는 문자열의 끝과 매치됨을 의미한다.
# 이것 역시 \A 와 동일하게 re.MULTILINE 옵션을 사용할 경우 $ 메타 문자와는 달리 전체 문자열의 끝과 매치된다.


# \b
# 다음 예를 보자.

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

# \bclass\b 정규식은 앞뒤가 whitespace로 구분된 class라는 단어와 매치됨을 의미한다.
# 따라서 no class at all의 class라는 단어와 매치됨을 확인할 수 있다.

print(p.search('the declassified algorithm'))

# 위 예의 the declassified algorithm 문자열 안에도 class 문자열이 포함되어 있긴 하지만 whitespace로 구분된 단어가 아니므로 매치되지 않는다.

print(p.search('one subclass is'))

# subclass 문자열 역시 class 앞에 sub 문자열이 더해져 있으므로 매치되지 않음을 알 수 있다.

# \b 메타 문자를 사용할 때 주의해야 할 점이 있다.
# \b는 파이썬 리터럴 규칙에 의하면 백스페이스(Backspace)를 의미하므로
# 백스페이스가 아닌 단어 구분자임을 알려주기 위해 r'\bclass\b' 처럼 Raw string 임을 알려주는 기호 r을 반드시 붙여 주어야 한다.\


# \B
# \B 메타 문자는 \b 메타 문자와 반대의 경우이다. 즉 whitespace로 구분된 단어가 아닌 경우에만 매치된다.

p = re.compile (r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

# class 단어의 앞뒤에 whitespace가 하나라도 있는 경우에는 매치가 안 되는 것을 확인할 수 있다.


# 그루핑
