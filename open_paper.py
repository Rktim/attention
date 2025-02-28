import pkg_resources
import webbrowser
import os

def open_attention_paper():
    """Opens the Attention Is All You Need paper in the browser."""
    paper_path = pkg_resources.resource_filename("attention_paper", "C:/Users/raktm/rk/attentionalluneed.pdf")

    if os.path.exists(paper_path):
        webbrowser.open(f"file://{paper_path}")
    else:
        print("Error: Paper not found. Please reinstall the package.")
