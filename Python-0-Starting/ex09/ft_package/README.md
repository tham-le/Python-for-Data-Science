# Example Package

This is a simple example package with one function:

- ``count_in_list`` count the nunber of times an object appreas in a list of said objects

Make sure you have the latest version of PyPA’s build installed:
```python3 -m pip install --upgrade build```

run this command from the same directory where pyproject.toml is located:
```python3 -m build```

show package info
```pip show -v ft_package```

uninstall
```python -m pip uninstall ft_package```

The package will be installed via pip using one of the following commands (both should work):
• pip install ./dist/ft_package-0.0.1.tar.gz
• pip install ./dist/ft_package-0.0.1-py3-none-any.whl