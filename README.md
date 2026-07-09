# tipster-elo

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
