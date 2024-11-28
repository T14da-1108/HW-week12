from contextlib import contextmanager
from typing import Iterator, TextIO, Type
import sys
import traceback


@contextmanager
def supresser(*types_: Type[BaseException]) -> Iterator[None]:
    try:
        yield
    except types_:
        # Suppress the specified exceptions and return control to the flow
        pass


@contextmanager
def retyper(type_from: Type[BaseException], type_to: Type[BaseException]) -> Iterator[None]:
    try:
        yield
    except type_from as e:
        # Retype the exception, preserving args and traceback
        raise type_to(*e.args).with_traceback(e.__traceback__) from None


@contextmanager
def dumper(stream: TextIO | None = None) -> Iterator[None]:
    if stream is None:
        stream = sys.stderr  # Default to stderr if no stream is provided
    try:
        yield
    except BaseException as e:
        # Write the exception message to the provided stream
        exception_msg = ''.join(traceback.format_exception_only(type(e), e))
        stream.write(exception_msg)
        stream.flush()
        # Re-raise the exception to propagate it further
        raise
