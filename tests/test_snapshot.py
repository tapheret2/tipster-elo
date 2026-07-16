from tipster_elo import EloTable

def test_snapshot_is_copy():
    t = EloTable()
    t.update("A", True)
    s = t.snapshot()
    s["A"] = -1
    assert t.ratings["A"] != -1
