from arithmetic_arranger import arithmetic_arranger
from unittest import main

while True:
    equations = input('Give me up to 5 equations split by commas\n')
    equations = equations.replace(', ', ',').split(',')
    show_answer = input('Do you want to see the answers for these equations? [yes, no]\n')
    show_answer = True if 'y' in show_answer.lower() else False
    print(arithmetic_arranger(equations,show_answer))
# print(arithmetic_arranger(['32 + 698','3801 - 2','45 + 43','123 + 49']))

# main(module='test_module', exit=False)