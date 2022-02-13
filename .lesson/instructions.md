# Tuples and lists

## Introduction

We have already encountered _tuples_ and _lists_ in the previous examples. They are structured sequences that combine elements of the same or different type. The main difference between them is that tuples are immutables whereas lists are mutable, with mutability being the capacity to add or subtract elements.

## Tuples

Tuples can be declared with or without parenthesis as long as they are fed a sequence of elements separated by commas (using parenthesis is safer). If the sequence consists of only one element, there must be a trailing comma after it.

```python
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
```

Tuples allows us to assign multiple variables at once: this is called _tuple unpacking_. Among other things, tuple unpacking allows us to flip the values of two variables without a temporary variable.


```python
yogurt = 'lemon'
cookie = 'chocolate'
yogurt, cookie = (cookie, yogurt)
print(f'{yogurt=}, {cookie=}')
```

Tuples can also be created with the `tuple()` function, combined with the `+` operator, and duplicated with the `*` operator.

```python
list_materials = ['straw', 'wood', 'bricks']
tuple_materials = tuple(list_materials)
tuple_materials + ('concrete',)
tuple_materials * 2
```

Tuples are immutable, as said before, so when we appear to modify a tuple as in next example we are actually creating a new one, as we can check with the `id()` command.

** Try it yourself **

Tuples can be compared, and the comparison only evaluates to `True` if it is so elementwise.

```python
t1 = (1,2,3)
t2 = (1,1,1,1)
t1 > t2
t2 > t1
(1,1,1) < (2,2,2)
```

## Lists

Lists are similar to `tuples` but mutable, which means we can add, delete, or replace elements. Also, the same value can occur more than once in a list, but not in a tuple. Lists are defined with the `list()` functions or with the `[]`.


```python
human_needs = ['security', 'well-being', 'belonging', 'recognition', 'control']
human_needs = list(('security', 'well-being', 'belonging', 'recognition', 'control'))
list('dog')
```

Lists can also be created from strings with `split()`, which takes a separator as optional parameter.

```python
question = 'what might be done?, what is wrong?'
question.split()
question.split('?')
question.split(',')
```

### Slicing

As in strings or tuples, single values are extracted by specifying the offset. Multiple values are specified according to the convention `start:end:step`.

```python
contract = ['terms', 'conditions', 'prices', 'dates', 'numbers', 'liabilities']
contract[1]
contract[0]
contract[-1]
contract[1::2]
contract[-1:1:-1]
contract
contract.reverse()
contract
```

Note that the list is not changed until we use `list.reverse()`.

### Add and duplicate items

`append()` is the traditional way of adding items to the end of a list. If we want to insert an element in a specific position, we can use `insert()`. If we want to duplicate items, we may use the `*` operator.

```python
mathematicians = ['Gauss', 'Euler', 'Euclid', 'Fermat', 'Leibniz', 'Pythagoras', 'Ramanujan', 'Poincaré']
mathematicians.append('Galois')
mathematicians.insert(3, 'Von Neumann')
print(mathematicians)
['Gauss'] * 3
```

`extend()` serves to merge one list into another, similarly to `+`.

```python
physicists = ['Einstein', 'Newton', 'Maxwell', 'Dirac']
mathematicians.extend(physicists)
print(mathematicians)
mathematicians += ['Feynman', 'Rutherford', 'Faraday']
```

### Change items

Mutability of lists means that we can alter its content, typically through indexing. The following examples show the flexibility (and risks) that this brings.

```python
mathematicians[0] = 'Baudelaire'
print(mathematicians)
mathematicians[1:3] = ['Shakespeare', 'Milton']
print(mathematicians)
mathematicians[4:] = 'this'
print(mathematicians)
```

### Delete items

There are several ways to remove elements from a list: `del()` will delete them by offset, `remove()` will delete them by name, `pop()` will delete the last one (this is called _LIFO_ in operations and computer science jargon, for "last in first out", or _stack_), `pop(0)` will delete the first one (this is analogously called _FIFO_), etc.

```python
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
```

### Test for values and count occurences

If we want to check whether an item is on a list, and its position (more precisely, the position of the first occurence), we may use `index()`.

```python
alkali = ['hydrogen', 'lithium', 'sodium', 'potassium', 'rubidium', 'caesium', 'francium']
alkali.index('sodium')
```

However, it is more _pythonic_ to use `in`.

```python
'sodium' in alkali
```

Counting occurences is achieved with `count()`.

```python
word = 'abbcccddddeeeee'
word.count('c')
```

### Convert a list to a string

The opposite of the `split()` command is `join()`. Its syntax looks backwards, but it is actually consistent with that of `split()`. The advantage of this syntax (versus a hypothetical `list.join()`) is that it accepts any string or iterable sequence of strings as an input, and not just a list.

```python
noble_gases_string = 'helium, neon, argon, krypton, xenon, radon, oganesson'
noble_gases_list = noble_gases_string.split(', ')
print(noble_gases_list)
separator = '...'
separator.join(noble_gases_list)
```

### Sort the items in a list

There are two ways to sort the elements in a list. One is the _method_ `sort()`, and the other is the _function_ `sorted()`. A method can be loosely described for now as a function that an object applies on itself, meaning the change will remain _in place_.

```python
gods = ['jupiter', 'apollo', 'juno', 'mars', 'vesta', 'neptune']
sorted(gods)
print(gods)
gods.sort()
print(gods)
```

Note that `sorted()` returns a copy of the object, but does not modify the object itself. This is an important distinction between methods and general functions that we will encounter more times down the road.

`sort()` also works with numeric types and with reverse order.

```python
numbers = [1, -3, 10]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
```

### Measure the length

The length of a list (i.e. the number of items in it) is obtained with the `len()` operator:

```python
list_ = ['a', 'b', 'b']
len(list_)
```

Note how we used `list_` as a name for a dummy list as a way to avoid conflation with a keyword with no need to be particularly original.

### Assign and copy

Remember that variables are names (i.e. tags) that we associate with an object. If we label an object with two tags, and we change the content of the object, both tags will point to the changed object. This seems reasonable but may surprise you in practice.

```python
l1 = [10, 20, 30]
l2 = l1
l1[0] = 40
print(l2)
```

So, what should we do if we want an independent, fresh list? We have three options: the `copy()` method, the `list()` function, and the slice `[:]`.

```python
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
```

There is a caveat, though. Since lists are mutable, a list may contain another list that may change, and that change would pass under the radar of the `copy()`, `list()` and `[:]` copies that we generated. To avoid this situation we can use `deepcopy()`, which is part of the `copy` package.

```python
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
```

### Compare lists

List comparison is executed comparing element by element. In case of tie, the number of elements is used to untie.

```python
t1 = (2,2,2)
t2 = (1,1,1,1)
print(t2 < t1)
l1 = [2, 2, 2]
l2 = [1, 1, 1, 1]
print(l2 < l1)
l3 = [2, 2, 2, 2]
print(l1 < l3)
```

### Iterate over a list

Iterating over a list is similar to iterating over a tuple, with similar uses of `break`, `continue`, and `else`.

```python
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
```

The `else` clause gets control when the `for` loop is completed without a `break` or when the initial `for` does not run at all (e.g. if the list is empty).

### Iterate over multiple sequences

The `zip()` function provides a nice trick to iterate over multiple sequences in parallel.

```python
animals = ['dog', 'cat', 'bird', 'cow', 'frog']
sound = ['woof', 'meow', 'tweet', 'moo', 'croak']
for a, s in zip(animals, sound):
    print(a, 'goes', s)
```

In the next chapter we will see how to create a dictionary that captures the correspondence between those two lists. Alternatively, we can also use the `zip()` command to pair the lists:

```python
list(zip(animals, sound))
dict(zip(animals, sound))
```

### Create a list with list comprehension

The `append()` method of adding elements to a list is slow even if we place it inside a loop.

```python
salad = []
salad.append('tomato')
salad.append('olive oil')
salad.append('lettuce')
salad.append('cheese')
salad.append('vinegar')
print(salad)
```

```python
number_list = []
for number in range(10,20):
    number_list.append(number)
print(number_list)
```

The `list()` command also works in combination with `range()`.

```python
list(range(10, 20))
```

A more _pythonic_ way to do this is to use a _list comprehension_, which has the general form `[expression for item in iterable]`.

```python
number_list = [number for number in range(10, 20)]
```

The power of this approach is that is allows to include expressions and conditional statements into the definition. e.g. we may want to have a list with squared numbers of odd numbers.

```python
squared_odds = [n**2 for n in range(0,10) if n%2 !=0]
```

Finally, we can use list comprehensions to build _cartesian products_, which are sets of all ordered pairs of elements in two lists.

```python
body = ['sedan', 'suv', 'pickup', 'limo']
color = ['blue', 'red', 'white']
model = [(b, c) for b in body for c in color]
print(model)
```

### Embed lists

Lists can contain elements of different types, including other lists. The way to access those elements in through one or more indexes.

```python
bedroom = ['chair', 'desk', 'bed']
kitchen = ['fridge', 'stove', 'oven']
living_room = ['sofa', 'coffee table', 'tv']
house = [bedroom, kitchen, living_room]
print(house)
house[0][1]
house[-1][2]
```

## Lists versus tuples

You may want to try "tuple comprehension", but unfortunately there is no such thing and the expression will generate a _generator_ instead (we will cover those later):

```python
tuple_comprehension = (n for n in range(0,10))
tuple_comprehension
```

So, why not forget about tuples and use just lists? Tuple do have a number of advantages, namely:

- They consume less memory
- They are immutable, which is a good property in certain contexts
- They are useful to generate dictionaries (more on this later)
- They have a useful close cousing called _named tuples_, which we will cover later

And, more generally, one must use the simplest structure whenever possible, and tuples are amongs the simplest structures in Python.
