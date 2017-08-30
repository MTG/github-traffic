from setuptools import setup

setup(
    name = "github-traffic",
    version = "0.1",
    author = "Music Technology Group, Universitat Pompeu Fabra",
    author_email = "alastair.porter@upf.edu",
    description = "A tool to get GitHub traffic stats for a repository",
    install_requires = ["python-dateutil", "requests"],
    license = "MIT",
    url = "https://github.com/MTG/github-traffic",
    packages = ["github_traffic"],
    data_files = [('github_traffic', ['github_traffic/config.ini'])],
    entry_points = {"console_scripts": ["github_get_traffic=github_traffic.get_traffic.main"]},
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
