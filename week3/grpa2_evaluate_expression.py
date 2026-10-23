"""GRPA 2 — Postfix (Reverse Polish Notation) expression evaluator using a stack."""

_OPERATORS = frozenset({"+", "-", "*", "/", "**"})


def evaluate_expression(exp: str) -> float:
    """Evaluate a postfix expression and return the result as a float.

    Tokens are separated by spaces. Supported operators: +, -, *, /, **.
    For a binary operator, the first popped value is the *right* operand (B)
    and the second popped value is the *left* operand (A), so the operation
    performed is  A op B.

    Args:
        exp: A postfix expression string with space-separated tokens,
             e.g. ``"2 3 1 * + 9 -"``.

    Returns:
        The evaluated numeric result as a float.

    Raises:
        ValueError: If the token is neither a valid number nor a known operator.

    Time:  O(n)  where n = number of tokens
    Space: O(n)  for the operand stack
    """
    stack: list[float] = []

    for token in exp.split():
        if token in _OPERATORS:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
            elif token == "**":
                stack.append(a**b)
        else:
            stack.append(float(token))

    return stack[0]


# ---------------------------------------------------------------------------
# Backward-compatible alias matching the original graded assignment signature
# ---------------------------------------------------------------------------
EvaluateExpression = evaluate_expression
