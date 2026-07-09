from tipster_elo import EloTable

def test_reset_clears_table():
    t = EloTable()
    t.update("A", True)
    t.reset()
    assert t.ratings == {}
    assert t.games == {}
