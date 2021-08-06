from function_collection.main import timer_wrapper, exp_by_squaring

def calc97():
    return str(28433 * exp_by_squaring(2, 7830457) + 1)[-10:]

print(timer_wrapper(calc97))