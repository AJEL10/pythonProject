d={1:4,0:2,3:5,6:7}
print('original dictionary ',d)
sorted_d=sorted(d.items())
print('dictionary in ascending order by value :',sorted_d)
sorted_d=sorted(d.items(),reverse=True)
print('dictionary in descending order in value:',sorted_d)

