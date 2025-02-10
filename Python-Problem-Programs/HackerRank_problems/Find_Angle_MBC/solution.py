import math

ab = int(input())
bc = int(input())

ac = (ab**2 + bc**2) ** 0.5  

mbc = math.acos(bc / ac)  

print(f"{round(math.degrees(mbc))}{chr(176)}")  
#176 is degree symbol