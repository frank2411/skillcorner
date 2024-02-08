# How to run the project

##  Install the package (inside or outside a venv, your choice)

### If you want to run the test suite
```
pip install -e ".[dev]"
```

**And then**

```
tox
```


### Or if you simply want to run the package
```
pip install .
```

**or**

```
pip install -e .
```

**And then run it with**
```
import-data data/data.log
```
