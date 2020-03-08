def fizzbuzz_convert(number):
    if number % 15 == 0:
        return 'fizzbuzz'

    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'


assert fizzbuzz_convert(3) == 'fizz'
assert fizzbuzz_convert(5) == 'buzz'
assert fizzbuzz_convert(15) == 'fizzbuzz'
