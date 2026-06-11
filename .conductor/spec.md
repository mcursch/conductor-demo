# greeter — project spec

A tiny Python greeting library. Keep it minimal.

## Current state

- `greeter.hello(name)` returns `"Hello, {name}!"`.
- Tests run with `python -m unittest discover -s tests`.

## Desired work

Add exactly one small feature — a farewell counterpart to `hello`:

- Add `greeter.farewell(name)` that returns `"Goodbye, {name}!"`.
- Add a unit test for it in `tests/test_greeter.py`.
- Leave the existing `hello` behavior unchanged.

This single farewell feature is the only work needed. Do not add anything else
(no CLI, no packaging, no extra functions).
