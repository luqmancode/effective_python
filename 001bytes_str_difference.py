a = b'h\x65llo'
print(a, type(a)) # b'hello' <class 'bytes'>
print(list(a)) # [104, 101, 108, 108, 111]

b = 'a\u0300 propos'
print(b, type(b)) # à propos <class 'str'>
print(list(b)) # ['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']

# bytes have numeric encoding and Strings have Unicode encoding contradicts
print(a.decode(), a.decode('utf-8')) # hello hello
print(b.encode()) # b'a\xcc\x80 propos'

pantry = [
    ('avocado', 1.25),
    ('bananas', 2.5),
    ('cherries', 15)
]

for idx, (item, price) in enumerate(pantry, start=1):
    print('#%d:  %-10s = %.2f' % (idx, item.title(), price))

template = "%s loves food, See %s cooks as well"
name = 'Max'
print(template % (name, name))

template2 = "%(name)s loves food, See %(name)s cooks as well"
dict_name = {"name": 'Mike'}
print(template2 % dict_name)


c = 1234.5678
print(format(c, ',.2f')) # 1,234.57


print('{0} loves food, See {0} cooks'.format(name))

key = 'my_var'
value = 1.234

f_string = f'{key:<10} = {value:.2f}'
c_tuple = '%-10s = %.2f' % (key, value)
c_dict = "%(key)-10s = %(value).2f" % {"key": key, "value": value}
str_args = "{:<10} = {:.2f}".format(key, value)
str_kw = "{key:<10} = {value:.2f}".format(key=key, value=value)

assert c_tuple == c_dict == str_args == str_kw == f_string

# Support multiline f-string
for i, (item, count) in enumerate(pantry):
    print(f'#{i+1}: '
    f'{item.title():<10s} = '
    f'{round(count)}')

