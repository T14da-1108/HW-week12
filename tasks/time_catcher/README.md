## Time catcher (3 points)

`contextmanager` `time` `exceptions`

### Task

Sometimes you really want to check how long the code is running, but you're too lazy to start the profiler.

Write a simple context manager `TimeCatcher` that measures the execution time of the code and throws exceptions if the code takes too long to execute.

```python
with TimeCatcher() as t:
    print(float(t))
    sleep(1)
    print(float(t))
> 0.0000123
> 1.0000234

print(float(t))
> 1.0100246

print(float(t))
> 1.0100246

print(str(t))
> Time consumed: 1.0100


with TimeCatcher(soft_timeout=2, hard_timeout=3) as t:
    sleep(10)

> Traceback (most recent call last): ...
```

Also, you need to implement 3 exceptions: a general `TimeoutException` and one for each of the time limits.


### Clarifications

* To make the task easier - the exception should be thrown AFTER the execution of the context is already based on the results of the work
* If the parameters are incorrect, you need to throw an `AssertionError`
* For a more detailed interface of the context manager, see the tests
* Tip: here you need to create your own class of the context manager with additional `__float__` and `__str__` methods
