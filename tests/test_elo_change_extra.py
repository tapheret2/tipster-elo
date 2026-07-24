
from tipster_elo.elo import clamp_rating, elo_change

def test_elo_change_win():
    d = elo_change(1500, 1500, 1.0, k=32)
    assert abs(d - 16.0) < 1e-9

def test_clamp_rating():
    assert clamp_rating(50) == 100
    assert clamp_rating(4000) == 3000
