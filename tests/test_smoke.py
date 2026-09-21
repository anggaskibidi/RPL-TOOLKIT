def test_imports():
    import main
    from core.menu import run_menu

    assert callable(run_menu)
