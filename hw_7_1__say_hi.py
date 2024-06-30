def say_hi(name='Slim Shady', age=52):
    if age < 0:
        return 'incorrect age value: should be non-negative'

    years_plural = 'year' if age == 1 else 'years'
    return f"Hi. My name is {name} and I'm {age} {years_plural} old"


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
