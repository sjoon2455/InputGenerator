# -*- coding: utf-8 -*-
#Target source code target.py

class Triangle:
    TriangleType= {
        NOT_A_TRIANGLE,
        SCALENE, # 부등변 삼각형
        EQUILATERAL, #정삼각형
        ISOSCELES #이등변
    }


def classify(a, b, c):
    type = TriangleType
    temp = 0

    if a > b:
      temp = a
      a = b
      b = temp
    
    if a > c:
      temp = a
      a = c
      c = temp
    
    if b > c:
      temp = b
      b = c
      c = temp
    
    if a + b <= c:
      type = TriangleType.NOT_A_TRIANGLE
    else: 
        type = TriangleType.SCALENE
        if a == b: 
            if b == c: 
                type = TriangleType.EQUILATERAL
        else:
            if a == b:
                type = TriangleType.ISOSCELES
            else if b == c:
                type = TriangleType.ISOSCELES
    return type
  





'''
def funca, b:
    if a >= 3:
        a += 3
        if a <= 7:
            b -= 3
            if b != 0:
                return True
    return False
'''