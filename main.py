# %%
hlmi = {'2030':0.10, '2050':0.50, '2100':0.90}
hlmi = {
    '2030':0.10,
    '2050':0.50,
    '2100':0.90,
    }
# %%
# %%
english_to_german = dict(dog='Hund', cat='Katz', cow='Kuh')
# %%
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
# %%
songs = {
    'elvis': 'such a night',
    'beatles': 'all my loving',
    'stones': 'start me up',
}
songs['beatles'] = 'I am the walrus'
songs['deep purple'] = 'moby dick'
print(songs)
# %%
hits = {}
hits['beatles'] = 'I want to hold your hand'
hits['beatles'] = 'Back in the USRR'
hits['beatles'] = 'Dear Prudence'
hits

# %%
songs['beatles']
songs.get('stones')
'give me shelter' in songs
songs.get('Lucy in the sky with diamonds', 'this song is not stored')
# %%
songs.keys()
songs.values()
list(songs.keys())
list(songs.values())
# %%
songs.items()
list(songs.items())
# %%
len(songs)
# %%
old_albums = {'white album': 'beatles', 'rubber soul': 'beatles', 'how the west was won': 'led zeppelin'}
new_albums = {'unearthed': 'johnny cash', 'give up': 'the postal service'}
{**old_albums, **new_albums}
old_albums.update(new_albums)
print(old_albums)
# %%
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
# %%
d1 = {'Apple': 'AAPL', 'Amazon':'AMZN', 'Tesla':'TSLA'}
d2 = d1
d1['Palantir'] = 'PLTR'
print(d2)
# %%
d3 = d1.copy()
print(d3)
d1['Gold'] = 'GLD'
print(d3)
# %%
import copy
d4 = {'stocks':['AAPL', 'AMZN'], 'commodities':['GLD']}
d5 = d4.copy()
d6 = copy.deepcopy(d4)
d4['commodities'].append('SLV')
print(f'{d4=}')
print(f'{d5=}')
print(f'{d6=}')
# %%
d4 == d5
d6 != d5

# %%
portfolio = {'stocks':['Berkshire', 'GE'], 'bonds':['TIPS', 'T-bills']}
for security in portfolio.values():
    print(security)
for asset_class in portfolio.keys():
    print(asset_class)
for pair in portfolio.items():
    print(pair)
for asset_class, security in portfolio.items():
    print(f'My portfolio contains {asset_class}, specifically {security}')
# %%
words = 'How big is the cosmic endowment?'
letter_count = {word:len(word) for word in words.split()}
print(letter_count)
letter_count_large = {word:len(word) for word in words.split() if len(word)>3}
print(letter_count_large)
# %%
