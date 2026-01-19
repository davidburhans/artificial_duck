## 2024-05-22 - [String Concatenation Bottleneck]
**Learning:** Python string concatenation in loops is O(N^2) and becomes a massive bottleneck when processing file contents.
**Action:** Always use `"".join()` for aggregating text content, as it reduces complexity to O(N).
## 2024-05-23 - Missing Test Suite
**Learning:** The project currently has no visible test suite (no `tests/` directory, no test runner in `pyproject.toml`).
**Action:** Always create a verification script for any changes to ensure correctness before submitting.
## 2024-05-24 - [os.path.isdir in os.walk]
**Learning:** `os.walk` separates files and directories. Checking `os.path.isdir` on items from the `files` list is a redundant syscall (stat) that significantly slows down traversal.
**Action:** Trust `os.walk` classification and avoid `os.path.isdir` inside file loops.
