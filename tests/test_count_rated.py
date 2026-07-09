from tipster_elo import EloTable

def test_count_rated():
    t = EloTable()
    assert t.count_rated() == 0
    t.update("A", True)
    assert t.count_rated() == 1
