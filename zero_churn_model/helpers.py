"""Misc functions"""

from .imports import * 
from IPython.display import Markdown, display
from scipy.stats import mannwhitneyu as mwtest
from scipy.stats import t 
import inspect


def mw_test(df, col, p_threshold=0.05):
    """Perform a Mann-Whitney U test to compare two groups in a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data to test.
    col : str
        The column name on which to perform the test.
    p_threshold : float, optional
        The p-value threshold to reject the null hypothesis (default is
        0.05).

    Returns
    -------
    str
        'different' if the null hypothesis is rejected, otherwise
        'same'.
    """
    a = df.loc[df['churn'] == 0, col]
    b = df.loc[df['churn'] == 1, col]
    stat, p = mwtest(a, b, alternative='two-sided')
    # if p < threshold, the null hypothesis can be rejected 
    if p < p_threshold:
        return 'different'
    else:
        return 'same'


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


def project_path():
    """Return project path"""
    return dirname(dirname(__file__))


def data_path(subdir, filename, validate=True):
    fp = join(project_path(), 'data', subdir, filename)
    if validate:
        assert exists(fp), fp
    return fp


def load_data(subdir, filename):
    fp = data_path(subdir, filename)
    ext = splitext(fp)[1]
    if ext == '.parquet':
        df = pd.read_parquet(fp)
    elif ext == '.csv':
        df = pd.read_csv(fp)
    else:
        raise Exception(f"filename ext '{ext}' not handled. ")
    return df


def calculate_p_value(r, n):
    """Calculate the p value for a pearson correlation coefficient"""

    if r == 1:
        return 1
    else:
        t_stat = r * np.sqrt((n - 2) / (1 - r**2))
        degs_freedom = n - 2
        p_value = 2 * t.sf(np.abs(t_stat), degs_freedom)
        return p_value


