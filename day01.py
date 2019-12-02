import pytest



def required_fuel(mass):
    return int(mass / 3) - 2


def test_required_fuel():
    assert required_fuel(12) == 2
    assert required_fuel(14) == 2
    assert required_fuel(1969) == 654
    assert required_fuel(100756) == 33583


if __name__ == '__main__':
    with open('day01_input.txt') as f:
        modules = [int(m) for m in f]
    
    total_fuel = sum(required_fuel(m) for m in modules)
    print(f'Sum of all fuel requirements is {total_fuel}')


def test_required_fuel_forreals():
    assert required_fuel_forreals(14) == 2
    assert required_fuel_forreals(1969) == 966
    assert required_fuel_forreals(100756) == 50346

def required_fuel_forreals(mass):
    total_fuel = 0
    while True:
        mass = required_fuel(mass)
        if mass <= 0:
            break
        total_fuel += mass
    return total_fuel


if __name__ == '__main__':
    total_fuel = sum(required_fuel_forreals(m) for m in modules)
    print(f'Sum of all fuel requirements (taking into account fuel for fuel) is {total_fuel}')


