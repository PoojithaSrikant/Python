#if else
marks=90
if marks>=90:
    print("allowed for games")
elif marks>=70 and marks<=90:
    print("study hard")
else:
    print("lotty charge")

#-----------largest number
a=[500,300,100,700]
max_num = a[0]
for x in a:
    if x>=max_num:
        max_num=x
print(max_num)

#----------smallest number
a=[500,300,100,700]
min_num = a[0]
for x in a:
    if x<min_num:
        min_num=x
print(min_num)


