"""
File: sample_benchmark_test.py
Description: A simple benchmark test
"""

import pytest
import time


def sample_method():
    time.sleep(0.0001)
    return 0


def test_sample_benchmark(benchmark):
    result = benchmark(sample_method)
    assert result == 0


if __name__ == '__main__':
    pytest.main()
