from khwarizmi import exc, equations, linear, quadratic


def get_type(eqtn):
    """Returns an instance of the class that should correspond
    to the equation eqtn."""

    regular = equations.Equation(eqtn)

    if len(regular.unknowns) == 1:
        return regular
    elif len(regular.unknowns) == 2:
        return linear.Linear(eqtn)

def resolve_arguments(list_of_arguments):

    indexer = 0

    for argument in list_of_arguments:
        if argument.isdigit():
            list_of_arguments[indexer] = int(argument)
        indexer += 1

    return list_of_arguments

def apply_method(eqtn, operation):

    eqtn= get_type(eqtn)
    indexer = 0

    operation = resolve_arguments(operation)

    if isinstance(eqtn, linear.Linear):

        # If an argument was passed
        if len(operation) > 2:
            return str(vars(linear.Linear)[operation[0]](eqtn, operation[1], operation[2]))
        elif len(operation) > 1:
            return str(vars(linear.Linear)[operation[0]](eqtn, operation[1]))

        return str(vars(linear.Linear)[operation[0]](eqtn))

    elif isinstance(eqtn, equations.Equation):
        if len(operation) > 1:
            return (str(vars(equations.Equation)[operation[0]](eqtn, int(operation[1]))))
        return str(vars(equations.Equation)[operation[0]](eqtn))

def get_attribute(eqtn, operation):

    eqtn = get_type(eqtn)
    return vars(eqtn)[operation]

def solve(eqtn, operation):

    operation = operation.replace('(', ' ').replace(')', '').replace(',', '')
    operation = operation.split()

    if operation[0] in vars(linear.Linear) or operation[0] in vars(equations.Equation):
        return apply_method(eqtn, operation)

    return get_attribute(eqtn, operation[0])