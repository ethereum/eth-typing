def test_import_and_version():
    import eth_typing

    assert isinstance(eth_typing.__version__, str)
