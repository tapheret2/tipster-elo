from tipster_elo import EloTable, rate_sequence


def test_win_raises_rating():
    t = EloTable()
    before = t.get("A")
    after = t.update("A", True)
    assert after > before


def test_loss_lowers():
    t = EloTable()
    before = t.get("A")
    after = t.update("A", False)
    assert after < before


def test_sequence_leaderboard():
    table = rate_sequence([("A", True), ("A", True), ("B", False), ("B", False)])
    board = table.leaderboard()
    assert board[0][0] == "A"
