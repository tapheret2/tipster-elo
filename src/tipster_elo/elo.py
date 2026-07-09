from __future__ import annotations

from dataclasses import dataclass, field


def expected_score(rating: float, opp: float) -> float:
    return 1.0 / (1.0 + 10 ** ((opp - rating) / 400.0))


@dataclass
class EloTable:
    base: float = 1500.0
    k: float = 20.0
    market_rating: float = 1500.0
    ratings: dict[str, float] = field(default_factory=dict)
    games: dict[str, int] = field(default_factory=dict)

    def get(self, name: str) -> float:
        return self.ratings.get(name, self.base)

    def update(self, tipster: str, won: bool) -> float:
        r = self.get(tipster)
        exp = expected_score(r, self.market_rating)
        score = 1.0 if won else 0.0
        r2 = r + self.k * (score - exp)
        self.ratings[tipster] = r2
        self.games[tipster] = self.games.get(tipster, 0) + 1
        return r2

    def reset(self) -> None:
    """Clear all ratings and game counts."""
    self.ratings.clear()
    self.games.clear()

def leaderboard(self) -> list[tuple[str, float, int]]:
        rows = [(n, self.ratings[n], self.games.get(n, 0)) for n in self.ratings]
        rows.sort(key=lambda x: x[1], reverse=True)
        return rows


def rate_sequence(results: list[tuple[str, bool]], k: float = 20.0, base: float = 1500.0) -> EloTable:
    table = EloTable(base=base, k=k)
    for name, won in results:
        table.update(name, won)
    return table
