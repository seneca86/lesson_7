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
