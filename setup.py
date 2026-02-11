# from setuptools import setup, find_packages

# setup(
#     name="attention_paper",
#     version="0.1",
#     packages=find_packages(),
#     include_package_data=True,
#     install_requires=[],
#     entry_points={
#         "console_scripts": [
#             "attention=attention_paper.open_paper:open_attention_paper",
#         ],
#     },
#     package_data={
#         "attention_paper": ["data/attentionalluneed.pdf"],
#     },
# )
# setup.py

from setuptools import setup, find_packages

setup(
    name="attention",
    version="0.3.0",
    packages=find_packages(),
    description="CLI to list and open high-impact AI research papers (Transformers, LLMs, MCP, etc.)",
    long_description="attention is a research paper loader for Transformer and post-Attention-Is-All-You-Need era AI research.",
    author="Raktim Kalita",
    py_modules=["main"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "attention=main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
