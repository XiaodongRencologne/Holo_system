# python-tcs

Base set of libraries to talk to telescope control system via http

# install
python setup.py install

# run tests
python setup.py pytest

## run individual test
python -m pytest -v -v -v tests/test_tcs.py -k test_azi_scan
