r_num=2
c_num=3
twod_arr=[[0 for col in range(c_num)] for row in range(r_num)]
value=0
for row in range(r_num):
    for col in range(c_num):
        value+=1
        twod_arr[row][col]=value
print(twod_arr[1][1])