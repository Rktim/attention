# attention/__init__.py

import webbrowser

# === Paper registry ===
# Add as many papers as you want here.
PAPERS = {
    "attention_is_all_you_need": {
        "title": "Attention Is All You Need",
        "year": 2017,
        "url": "https://arxiv.org/abs/1706.03762"
    },
    "bert": {
        "title": "BERT: Pre-training of Deep Bidirectional Transformers",
        "year": 2018,
        "url": "https://arxiv.org/abs/1810.04805"
    },
    "gpt_3": {
        "title": "GPT-3: Language Models are Few-Shot Learners",
        "year": 2020,
        "url": "https://arxiv.org/abs/2005.14165"
    },
    "model_context_protocol_mcp": {
        "title": "Model Context Protocol (MCP)",
        "year": 2024,
        "url": "https://en.wikipedia.org/wiki/Model_Context_Protocol"
    },
    # You can add many more here...
}

# === Utility functions ===

def list_papers():
    """List all registered papers."""
    print("\nAvailable Research Papers:\n")
    for key, info in sorted(PAPERS.items(), key=lambda x: x[1]["year"]):
        print(f"- {info['title']} ({info['year']})")
    print()

def open_paper(name: str):
    """
    Open a specific paper in the default browser.
    `name` can be partial/approximate and will match normalized keys.
    """
    name_norm = name.lower().replace(" ", "_")
    if name_norm in PAPERS:
        url = PAPERS[name_norm]["url"]
        print(f"Opening: {PAPERS[name_norm]['title']} → {url}")
        webbrowser.open(url)
    else:
        print(f"❌ Paper '{name}' not found. Try `attention list` to see all available.")
