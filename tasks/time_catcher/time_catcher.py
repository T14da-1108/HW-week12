import time
from typing import Optional


class TimeoutException(Exception):
    """Base exception for timeouts."""
    pass


class SoftTimeoutException(TimeoutException):
    """Exception raised when the soft timeout is exceeded."""
    pass


class HardTimeoutException(TimeoutException):
    """Exception raised when the hard timeout is exceeded."""
    pass

class TimeCatcher:
    def __init__(self, soft_timeout: Optional[float] = None, hard_timeout: Optional[float] = None) -> None:
        """
        Initialize the TimeCatcher context manager.
        :param soft_timeout: Soft timeout in seconds (optional).
        :param hard_timeout: Hard timeout in seconds (optional).
        """
        # Validate timeout values
        if soft_timeout is not None and soft_timeout <= 0:
            raise AssertionError("Soft timeout must be greater than 0 or None.")
        if hard_timeout is not None and hard_timeout <= 0:
            raise AssertionError("Hard timeout must be greater than 0 or None.")
        if soft_timeout is not None and hard_timeout is not None and soft_timeout > hard_timeout:
            raise AssertionError("Soft timeout must be less than or equal to hard timeout.")

        self.soft_timeout = soft_timeout
        self.hard_timeout = hard_timeout
        self.start_time = None
        self.end_time = None

    def __enter__(self) -> "TimeCatcher":
        """Start the timer."""
        self.start_time = time.perf_counter()
        self.end_time = None
        return self

    def __exit__(self, exc_type, exc_value, _) -> None:
        """Stop the timer and check for timeout violations."""
        self.end_time = time.perf_counter()
        elapsed = self.elapsed_time

        # Check soft timeout only if it's not None and not zero
        if self.soft_timeout is not None and self.soft_timeout > 0 and elapsed > self.soft_timeout:
            raise SoftTimeoutException(f"Soft timeout of {self.soft_timeout:.4f} seconds exceeded.")

        # Check hard timeout only if it's not None and not zero
        if self.hard_timeout is not None and self.hard_timeout > 0 and elapsed > self.hard_timeout:
            raise HardTimeoutException(f"Hard timeout of {self.hard_timeout:.4f} seconds exceeded.")

    @property
    def elapsed_time(self) -> float:
        """Calculate the elapsed time."""
        if self.start_time is None:
            raise RuntimeError("Timer has not started.")
        end_time = self.end_time if self.end_time is not None else time.perf_counter()
        return end_time - self.start_time

    def __float__(self) -> float:
        """Return the elapsed time as a float."""
        return self.elapsed_time

    def __str__(self) -> str:
        """Return a string representation of the elapsed time."""
        return f"Time consumed: {self.elapsed_time:.4f}"
