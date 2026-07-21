from tipster_elo.elo import EloTable

def test_delta_and_reset():
    t = EloTable()
    t.update("alice", True)
    t.update("bob", False)
    assert t.delta("alice", "bob") > 0
    assert t.count_rated() == 2
    t.reset()
    assert t.count_rated() == 0
    assert t.snapshot() == {}
