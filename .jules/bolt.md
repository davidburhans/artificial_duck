## 2024-05-22 - [String Concatenation Bottleneck]
**Learning:** Python string concatenation in loops is O(N^2) and becomes a massive bottleneck when processing file contents.
**Action:** Always use `"".join()` for aggregating text content, as it reduces complexity to O(N).
## 2024-05-23 - Missing Test Suite
**Learning:** The project currently has no visible test suite (no `tests/` directory, no test runner in `pyproject.toml`).
**Action:** Always create a verification script for any changes to ensure correctness before submitting.
