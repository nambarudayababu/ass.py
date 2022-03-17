s=input( )
l=list(s)
x=[ ]
for j in l:
    if j=='a' or j=='A':
        continue
    elif j=='e' or j=='E':
        continue
    elif j=='i' or j=='I':
        continue
    elif j=='o' or j=='O':
        continue
    elif j=='u' or j=='U':
        continue
    else:
        x.append(j)
for j in x:
    print(j,end='')
