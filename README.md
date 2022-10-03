# USA States Data
This repository is going to show dependencies between USA's economy (by state) and different variables - <b>in construction</b> 🔨

<br>

> By NorthBrains Analytics 🧠

<br>

## Used Packages 💡

```python
from enum import IntEnum
import pandas as pd
import requests as req
from IPython.display import display
from libraries.table_load import GetRegionalData
```
the last one is <b>builded by us</b> python's class which load chosen table name and line code from BEA's serveres for Regional frame.

<a herf="https://apps.bea.gov/API/signup/index.cfm">BEA's API info hub</a>

<br>

## Load BEA's line codes with simple python script, straight from your terminal ✌🏼
```bash
python3 BEALineCodePick.py
```
<br>

