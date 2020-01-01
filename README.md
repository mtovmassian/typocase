# Typocase

![](static/printer.png)

___

Lightweight library written in idiomatic Python (no regular expressions), that aims to translate string into various typography conventions.

## How it works

- Accept any string as input.
- Detect substrings based on special chars or uppercase letters as separators.
- Join substrings based on the typography convention selected:
  - snake case
  - pascal case
  - camel case
  - kebab case
  - dot case
  - path case
  - ...

## Install



## Usage

```python
>>> from typocase import TypoCase

>>> TypoCase("abc def ghi").snake_case()
'abc_def_ghi'

>>> TypoCase("abc def ghi").camel_case()
'abcDefGhi'

>>> TypoCase("abc def ghi").kebab_case()
'abc-def-ghi'
```

## License
This software is released under the MIT LICENSE.

## Author
Martin Tovmassian