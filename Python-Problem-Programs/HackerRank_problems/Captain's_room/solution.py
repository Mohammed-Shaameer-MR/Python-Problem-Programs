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
