## 2024-05-22 - [String Concatenation Bottleneck]
**Learning:** Python string concatenation in loops is O(N^2) and becomes a massive bottleneck when processing file contents.
**Action:** Always use `"".join()` for aggregating text content, as it reduces complexity to O(N).
## 2024-05-23 - Missing Test Suite
**Learning:** The project currently has no visible test suite (no `tests/` directory, no test runner in `pyproject.toml`).
**Action:** Always create a verification script for any changes to ensure correctness before submitting.
## 2024-05-24 - [File System Traversal Optimization]
**Learning:** `os.path.isdir()` and redundant path substring checks inside `os.walk` loops add significant overhead (~20-30%) in large directory trees.
**Action:** When using `os.walk`, rely on its structure (dirs vs files) and pruning to avoid redundant `stat` calls and path checks. Use O(1) sets for filename exclusions.
