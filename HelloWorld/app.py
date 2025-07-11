
"""Adding comment to avoid 'Missing module docstring' error.  You can also 
turn off this messages in VSCode. To do so - find settings.json and add:
"python.linting.pylintArgs": ["--disable=C0111"], 
"""

count = 0

for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
print("We have {count} even numbers")
