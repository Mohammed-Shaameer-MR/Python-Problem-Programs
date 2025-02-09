'''
Today coding questions 
1.The pattern has two parts – both mirror reflections of each other. The base of the triangle has to be at the bottom of the imaginary mirror and the tip at the top.

Illustration:

Input:
size = 7

Output:

      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * * 
* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      *
'''



#Code:-

def pattern(n):
    for i in range(n):
        print(('*'*i).rjust(n)+'*'+('*'*i).ljust(n))
    for i in range(n,-1,-1):
        print(('*'*i).rjust(n)+'*'+('*'*i).ljust(n))

pattern(7)
