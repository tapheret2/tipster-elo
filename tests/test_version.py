def test_version_string():
    import tipster_elo as m
    assert hasattr(m, "__version__")
    assert isinstance(m.__version__, str)
    assert m.__version__
