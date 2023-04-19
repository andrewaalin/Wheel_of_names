names = '''
Andrew
Bob
Charlie
Don
Eric
Frank
Georgia
Harriet
Isla
Jane
'''
from IPython.display import clear_output
import time
import copy
import random
import matplotlib.pyplot as plt
namelist=[]
vals=[]
explodes=[]
first=True
for name in names.splitlines():
    if len(name)>0:
        namelist.append(name)
        vals.append(1)
        explodes.append(0)
index=0
interval=0.001+random.random()*0.005

while interval < 1:
    if index<=0:
        index=len(namelist)-1
    else:
        index-=1
    clear_output(wait=True)
    reorderedexplodes=copy.deepcopy(explodes)
    reorderedexplodes[index]=0.1
    plt.pie(vals, labels=namelist, explode=reorderedexplodes)
    plt.show() 
    time.sleep(interval)
    interval=interval*1.15
print("Winner!")
    

