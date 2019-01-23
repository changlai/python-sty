Python in Latex
===============

This package enables you to embed Python code (www.python.org) in LaTeX and insert the output into your LaTeX document.

Installing
----------

Copy `python.sty` side by side with your document.


Using
-----

In you LaTeX document insert::

    \usepackage{python}
    ...
    \begin{python}
    print("42")
    \end{python}

Compile the document with the shell escape option and of course Python installed::

    $ latex -shell-escape document.tex

or insert/change "shell_escape = t" in your texmf.cnf

**Note**: By default LaTeX and its variants disallowing calling of arbitrary shell commands. python.sty requires unrestricted
to the shell in order to execute embedded Python scripts. When running python.sty you must execute ``latex`` or ``pdftex`` with
either the ``-enable-write18`` or ``-shell-escape`` command line argument to enabled access to the Python executable.


Package options
---------------

The package takes an optional key-value option (`bin`) that can be used to specify the 
python binary to use. (If not present `python` is used)::
 
     \usepackage[bin=python2.6]{python}
     

Python scripts, output, error and return files are saved by default in the same folder as the documents and the folder gets crowded quite easily, If the word `subfolder` is 
added to the options, these files will be served to a subfolder named `py`::

     \usepackage[subfolder]{python}


If -output-directory option is used, it must also be indicated here using `outputdir` option.

     \usepackage[outputdir=build]{python}
     

Package content
---------------

Original discussion and examples at http://web.archive.org/web/20120423051102/http://pycurious.org/2011/12/the-ultimate-python-latex-environment/

example.tex
    Example usage of python.sty.

pytex.vim
    A Vim syntax highlighting file to correctly highlight python embedded in
    LaTeX documents.

python.sty
    A LaTeX package that allows direct embedding of python scripts in LaTeX
    documents.
    
