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

