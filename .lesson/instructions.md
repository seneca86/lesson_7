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

### Changing items

