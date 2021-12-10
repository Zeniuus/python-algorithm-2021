import re
from typing import List, Any


def print_result(solution: object, inputs: List, expected: Any):
    method_names = [method_name for method_name in dir(solution)
                    if callable(getattr(solution, method_name)) and not re.match(r'__[\w\W_-]*__', method_name)]
    func = getattr(solution, method_names[0])  # TODO: 특정 시그니처의 함수 가져오게 하기
    result = func(*inputs)
    if input != expected:
        print(f'expected : {expected}\n'
              f'actual   : {result}')
