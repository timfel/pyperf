from __future__ import division, print_function, absolute_import

VERSION = (1, 5, 1)
__version__ = '.'.join(map(str, VERSION))

# Clocks
try:
    # Python 3.3+ (PEP 418)
    from time import perf_counter
except ImportError:
    import sys
    import time

    if sys.platform == "win32":
        perf_counter = time.clock
    else:
        perf_counter = time.time

    del sys, time
__all__ = ['perf_counter']


from perf._utils import python_implementation, python_has_jit  # noqa
__all__.extend(('python_implementation', 'python_has_jit'))

from perf._metadata import format_metadata  # noqa
__all__.append('format_metadata')

from perf._bench import Run, Benchmark, BenchmarkSuite, add_runs  # noqa
__all__.extend(('Run', 'Benchmark', 'BenchmarkSuite', 'add_runs'))

from perf._runner import Runner   # noqa
__all__.append('Runner')
