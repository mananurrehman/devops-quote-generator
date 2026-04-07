import random

QUOTES = [
    {"text": "Move fast and automate things.", "author": "DevOps Philosophy"},
    {"text": "Infrastructure as code means your data center is a bug tracker away from perfection.", "author": "Kief Morris"},
    {"text": "You build it, you run it.", "author": "Werner Vogels, AWS"},
    {"text": "The goal of DevOps is not to eliminate ops. It is to give developers more responsibility for their code in production.", "author": "Patrick Debois"},
    {"text": "Continuous delivery is the ability to get changes of all types into production safely and quickly in a sustainable way.", "author": "Jez Humble"},
    {"text": "Automate everything that can be automated.", "author": "Site Reliability Engineering"},
    {"text": "Shipping is a feature. A really important feature.", "author": "Joel Spolsky"},
    {"text": "If it hurts, do it more frequently, and bring the pain forward.", "author": "Jez Humble"},
    {"text": "DevOps is not a tool. It is a cultural movement.", "author": "Gene Kim"},
    {"text": "The best monitoring is the kind that wakes someone else up at 3 AM.", "author": "Unknown SRE"},
]


def get_random_quote():
    return random.choice(QUOTES)


def get_all_quotes():
    return QUOTES


def generate_html(quote):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Quote Generator</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }}
        .card {{
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 3rem;
            max-width: 700px;
            text-align: center;
            backdrop-filter: blur(10px);
        }}
        .tag {{
            background: #00d4aa;
            color: #0f2027;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 2px;
            padding: 4px 14px;
            border-radius: 50px;
            display: inline-block;
            margin-bottom: 2rem;
            text-transform: uppercase;
        }}
        blockquote {{
            font-size: 1.5rem;
            color: #ffffff;
            line-height: 1.7;
            margin-bottom: 1.5rem;
            font-style: italic;
        }}
        cite {{
            color: #00d4aa;
            font-size: 0.95rem;
            font-style: normal;
        }}
        .footer {{
            margin-top: 2.5rem;
            font-size: 0.75rem;
            color: rgba(255,255,255,0.3);
        }}
    </style>
</head>
<body>
    <div class="card">
        <span class="tag">DevOps Wisdom</span>
        <blockquote>"{quote['text']}"</blockquote>
        <cite>— {quote['author']}</cite>
        <p class="footer">Built with Python + GitHub Actions · Deployed via CI/CD</p>
    </div>
</body>
</html>"""


if __name__ == "__main__":
    quote = get_random_quote()
    html = generate_html(quote)
    with open("index.html", "w") as f:
        f.write(html)
    print(f"Generated quote: {quote['text']}")
    print("index.html written successfully.")