# Dictionaries

## Definition

Dictionaries, also called _hashes_, _associate arrays_, or _hashmaps_, are pairs of _keys_ and _values_, which can consist of any of Python's immutable types. They are created with the `{}` symbol and with `key:value` pairs.

Let's build a simple dictionary that captures the answer to the question "When will we have human-level machine intelligence?", including years and probabilities.

```python
hlmi = {'2030':0.10, '2050':0.50, '2100':0.90}
```

For longer dictionaries, we will typically arrange the syntax as follows (the trailing comman and the indentation are optional):

```python
hlmi = {
    '2030':0.10,
    '2050':0.50,
    '2100':0.90,
    }
```

When the key is a string and has a legal string name, we can declare a dictionary in an alternative way.

```python
english_to_german = dict(dog='Hund', cat='Katz', cow='Kuh')
```

These sequences can easily be transformed to dictionaries:
- Lists of two-item lists
- Lists of two-item tuples
- Tuples of two-item lists
- Lists of two-character strings
- Tuples of two-character strings

```python
ll = [['Spain', 'Madrid'], ['US', 'NYC'], ['China', 'Beijing']]
dict(ll)
tl = (['Spain', 'Madrid'], ['US', 'NYC'], ['China', 'Beijing'])
dict(tl)
lt = [('Spain', 'Madrid'), ('US', 'NYC'), ('China', 'Beijing')]
dict(lt)
tt = (('Spain', 'Madrid'), ('US', 'NYC'), ('China', 'Beijing'))
dict(tt)
ls = ['ax', 'by', 'cz']
dict(ls)
ts = ('ax', 'by', 'cz')
dict(ts)
```

## Add or change keys

Adding a key or chaning a key in a dictionary has the same syntax. This is a consequence of keys in a dictionary being unique. ```python
```python
songs = {
    'elvis': 'such a night',
    'beatles': 'all my loving',
    'stones': 'start me up',
}
songs['beatles'] = 'I am the walrus'
songs['deep purple'] = 'moby dick'
print(songs)
```

Another consequence is that, if we use a key more than once, the last value prevails.

```python
hits = {}
hits['beatles'] = 'I want to hold your hand'
hits['beatles'] = 'Back in the USRR'
hits['beatles'] = 'Dear Prudence'
hits
```

## Retrieve a key

Retriveing a key can be done with `[]` or with `get()`; existance checks can be done with `in`. `get()` has an optional value that is returned if the search is unsuccessful.

```python
songs['beatles']
songs.get('stones')
'give me shelter' in songs
songs.get('Lucy in the sky with diamonds', 'this song is not stored')
```

`keys()` retrieves all keys, whereas `values()` retreives all values. The result is an iterable view, which is a temporal view, and which is more useful if put into a list.

```python
songs.keys()
songs.values()
list(songs.keys())
list(songs.values())
```

Keys and values can be retrieved simultaneously with the `items()` method.

```python
list(songs.items())
```

Finally, the `len()` function counts the key-pairs.

```python
len(songs)
```

### Combine dictionaries

Dictionaries can be combined with the `**` operator or with the `update()` function.

```python
old_albums = {'white album': 'beatles', 'rubber soul': 'beatles', 'how the west was won': 'led zeppelin'}
new_albums = {'unearthed': 'johnny cash', 'give up': 'the postal service'}
{**old_albums, **new_albums}
old_albums.update(new_albums)
print(old_albums)
```

### Delete items

Items can be deleted with the `del` command or with `pop()`. If we want to remove all items, we use `clear()`, and if we want to check existance, we will use `in`.

```python
g7_pop = {
    'US':333,
    'France':67,
    'Germany':83,
    'Japan':125,
    'Italy':59,
    'UK':67,
    'Canada':38,
    }
print(g7_pop)
del g7_pop['UK']
print(g7_pop)
g7_pop.pop('Italy')
print(g7_pop)
g7_pop.pop('France', 'item not found')
g7_pop.pop('Spain', 'item not found')
print(g7_pop)
g7_pop.clear()
print(g7_pop)
'UAE' in g7_pop
```

### Assign, copy, deepcopy

These commands work as in lists, so let's recap the behavior with a few examples.

```python
d1 = {'Apple': 'AAPL', 'Amazon':'AMZN', 'Tesla':'TSLA'}
d2 = d1
d1['Palantir'] = 'PLTR'
print(d2)
```

```python
d3 = d1.copy()
print(d3)
d1['Gold'] = 'GLD'
print(d3)
```

```python
import copy
d4 = {'stocks':['AAPL', 'AMZN'], 'commodities':['GLD']}
d5 = d4.copy()
d6 = copy.deepcopy(d4)
d4['commodities'].append('SLV')
print(f'{d4=}')
print(f'{d5=}')
print(f'{d6=}')
```

### Compare dictionaries

Comparing dictionaries only make sense to check if they are equal or different, there is no `<` or `>`.

```python
d4 == d5
d6 != d5
```

Note that the order in which the keys were created does not matter, because keys in a dictionary do not have an intrinsic order.

### Iterate over dictionaries

Iteration can be done over `keys()`, `values()`, or `items()` (both).

```python
portfolio = {'stocks':['Berkshire', 'GE'], 'bonds':['TIPS', 'T-bills']}
for security in portfolio.values():
    print(security)
for asset_class in portfolio.keys():
    print(asset_class)
for pair in portfolio.items():
    print(pair)
for asset_class, security in portfolio.items():
    print(f'My portfolio contains {asset_class}, specifically {security}')
```

### Dictionary comprehensions

Also analogous to list comprehensions, let's illustrate them directly with an example.

```python
words = 'How big is the cosmic endowment?'
letter_count = {word:len(word) for word in words.split()}
print(letter_count)
letter_count_large = {word:len(word) for word in words.split() if len(word)>3}
print(letter_count_large)
```