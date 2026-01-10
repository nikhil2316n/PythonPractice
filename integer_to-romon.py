num=2865
values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbuls=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']


roman=''
for i in range(len(values)):
    while(num>=values[i]):
        roman=roman+symbuls[i]
        num=num-values[i]

print(roman)