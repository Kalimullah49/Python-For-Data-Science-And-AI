#while loop and for loop

#while loop

x=0
while(x<5): #jb tk 5 tk ni ponch jata print hota rahay ga.
    print(x)
    x=x+1

#for loop
    
for x in range (5,10): # 5 sa 10 ke rang man rint kry ga
    print(x)


for x in range (5,11): # 5 sa 11 ke rang
    print(x)


#aray : mean data set

    
days =[ "mon","tue","thus","wen","fri","sat","sun"]

for d in days:
    if (d=="fri"):break  # loop stop
    if (d=="fri"):continue # skip d
    print(d)