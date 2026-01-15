## 2024-05-22 - [String Concatenation Bottleneck]
**Learning:** Python string concatenation in loops is O(N^2) and becomes a massive bottleneck when processing file contents.
**Action:** Always use `"".join()` for aggregating text content, as it reduces complexity to O(N).
