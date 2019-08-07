# pylnd

[![Build Status](https://travis-ci.org/smadici-labs/pylnd.svg?branch=master)](https://travis-ci.org/smadici-labs/pylnd)
[![Documentation Status](https://readthedocs.org/projects/pylnd/badge/?version=latest)](https://pylnd.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/smadici-labs/pylnd/branch/master/graph/badge.svg)](https://codecov.io/gh/smadici-labs/pylnd)


Python client for Lightning Network Deamon [(LND)](https://github.com/lightningnetwork/lnd) with batteries included.

Planned support for both REST and gRPC.

Only supporting Python 3 since we should not be using Python 2.x anymore.

## Getting started

### Development

Make a virtual environment,

```bash
python3 -m virtualenv -p python3 .venv
source .venv/bin/activate
```

Then install,

`python setup.py develop`

To run tests execute,

`pytest`

with code coverage,

`pytest --cov=pylnd`

## License

This project is licensed under the MIT License - see the LICENSE file for details