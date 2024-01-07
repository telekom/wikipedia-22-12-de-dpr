src := .

format:
	black $(src) $(test-src)
	mdformat --number .
