def arithmetic_arranger(problems,show_answer=False):
    top = ''
    mid = ''
    bottom = ''
    answer_row = ''

    for problem in problems:
        first,operator,second = problem.split()
        first,second = (first,second) if int(first) > int(second) else (second,first)

        answer = str(eval(f'{first}{operator}{second}'))

        first = f'  {first}'
        second = f'{operator}{" " * (len(first) - len(second) - 1)}{second}'
        line = f'{"-" * len(second)}'
        answer = f'{" " * (len(second) - len(answer))}{answer}'

        if problems.index(problem) != len(problems) - 1:
            top += f'{first}    '
            mid += f'{second}    '
            bottom += f'{line}    '
            answer_row += f'{answer}    '
        else:
            top += f'{first}\n'
            mid += f'{second}\n'
            bottom += f'{line}\n'
            answer_row += f'{answer}\n'
    
    arranged_problems = top + mid + bottom

    if show_answer:
        arranged_problems += answer_row

    return arranged_problems