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
dict(l1)
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

