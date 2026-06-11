# greeter

A tiny demo Python greeting library, used to exercise Conductor end-to-end.

## Usage

```python
from greeter import hello
hello("World")   # -> "Hello, World!"
from greeter import farewell
farewell("World")  # -> "Goodbye, World!"
```

## Tests

```bash
python -m unittest discover -s tests
```
