# 한국어

## 초성, 중성, 종성 분리하기
```
x = '안녕하세요'.encode('utf-8')
x
```
b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'

**초성**   
```
x[::3]
```
b'\x88\x95\x98\xb8\x94'

**중성**   
```
x[1::3]
```
b'\x95\x85\x95\x84\x9a'

**종성**   
```
x[2::3]
```
b'\x88\x95\x98\xb8\x94'