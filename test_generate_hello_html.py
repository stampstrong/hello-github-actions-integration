from generate_hello_html import generate_hello_html


def test_hello_gihub_actions():
    assert generate_hello_html("") == "<span>Hello Github Actions!</span>"

def test_hello_someone():
    assert generate_hello_html("Athibet") == "<span>Hello Athibet!</span>"
