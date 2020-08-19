# teext -- typing extensions extensions

Package which provides useful types.

### [Documentation](https://predictive-analytics-lab.com/teext/)

## Examples

### Constraint types without runtime overhead

These types are most useful in conjunction with static type checkers like mypy.

```python
from teext import PositiveInt

a = PositiveInt(5)  # OK

def f(x: PositiveInt) -> None:
    print(x)
    
f(a)  # OK
f(7)  # works at runtime but mypy gives error

b = PositiveInt(-3)  # AssertionError
```
