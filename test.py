# import datetime
# now = datetime.datetime.today()
# print(now)
#
# date=datetime.datetime(2019,5,5)
# print(date)
# weekday = datetime.date(2019,5,5).weekday()
# print(weekday)  #顯示六 但是要加一變禮拜天

#
# n=2
# num = 0
# while n>=2:
#     num += 2**n-1
#     n+=1
#     print(num)

# list2=[[1,2],[35,70],[18,39,66,83,95,73,45,21]]
# a=0
# j=0
# for i in range(len(list2)):
#     while j>=0:
#         j+=1
#         a+=list2[i][j]
#         break
#     print(a,end=' ')
# print()
list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=[1,2,3,4]


sum=[]
for i in range(len(list1)):
    sum += list1[i] * list2[i]
print(sum)

#
#    count = 0
#     countyear=0
#     sum = 0
#     a=0
#     list1=[]
#     for i in range(len(listrain)): #  0-2(1~3層)
#         for j in range(len(listrain[i])):  #  0-3 (1-4列
#             countyear+=1
#             for k in range(len(listrain[i][j])): #  0-2 (1-3排)
#                 count += 1
#                 sum += listrain[i][j][k]
#                 list1.append(sum)
#                 if count%3 == 0:
#                     a += sum
#                 print(a)
#         if countyear%5==0:
#             break
#         print('{} 的季平均 {}'.format(listseason[i],a))
#
# print(seasonavg())