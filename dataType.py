# Numeric Data types Integer and float
a: int = 20
print(type(a))
print(type(2 + 3))
print(type(2 * 3))
print(type(2 / 3))
print(2 ** 3)
print(2 // 3)
print(5 // 4)
# Math Function
print(round(23.456))
# abs return positive number
print(abs(-23.87))
# Operator precedence
# (), **,*,/,+,-
# Extra data type for numbers=complex(real + imaginary)
print(bin(5))
print(int('0b101', 2))

name = "Sheetal"
print(name)

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
iq = 100
# Expression is iq/5 whereas age=iq/5 is statement
age = iq / 5

# augmentend assignment operator

i = 4
i = i + 2

print(i)
i -= 2
i += 2
print(i)

# Multiline string used with 3 single quotes
long_string = '''
wow
Hi
Hello'''

print(long_string)
# Conversion
print(type(str(i)))
print(type(int(str(i))))
# Escape sequence
weather = "It's \"kind of\" Sunny"
print(weather)
# \t for tab \n new line

name = "sheetal"
age = 27

msg = f' Hi {name} is {age} years old'
print(msg)
msg = ' Hi {} is {} years old'.format(name, age)
print(msg)
msg = ' Hi {1} is {0} years old'.format(age, name)
print(msg)
msg = ' Hi {name} is {your_age} years old'.format(your_age=27, name="sheetal")
print(msg)
# [start:stop:stepover]

print(msg[4:12])
print(msg[4:12:2])
print(msg[-1:-6:])
print(len(msg))
