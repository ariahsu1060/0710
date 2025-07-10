with open("maillist.txt") as f:
    lines = f.readlines()
    final_ans = []
    for i in lines:
        ans = i.split("\n")
        print(ans)
        final_ans.append(ans[0])

f = open("context.txt")
data = f.read()
print(data)
f.close()