from app import get_random_quote, get_all_quotes, generate_html


def test_get_random_quote_returns_dict():
    quote = get_random_quote()
    assert isinstance(quote, dict)


def test_quote_has_required_keys():
    quote = get_random_quote()
    assert "text" in quote
    assert "author" in quote


def test_quote_text_is_non_empty_string():
    quote = get_random_quote()
    assert isinstance(quote["text"], str)
    assert len(quote["text"]) > 0


def test_quote_author_is_non_empty_string():
    quote = get_random_quote()
    assert isinstance(quote["author"], str)
    assert len(quote["author"]) > 0


def test_get_all_quotes_returns_list():
    quotes = get_all_quotes()
    assert isinstance(quotes, list)


def test_all_quotes_have_text_and_author():
    quotes = get_all_quotes()
    for q in quotes:
        assert "text" in q
        assert "author" in q


def test_quote_pool_has_minimum_size():
    quotes = get_all_quotes()
    assert len(quotes) >= 5


def test_generate_html_contains_quote_text():
    quote = {"text": "Test quote here.", "author": "Test Author"}
    html = generate_html(quote)
    assert "Test quote here." in html


def test_generate_html_contains_author():
    quote = {"text": "Test quote here.", "author": "Test Author"}
    html = generate_html(quote)
    assert "Test Author" in html


def test_generate_html_is_valid_html_string():
    quote = get_random_quote()
    html = generate_html(quote)
    assert html.startswith("<!DOCTYPE html>")
    assert "<html" in html
    assert "</html>" in html