import sys

import pytest

import book_app


def test_list_unread_command_displays_unread_books(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(sys, "argv", ["book_app.py", "list", "unread"])
    monkeypatch.setattr(
        book_app.collection,
        "get_unread_books",
        lambda: [],
    )

    book_app.main()

    assert "No books found." in capsys.readouterr().out


def test_help_lists_list_unread_command(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(sys, "argv", ["book_app.py", "help"])

    book_app.main()

    assert "list unread - Show unread books" in capsys.readouterr().out
