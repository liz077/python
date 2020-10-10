# Chapter02-1
# 파이썬 완전 기초
# print 사용법


#기본출력
print('phython start!')
print("python strat!")
print('''python start!''')
print("""python start!""")

print() #줄바꿈

#separater 옵션
print('P','Y','T','H','O','N',sep=',')
print('P','Y','T','H','O','N',sep='|')
print('P','Y','T','H','O','N',sep='    ')
print('python','google.com',sep='@')


#end 옵션

print('welcome to',end=' ')
print('IT News',end='')
print('Web Site')
print()

#file 옵션(별도의 파일에 쓰기)
import sys

print('Learn Python', file=sys.stdout)
print()

#format 사용(d : 3,s:'python',f: 3.14444)
print('%s %s' % ('one','two')) # s가 2개라서 2개를 대체 가능
print('{} {}'. format('one','two')) #가독성이 좀더 좋음
print('{1} {0}'.format('one','two')) #인덱스는 0부터 시작되므로
print()

# %s
print('%10s' % ('nice')) #총 10자리 수에서 왼쪽부터 공백으로 남기고 nice
print('{:>10}'.format('nice')) #위와 동일한 결과

print('%-10s' % ('nice')) #음수가 왔으므로 오른쪽부터 공백 채우기
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) #공백을 입력한 기호로 채움
print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))#원하는 자리수 만큼 왼쪽부터
print('{:10.5}'.format('pythonstudy'))#공간은 10자리에 글자는 5개만 표시

print()
# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()
# %f

print('%1.8f' % (3.1443434343434))#정수부와 소수부 자리수를 지정할 수 있음
print('{:f}' . format(3.1434343434))

print('%06.2f' % (3.141592999999))#총 6개 중에서 정수부는 1자리라 0으로 채우고 나머지는 2가리 표시
print('{:06.2f}'.format(3.141592999999))
