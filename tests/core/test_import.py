def test_import():
    import eth_typing

    assert isinstance(eth_typing.__version__, str)
