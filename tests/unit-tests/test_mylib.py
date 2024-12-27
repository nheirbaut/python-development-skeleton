from mylib.mylib import is_even


def test_is_even_with_even_number() -> None:
    """Test is_even() with an even number."""
    assert is_even(4)

def test_is_even_with_odd_number() -> None:
    """Test is_even() with an odd number."""
    assert not is_even(3)

def test_is_even_with_zero() -> None:
    """Test is_even() with zero, which is considered even."""
    assert is_even(0)

def test_is_even_with_negative_even() -> None:
    """Test is_even() with a negative even number."""
    assert is_even(-2)

def test_is_even_with_negative_odd() -> None:
    """Test is_even() with a negative odd number."""
    assert not is_even(-3)
