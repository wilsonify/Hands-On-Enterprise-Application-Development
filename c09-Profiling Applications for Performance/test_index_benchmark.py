"""
File: test_index_benchmark.py
Description: Benchmark the index API endpoint
"""
import os
import pytest
import tempfile
import bugzot


@pytest.fixture(scope='module')
def test_client():
    db, bugzot.app.config['DATABASE'] = tempfile.mkstemp()
    bugzot.app.config['TESTING'] = True
    test_client = bugzot.app.test_client()
    with bugzot.app.app_context():
        bugzot.db.create_all()
        yield test_client
    os.close(db)
    os.unlink(bugzot.app.config['DATABASE'])


def test_index_benchmark(test_client, benchmark):
    resp = benchmark(test_client.get, "/")
    assert resp.status_code == 200
