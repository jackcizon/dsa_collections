from typing import Any, Callable
from ds.stack import StandardStack


def valid_brackets(brackets: str = "{()}<>[]") -> bool:
    bracket_pairs = {"{": "}", "(": ")", "<": ">", "[": "]"}

    stack = StandardStack(100)

    for c in brackets:
        if c in bracket_pairs.keys():  # open bracket
            stack.push(c)
        elif c in bracket_pairs.values():  # close bracket
            if stack.is_empty() or bracket_pairs[stack.pop()] != c:
                return False
    return stack.is_empty()


def rpn(symbols: str) -> Any:
    """recv str symbols, split into tokens, execute func via map"""

    def add(x: float, y: float) -> float:
        return x + y

    def multiply(x: float, y: float) -> float:
        return x * y

    def abs_(x: float) -> float:
        return abs(x)

    def square(x: float) -> float:
        return x * x

    func_map: dict[str, tuple[Callable, int]] = {
        "+": (add, 2),
        "abs": (abs_, 1),
        "square": (square, 1),
        "*": (multiply, 2),
    }

    stack = StandardStack(2**10)

    symbols = [s.strip(" ") for s in symbols.split(",")]

    for s in symbols:
        if s in func_map:
            func_tuple: tuple[Callable, int] = func_map.get(s)
            func: Callable = func_tuple[0]
            params_count: int = func_tuple[1]
            args = [stack.pop() for _ in range(params_count)]
            args.reverse()  # 确保顺序正确(stack的push和pop是相反的), 避免诸如 'a-b' -> 'b-a'的操作导致结果错误
            stack.push(func(*args))
        else:
            try:
                stack.push(float(s))  # 转成数字再入栈
            except ValueError:
                raise ValueError("could not convert string to float")

    last_val = stack.pop()
    if stack.is_empty():
        return last_val
    raise Exception("表达式有误")


def infix_to_suffix(tokens: str) -> str:
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}
    stack = StandardStack(2**10)
    expr = []
    prev_token = "_"

    for token in tokens:
        if token.isnumeric():  # 数字直接输出
            expr.append(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":  # 遇到右括号，弹出直到左括号
            while not stack.is_empty() and stack.top() != "(":
                expr.append(stack.pop())
            stack.pop()  # 弹出左括号
        else:  # 运算符
            if prev_token is None or (prev_token in precedence.keys() and prev_token != ")"):
                raise Exception("invalid expr")
            while not stack.is_empty() and precedence[stack.top()] >= precedence[token]:
                expr.append(stack.pop())
            stack.push(token)

        prev_token = token  # 更新前一个 token

    while not stack.is_empty():  # 弹出剩余运算符
        expr.append(stack.pop())

    expr_str = ",".join(expr)
    expr_str = expr_str.lstrip(",")
    return expr_str
