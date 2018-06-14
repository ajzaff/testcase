# testcase
Run tabular unit tests.

## Support

It has been tested with `unittest.TestCase`.
Basically it will work with any class that implements:
- `assertEqual(x, y)`
- `assertRaises(t)` with `__enter__` and `__exit__` handlers for `with`.

## Example

```python
import unittest
import testcase


def foo(x, y):
    return x / y


class FooTest(unittest.TestCase):
    def test_foo(self):
        testcase.runall(self, foo, [
            testcase.new(
                name='1 / 1 = 1',
                args=(1, 1),
                expect=1),
            testcase.new(
                name='raises ZeroDivisionError',
                args=(1, 0),
                raises=ZeroDivisionError),
        ])


if __name__ == '__main__':
    unittest.main()

```