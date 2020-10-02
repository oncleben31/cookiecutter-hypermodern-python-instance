"""Sphinx configuration."""
from datetime import datetime


project = "Cookiecutter Hypermodern Python Instance"
author = "Oncleben31"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
autodoc_typehints = "description"
