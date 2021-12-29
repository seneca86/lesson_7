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
mathematicians[0] = 'Baudelaire'
print(mathematicians)
mathematicians[1:3] = ['Shakespeare', 'Milton']
print(mathematicians)
mathematicians[4:] = 'this'
print(mathematicians)
# %%
alkali = ['hydrogen', 'lithium', 'sodium', 'potassium', 'rubidium', 'caesium', 'francium']
del alkali[0]
print(alkali)
alkali.remove('lithium')
print(alkali)
alkali.pop()
print(alkali)
alkali.pop(0)
print(alkali)
alkali.clear()
print(alkali)
# %%
alkali = ['hydrogen', 'lithium', 'sodium', 'potassium', 'rubidium', 'caesium', 'francium']
alkali.index('sodium')
'sodium' in alkali
# %%
word = 'abbcccddddeeeee'
word.count('c')
# %%
noble_gases_string = 'helium, neon, argon, krypton, xenon, radon, oganesson'
noble_gases_list = noble_gases_string.split(', ')
print(noble_gases_list)
separator = '...'
separator.join(noble_gases_list)

# %%
gods = ['jupiter', 'apollo', 'juno', 'mars', 'vesta', 'neptune']
sorted(gods)
print(gods)
gods.sort()
print(gods)
# %%
numbers = [1, -3, 10]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
# %%
list_ = ['a', 'b', 'b']
len(list_)
# %%
l1 = [10, 20, 30]
l2 = l1
l1[0] = 40
print(l2)

# %%
l1 = [10, 20, 30]
l2 = list(l1)
l3 = l1.copy()
l4 = l1[:]
l5 = l1
l1[0] = 'new'
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
# %%
import copy
l1 = ['a', 'b', [1, 2]]
l2 = l1.copy()
l3 = l1[:]
l4 = l1
l5 = copy.deepcopy(l1)
l1[-1][0] = 'hidden change'
print(l2)
print(l3)
print(l4)
print(l5)
# %%

t1 = (2,2,2)
t2 = (1,1,1,1)
print(t2 < t1)
l1 = [2, 2, 2]
l2 = [1, 1, 1, 1]
print(l2 < l1)
l3 = [2, 2, 2, 2]
print(l1 < l3)
# %%
games = ['chess', 'go', 'checkers', 'backgammon', 'othello', 'bridge', 'pocker']
for g in games:
    if g.startswith('c'):
        print('skipped a game starting with c')
        continue
    elif g.endswith('e'):
        print('abort because a game ends with e')
        break
    print(f'{g=}')
else:
    print('completed the loop without any game starting with e')
# %%
animals = ['dog', 'cat', 'bird', 'cow', 'frog']
sound = ['woof', 'meow', 'tweet', 'moo', 'croak']
for a, s in zip(animals, sound):
    print(a, 'goes', s)
# %%
list(zip(animals, sound))
dict(zip(animals, sound))
# %%
salad = []
salad.append('tomato')
salad.append('olive oil')
salad.append('lettuce')
salad.append('cheese')
salad.append('vinegar')
print(salad)
# %%
number_list = []
for number in range(10,20):
    number_list.append(number)
print(number_list)

# %%
list(range(10, 20))
# %%
number_list = [number for number in range(10, 20)]