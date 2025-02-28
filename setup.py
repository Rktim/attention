from setuptools import setup, find_packages

setup(
    name="attention_paper",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "attention=attention_paper.open_paper:open_attention_paper",
        ],
    },
    package_data={
        "attention_paper": ["data/attention_is_all_you_need.pdf"],
    },
)
