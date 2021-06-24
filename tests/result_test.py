from teext import Err, Ok, Result


def maybe_to_int(s: str) -> Result[int, ValueError]:
    try:
        return Ok(int(s))
    except ValueError as e:
        return Err(e)


def test_ok() -> None:
    r = maybe_to_int("32")
    assert isinstance(r, Ok)
    assert r.value == 32


def test_err() -> None:
    r = maybe_to_int("foobar")
    assert isinstance(r, Err)
    assert isinstance(r.error, ValueError)
