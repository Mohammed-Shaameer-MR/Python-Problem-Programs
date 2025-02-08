'''
CAPTAINS ROOM PROBLEM
Mr. Anant Asankhya is the manager of the INFINITE hotel, which has an unlimited number of rooms. One day, a group of tourists arrives, consisting of a single Captain and several families. Each family has exactly 𝑘 members, where 𝑘 is a given integer greater than 1. The Captain is assigned a separate room, while each family is assigned one room shared among its members. As a result, every room number appears exactly 𝑘 times, except for the Captain’s room, which appears only once.

The manager has a list of room numbers, arranged in no particular order, representing the room assignments of all guests. He needs to determine which room belongs to the Captain. The only information available is the value of 𝑘 and the unordered list of room numbers. The total number of room assignments follows the structure where the family rooms appear in multiples of 𝑘, plus one additional room for the Captain.

Given this information, the task is to identify and print the room number that appears only once in the list. The value of 𝑘 is guaranteed to be at least 2 and less than 1000. The room numbers are all positive integers. The input consists of an integer 𝑘 on the first line, followed by the space-separated list of room numbers on the second line. The output should be a single integer representing the Captain’s room number.
'''

#Code:-
import sys
from collections import Counter
#Getting size of group
k=int(input())

#Getting room no list
rooms=[int(x) for x in sys.stdin.readline().split()]
room_count=Counter(rooms)

#from collections import defaultdict
#room_count=defaultdict(int)
#for i in rooms:
    #room_count[i]+=1

captain_room=next((key for key,item in room_count.items() if item==1),None)    
print(captain_room)
