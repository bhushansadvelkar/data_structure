## Cursor Cloud specific instructions

This is a pure Python (3.8+) data structures & algorithms practice package with **zero external dependencies**. There is no web server, database, Docker, or CI/CD.

### Running solutions

Activate the virtual environment then run any solution module:

```bash
source .venv/bin/activate
python -m data_structures.<topic>.<problem>
```

Example: `python -m data_structures.arrays.leetcode_1_two_sum`

### Testing

There is no pytest or unittest. Each solution file contains inline tests using the custom `run_test()` helper from `data_structures.utils.test_utils`. Running a module directly executes its tests and prints PASS/FAIL to stdout.

To run all solutions in a topic, iterate over the `.py` files in that subpackage (excluding `__init__.py`). Some solution files may print FAIL for unimplemented approaches — this is expected for a practice repo.

### Gotchas

- The `python3.12-venv` system package must be installed before creating the venv (`sudo apt-get install -y python3.12-venv`). The VM snapshot includes this.
- Some topic directories (e.g. `hashing/`, `queue/`, `graphs/`) only have `__init__.py` with no solutions yet.
- Some solution files have approaches marked as "not implemented" that will show FAIL — this is intentional.
