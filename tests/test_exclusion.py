import os
import unittest
from artificial_duck.cli import should_exclude_path

class TestExclusion(unittest.TestCase):
    def test_should_exclude_path(self):
        # Test default behavior
        self.assertTrue(should_exclude_path("package-lock.json"))
        self.assertTrue(should_exclude_path("/path/to/package-lock.json"))
        self.assertTrue(should_exclude_path("license.md"))

        # Test case insensitivity
        self.assertTrue(should_exclude_path("LICENSE.md"))

        # Test extension exclusion
        self.assertTrue(should_exclude_path("file.pyc"))
        self.assertTrue(should_exclude_path("file.lock"))

        # Test path substring exclusion
        self.assertTrue(should_exclude_path("/path/to/venv/file.py"))
        self.assertTrue(should_exclude_path("/path/to/__pycache__/file.pyc"))
        self.assertTrue(should_exclude_path("/path/to/node_modules/package.json"))

        # Test non-excluded files
        self.assertFalse(should_exclude_path("main.py"))
        self.assertFalse(should_exclude_path("/path/to/main.py"))
        self.assertFalse(should_exclude_path("README.md"))

    def test_should_exclude_path_with_basename(self):
        # Test optimization with basename provided
        self.assertTrue(should_exclude_path("/long/path/to/package-lock.json", basename="package-lock.json"))
        self.assertTrue(should_exclude_path("/path/to/file.pyc", basename="file.pyc"))
        self.assertFalse(should_exclude_path("/path/to/main.py", basename="main.py"))

if __name__ == '__main__':
    unittest.main()
