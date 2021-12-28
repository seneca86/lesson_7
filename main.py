# %%
empty_tuple = ()
stationery = 'pen', 'pencil', 'paper'
furniture = ('chair', 'table', 'couch')
atomic_tuple = 'just_me',
not_a_tuple = 'just_me'
print(empty_tuple)
print(stationery) 
print(furniture)
print(atomic_tuple)
print(not_a_tuple)
# %%
yogurt = 'lemon'
cookie = 'chocolate'
yogurt, cookie = (cookie, yogurt)
print(f'{yogurt=}, {cookie=}')
# %%
list_materials = ['straw', 'wood', 'bricks']
tuple_materials = tuple(list_materials)
tuple_materials + ('concrete',)
tuple_materials * 2
# %%
t1 = (1,2,3)
t2 = (1,1,1,1)
t1 > t2
t2 > t1
(1,1,1) < (2,2,2)
# %%
t1 = ('guitar', 'piano')
print(id(t1))
t2 = ('bass',)
t1 += t2
print(id(t1))
# %%
human_needs = ['security', 'well-being', 'belonging', 'recognition', 'control']
human_needs = list(('security', 'well-being', 'belonging', 'recognition', 'control'))
list('dog')
# %%
question = 'what might be done?, what is wrong?'
question.split()
question.split('?')
question.split(',')
# %%
contract = ['terms', 'conditions', 'prices', 'dates', 'numbers', 'liabilities']
contract[1]
contract[0]
contract[-1]
contract[1::2]
contract[-1:1:-1]
contract
contract.reverse()
contract
# %%
mathematicians = ['Gauss', 'Euler', 'Euclid', 'Fermat', 'Leibniz', 'Pythagoras', 'Ramanujan', 'Poincaré']
mathematicians.append('Galois')
mathematicians.insert(3, 'Von Neumann')
print(mathematicians)
['Gauss'] * 3
# %%
physicists = ['Einstein', 'Newton', 'Maxwell', 'Dirac']
mathematicians.extend(physicists)
print(mathematicians)
mathematicians += ['Feynman', 'Rutherford', 'Faraday']
# %%

