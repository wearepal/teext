# teext – typing extensions extensions

Package which provides useful types.

### [Documentation](https://predictive-analytics-lab.com/teext/)

## Examples

### Constraint types without runtime overhead

These types are most useful in conjunction with static type checkers like mypy.

```python
import teext as tx

a = tx.PositiveInt(5)  # OK

def f(x: tx.PositiveInt) -> None:
    print(x)
    
f(a)  # OK
f(7)  # works at runtime but mypy gives error

b = tx.PositiveInt(-3)  # AssertionError
```
