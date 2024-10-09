d={}
l=[]
with open('poem.txt') as fobj:
        word=fobj.read()
        words=word.strip('\n')
        l=words.split()
        for ind in range(len(l)):
                if l[ind] not in d:
                        d[l[ind]]=1
                else:
                        d[l[ind]]+=1
        print(d)               

            