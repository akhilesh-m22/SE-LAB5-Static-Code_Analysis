1. Which issues were the easiest to fix, and which were the hardest? Why?
Answer:
The easiest issues to fix were style and formatting errors such as missing docstrings, naming conventions, and long lines, since they only required minor text edits.
The hardest issues were related to security and logic — like replacing eval() and removing the global variable — because they required structural code changes and re-testing.

2. Did the static analysis tools report any false positives? If so, describe one example.
Answer:
Yes, one example was the warning about using lazy % formatting in logging. While the existing f-strings were functionally correct, Pylint flagged them for best practice rather than an actual error — making it more of a stylistic preference than a true bug.

3. How would you integrate static analysis tools into your actual software development workflow?
Answer:
I would integrate Pylint, Bandit, and Flake8 into a CI pipeline so that every commit triggers automated static analysis. Developers could also run these tools locally before pushing code to ensure consistent quality and early detection of issues.

4. What tangible improvements did you observe after applying the fixes?
Answer:
After applying the fixes, the code became more readable, secure, and maintainable. Logging and error handling improved visibility, security warnings were eliminated, and the overall Pylint score increased to 10/10 — reflecting higher code quality and robustness.