# teext – typing extensions extensions

Package which provides useful types.

### [Documentation](https://wearepal.github.io/teext/)

## Examples

### Value-constraint types without runtime overhead

These types are most useful in conjunction with static type checkers like mypy.

```python
import teext as tx

def f(x: tx.PositiveInt) -> None:
    print(x)

a = 5
assert tx.is_positive_int(a)
f(a)  # OK
f(7)  # works at runtime but mypy gives error

assert tx.is_positive_int(-3)  # AssertionError
```
