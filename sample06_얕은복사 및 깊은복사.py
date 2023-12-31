import numpy as np
print(np.__version__)

'''
    얕은 복사 (주소값 복사) vs 깊은 복사(실제값 복사)
    
    1. 기본 python
     예> x = [1,2,3]
        x2 = x >> 얕은 복사, 따라서 x2에서 값을 변경하면 x도 변경이 됨.
     *python의 깊은복사 3가지 방법
      - x3에서 값을 변경해도 원본 x는 영향을 받지 않는다.
     x3 = x[:]
     x3 = x.copy()
     x3 = list(x)
    
    
    2. numpy
     - [:] 슬라이싱 처리는 얕은 복사로 처리함. 
        그런데 주소값은 다르다. -> 뷰 형태로 연결되어 있음.
                            -> 원본도 변경됨.
     * numpy의 깊은복사 방법
       - np.copy(값) 또는 값.copy()
   
'''

#1. 기본 python
x = [1, 2, 3]
x2 = x
print(id(x), id(x2))  #2396591192960 2396591192960
x2[0] = 100
print(x, x2) #[100, 2, 3] [100, 2, 3]

# 깊은복사
#x3 = x[:]
#x3 = x.copy()
x3 = list(x)
print(id(x), id(x3)) # 2703515479424 2703515479552
x3[1] = 100 #x3에서 값을 변경해도 x는 영향이 없음
print(x, x3) # [100, 2, 3] [100, 100, 3]

######################################################

#1. 기본 numpy
arr = np.array([1, 2, 3])
print(arr)

arr2 = arr[:] # numpy는 얕은 복사
print(id(arr), id(arr2)) #2900002006768 2900002006864 > 주소값은 다름 (뷰연결)
arr2[0] = 100  # 값 변경 시 원본도 변경 됨
print(arr, arr2) # [100   2   3] [100   2   3]

# 깊은 복사
arr3 = np.copy(arr)
print(id(arr), id(arr3)) # 2199835043568 2200378385392
arr3[1] = 200       # 주소값 변경 시 원본은 변경되지 않음
print(arr, arr3) # [100   2   3] [100 200   3]
