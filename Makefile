doc:
		$(MAKE) -C docs/ html
		# Uncomment open ... if you use Mac
		# open docs/_build/html/index.html
		xdg-open docs/_build/html/index.html

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log