def generate_hello_html(name):
    if name == "":
        name = "Github Actions"

    return f"<span>Hello {name}!</span>"
