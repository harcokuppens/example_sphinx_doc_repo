# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Example sphinx doc repo'
copyright = '2020, Harco Kuppens'
author = 'Harco Kuppens'


# -- Automatically add tool version  -----------------------------------------


# This adds 'toolversion' as variable to sphinx documentation.
# Use in .rst file as |toolversion|
# eg. Documentation for TorXakis version: |toolversion|
with open('TOOLVERSION.txt') as f:
    toolversion = f.readline()

import os
pdfdocumenturl=os.environ['DOCUMENT_URL_PDF']
rst_epilog = '.. |toolversion| replace:: %s' % toolversion
rst_prolog = '.. |pdfdocumenturl| replace:: %s' % pdfdocumenturl
#doc_base_url="https://harcokuppens.github.io/example_sphinx_doc_repo/"
#pdf_url=doc_base_url + "stable/

#https://github.com/harcokuppens/example_sphinx_doc_repo/releases/download/v0.1.14/TorXakis-v4.3.14_Userguide-v0.1.14.pdf

# DOCUMENT_URL_PDF


# -- General configuration ---------------------------------------------------
import sphinx_rtd_theme

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme = "sphinx_rtd_theme"