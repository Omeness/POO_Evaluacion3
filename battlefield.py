from datetime import datetime, timedelta
from typing import Optional



class Test:
    def __init__(self, num_id):
        self.num_id = num_id


a = Test(1)
b = Test(2)
c = Test(3)
d = Test(4)

lt = [a,b,c,d]

if a.num_id in [x.num_id for x in lt]:
    print("sis")
else:
    print("non") 

