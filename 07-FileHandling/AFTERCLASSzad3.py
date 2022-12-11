with open("sample.txt","r") as f:
    lines = len(f.readlines())
with open("sample.txt","r") as f:
    j=0
    while lines > 0:
        for i in range(5):
            j+=1
            print(f"{j}. {f.readline()}")
            lines -=1
        input()