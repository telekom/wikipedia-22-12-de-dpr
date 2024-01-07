src := .

format:
	black $(src) $(test-src)
	ruff $(src) --fix
	mdformat --number .
