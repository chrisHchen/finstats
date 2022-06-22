[![PyPI](https://img.shields.io/pypi/v/finstats?color=%234ec726&style=flat-square)](https://pypi.org/project/finstats/)


# Introduction 💪

Get your China A-share stock metrics **alpha, beta** with only one line of command 🚀 🚀 🚀.

## Installation 🔌
```
pip install finstats
```

# Usage 🏄

## args 🚩:

- -s:  specify the stock code
- -b:  specify the benchmark code, usually sh000001, sh000300
- -r:  risk free return. default 0
- -p:  period. periodicity of the 'returns' data:: y/q/m/w/d, default is d
- -l:  number of records to fetch, default is 252.
  


use **finstats --help** to see more details
## example 🌰:

```bash
finstats -s sh600519 -b sh000001 -l 500
```

or cross-calculate multiply codes and benchmarks

```bash
finstats -s sh600519 sh601318 sz300750 -b sh000001 sh000300
```

<img src="https://github.com/chrisHchen/finstats/blob/master/assets/finstats-001.png" width="440" height="142"/>

# Data Source 🔋：

finstats uses Sina HTTP API as its data source