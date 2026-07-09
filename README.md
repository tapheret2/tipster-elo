# tipster-elo

![status](https://img.shields.io/badge/status-active-brightgreen) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)

Simple **Elo rating** for tipsters: each settled tip is a game vs a baseline market opponent.

Pairs with `keo-ledger` CSV exports.

## Install

```bash
pip install -e ".[dev]"
```

## CLI

```bash
# CSV columns: tipster,result  (result = W or L)
tipster-elo rate --csv samples/tips.csv
tipster-elo rate --csv samples/tips.csv --k 24 --json
```
