heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print(len(heros))
res=0
for ele in heros:
    res+=1
print(res)
heros.append('black panther')
print(heros)
heros.pop()
print(heros)
ind=heros.index('hulk')
heros.insert(ind+1,'black panther')
print(heros)
heros.sort()
print(heros)
heros[1:3]=['doctor strange']
print(heros)

