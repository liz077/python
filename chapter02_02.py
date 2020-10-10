# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

#기본 선언
n = 700

#출력
print(n)
print(type(n))

print()
#동시선연
x = y = z = 700
print(x,y,z)
print()

#선언
var = 75

#재선언
var = "Change Value"

#출력
print(var)
print(type(var))

print()

#object references
#변수값 할당 상태
#1. 타입에 맞는 오브젝트 생성
#2. 값 생성
#3. 콘솔 출력

# 예1)
print(300)
print(int(300))

print()

#예2)
#n -> 777
n = 777

print(n,type(n))
print()

m = n
#m -> 777 <-# n

print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

#id(identity) 확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

#다양한 변수 선언
#camel case : numberOfCollegeGraduates
#pascal case : NumberOfCollegeGraduates
#snake case : number_of_college_graduates

# 허용하는 변수 선언법
age = 1
Age = 2
aGe = 3
a_g_e = 4
_age = 5
age_= 6
_AGE_ = 7

# 7age = 1 #숫자가 앞에 오면 에러 발생

#예약어는 변수명으로 불가능
# for =  3
# as = 3
# class =3
