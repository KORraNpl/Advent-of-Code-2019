def fuel_required_by_module(module_mass=0):
    return module_mass // 3 - 2


def total_fuel(modules):
    total = 0
    for module in modules:
        total += fuel_required_by_module(int(module))

    return total


def fuel_required_by_module_v2(module_mass=0):
    if (module_mass // 3 - 2) < 0:
        return 0
    return (module_mass // 3 - 2) + fuel_required_by_module_v2(module_mass // 3 - 2)


def total_fuel_v2(modules):
    total = 0
    for module in modules:
        total += fuel_required_by_module_v2(int(module))

    return total


if __name__ == '__main__':
    answer = 0
    with open('input.txt', 'r') as f:
        answer = total_fuel_v2(f)

    print(answer)
