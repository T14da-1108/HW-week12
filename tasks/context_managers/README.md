## Context Managers (3 points)

`try...except` `contextmanager` `sys.exc_info` `traceback.format_exception_only` `exc.with_traceback`

### Task

Exceptions are a wonderful thing. Combined with context managers, their capabilities increase manifold.

Write several context managers for exception handling.

#### Exception Suppressor

```python
with supresser(type_one, ...):
    do_smth()
```

Catches exceptions of specified (and only specified) types and returns control to the flow. The exception is not thrown further.

#### Exception Renamer

```python
with retyper(type_from, type_to):
    do_smth()
```

Changes the type of exception, leaving the error content (args attribute) and traceback unchanged. The exception is thrown further.

#### Exception Dumper

```python
with dumper(stream):
    do_smth()
```

Writes the error message to the passed stream and throws it further.

### Clarifications

* `dumper` should write to `sys.stderr` by default if `stream is None`.
* To better understand exceptions, what arguments and traceback they have, read in [exceptions](https://docs.python.org/3/library/exceptions.html)
* To extract information about the caught exception, use the [sys](https://docs.python.org/3/library/sys.html#sys.exc_info) module
* To dump only the exception without traceback in dumper, you can use [traceback.format_exception_only](https://docs.python.org/3/library/traceback.html#traceback.format_exception_only)

---