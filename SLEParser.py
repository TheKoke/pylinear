# class for parse string expressions to linear system
class ShuntingYard:
    @staticmethod
    def get_extend_matrix(expressions: list[str]) -> list[list[float]]:
        extendedmatrix = []
        vars = ShuntingYard.get_all_variables(expressions)

        for i in range(len(expressions)):
            extendedmatrix.append([])
            for j in range(len(vars)):
                extendedmatrix[i].append(
                    ShuntingYard.get_variable_coefficient(expressions[i], vars[j])
                )

        for i in range(len(expressions)):
            extendedmatrix[i].append(ShuntingYard.get_free_coeff(expressions[i]))

        return extendedmatrix
    
    @staticmethod
    def get_all_variables(expressions: list[str]) -> list[str]:
        result = []

        for i in range(len(expressions)):
            partVariables = ShuntingYard.get_equation_variables(expressions[i])
            ShuntingYard.merge_lists(result, partVariables)

        result.sort()
        return result

    @staticmethod
    def get_equation_variables(equation: str) -> list[str]:
        variables = []
        i = 0

        while i < len(equation):
            pretend = ''
            while i < len(equation) and equation[i].isalpha():
                pretend += equation[i]
                i += 1

            if pretend != '':
                variables.append(pretend)
                pretend = ''
                continue
            
            i += 1
        return variables

    @staticmethod
    def get_variable_coefficient(equation: str, variable: str) -> float:
        allcoeffs = []
        leftside = equation.split('=')[0]
        rightside = equation.split('=')[1]

        window = len(variable)

        for i in range(len(leftside) - window + 1):
            if leftside[i: i + window:] == variable:
                allcoeffs.append(ShuntingYard.current_coefficient(leftside, i, False))

        for i in range(len(rightside) - window + 1):
            if rightside[i: i + window:] == variable:
                allcoeffs.append(ShuntingYard.current_coefficient(rightside, i))
        
        return sum(allcoeffs)

    @staticmethod
    def current_coefficient(equation: str, var_index: int, negative=True) -> float:
        pretend = ''
        for i in range(var_index - 1, -1, -1):
            if equation[i].isdigit() or equation[i] == '.':
                pretend = equation[i] + pretend

            if equation[i].isalpha() or equation[i] in ['+', '-']:
                break
        
        pretend = ShuntingYard.find_sign(equation, var_index) + pretend

        if pretend == '+':
            return -1 if negative else 1

        if pretend == '-':
            return 1 if negative else -1

        return -1 * float(pretend) if negative else float(pretend)

    @staticmethod
    def find_sign(equation: str, curindex: int) -> str:
        if curindex - 1 < 0:
            return '+'
        
        for i in range(curindex - 1, -1, -1):
            if equation[i] in ['+', '-']:
                return equation[i]

        return '+'

    @staticmethod
    def get_free_coeff(equation: str) -> float:
        leftside = equation.split('=')[0]
        rightside = equation.split('=')[1]

        allcoeff = []

        for i in range(len(leftside)):
            if leftside[i].isdigit():
                allcoeff.append(-1 * ShuntingYard.checkup_for_freecoeff(leftside, i))
            
        for i in range(len(rightside)):
            if rightside[i].isdigit():
                allcoeff.append(ShuntingYard.checkup_for_freecoeff(rightside, i))

        return sum(allcoeff) 

    @staticmethod
    def checkup_for_freecoeff(equation: str, currindex: int) -> float:
        if currindex - 1 >= 0:
            part_of_another = (equation[currindex - 1].isdigit() 
                or equation[currindex - 1] == '.')

            if part_of_another:
                return 0

        pretend = ''
        i = currindex
        while i < len(equation):
            if equation[i].isalpha():
                return 0

            if equation[i] in ['+', '-']:
                break

            if equation[i].isdigit() or equation[i] == '.':
                pretend += equation[i]
            i += 1

        return float(ShuntingYard.find_sign(equation, currindex) + pretend)

    @staticmethod
    def merge_lists(first: list, second: list):
        for i in second:
            if i not in first:
                first.append(i)
