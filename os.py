import os
# if (not os.path.exists()):
# os.mkdir("data")

if ( not os.path.exists("data")):
    os.mkdir("data")


for i in range(0, 100):
    os.rename(f"data/day{i+1}", f"data/tutorials{i+1}")
    

