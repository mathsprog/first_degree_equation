fact_x=[]
consts=[]
allfracts={}

def initlize_item(insta,bool):
    if insta.startswith('-') and insta.count('-')==2:
        list = insta.split('-')
        list.remove(list[0])
        consts.append(-float(list[0]))
        if not bool:consts.append(-float(list[1]))
        else:fact_x.append(-float(list[1]))
    if insta.startswith('-') and insta.count('+')>0:
            list=insta.split('+')
            consts.append(float(list[0]))
            if not bool:consts.append(float(list[1]))
            else:fact_x.append(float(list[1]))

    if insta.startswith('+') and  insta.count('-')==0:
        list = insta.split('+')
        list.remove(list[0])
        consts.append(float(list[0]))
        if not bool:consts.append(float(list[1]))
        else:fact_x.append(float(list[1]))

    if insta.startswith('+') and  insta.count('-')>0:
        list = insta.split('-')
        consts.append(float(list[0]))
        if not bool:consts.append(-float(list[1]))
        else:fact_x.append(-float(list[1]))
    if not insta.startswith('+') and not insta.startswith('-') and insta.count('-')>0:
        list = insta.split('-')
        consts.append(float(list[0]))
        if not bool:consts.append(-float(list[1]))
        else:fact_x.append(-float(list[1]))
    if not insta.startswith('+') and not insta.startswith('-') and insta.count('+')>0:
        list = insta.split('+')
        consts.append(float(list[0]))
        if not bool:consts.append(float(list[1]))
        else:fact_x.append(float(list[1]))

def check(str):
    print(str)
    last_item=''
    bb = str.split('x')
    if bb[len(bb) - 1] == '':
        bb.pop()
        #print(bb, 'x')
    else:

        last_item=bb[len(bb) - 1]
        bb.pop()
    for i in bb:

        if i == '+' or i=='':
            bb[bb.index(i)] = '1'

        if i == '-':
            bb[bb.index(i)] = '-1'
    print(bb,last_item)
    for item in bb:
        try:
            if isinstance(float(item),float):
                fact_x.append(float(item))
        except:
            initlize_item(item, True)


    if len(last_item)>0:
        initlize_item(last_item,False)


    print({'x':fact_x,'consts':consts})


check('9-7x-8+6x')
#check('9x+7-6x')
#check('-x-7x+8-6')#1
#check('-x+7x+8-6x')
#check('-x+x+8-6')

print()
eq='9-7x-8+6x=7x'
left=eq.split('=')[0]
add=left.split('+')
minus=left.split('-')
listx=left.split('x')
