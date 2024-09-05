"""Misc functions"""

from .imports import * 
from IPython.display import Markdown, display
import inspect


def summarize_time(time_start, time_end, verbose=True):
    elapsed = time_end - time_start
    if verbose:
        print(f"that took {elapsed/60:.1f} minutes. ")
    return elapsed


def sample_dataframe(df, nrows=1000, ncols=1000):
    """Create a smaller dataframe for initial testing"""
    # create a copy for temporary testing
    sl = df.T.sample(ncols).T.sample(nrows).copy()

    return sl


def display_source(func):
    """In jupyter, display source of function"""
    x = inspect.getsource(func)
    x = f"```python\n{x}\n```"
    display(Markdown(x))

