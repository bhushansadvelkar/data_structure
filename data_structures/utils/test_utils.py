"""
Shared test helpers for data_structures examples.
"""


def run_test(got, expected, name, normalize=None, compare=True, details=None):
    """
    Print PASS/FAIL for a test case.

    - If compare is False, prints PASS with optional details.
    - If normalize is provided, both got/expected are normalized before compare.
    - If got is None, treat as not implemented.
    """
    if not compare:
        extra = f" | {details}" if details else ""
        print(f"PASS: {name}{extra}")
        return

    if got is None:
        print(f"FAIL: {name} | solution returned None (not implemented)")
        return

    if normalize:
        got = normalize(got)
        expected = normalize(expected)

    status = "PASS" if got == expected else "FAIL"
    extra = f" | got {got}, expected {expected}" if status == "FAIL" else ""
    print(f"{status}: {name}{extra}")
