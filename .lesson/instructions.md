# Tuples and lists

## Introduction

We have already encountered _tuples_ and _lists_ in the previous examples. They are sequence structured that combine elements of the same or different type. The main difference between them is that tuples are immutables whereas lists are mutable, with mutability being the capacity to add or subtract elements.

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

```python
t1 = (1,2,3)
t2 = (1,1,1,1)
t1 > t2
t2 > t1
(1,1,1) < (2,2,2)
```

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

There are two ways to sort the elements in a list. One is the _method_ `sort()`, and the other is the _function_ `sorted()`. A method can be loosly described for now as a function that an object applies on itself, meaning the change will remain _in place_.

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

The length