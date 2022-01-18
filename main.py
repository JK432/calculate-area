# Write a menu driven program to calculate araea of circle, triangle, rectangle and square. 
print("1.Circle")
print("2.triangle")
print("3.Rectangle")
print("4.Square")
i=int(input())
if(i==1):
  r=int(input())
  area=3.14*r
  print(area)

if(i==2):
  b=int(input())
  h=int(input()) 
  area=0.5*b*h
  print(area)



if(i==3):
  b=int(input())
  h=int(input()) 
  area=b*h
  print(area)

if(i==4):
  b=int(input())
  
  area=b*b
  print(area)