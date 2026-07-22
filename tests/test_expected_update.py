from tipster_elo.elo import expected_score, update_rating

def test_expected_equal():
    assert abs(expected_score(1500, 1500) - 0.5) < 1e-12

def test_update():
    r = update_rating(1500, 0.5, 1.0, k=20)
    assert abs(r - 1510) < 1e-9
