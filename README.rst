**Note**: By default LaTeX and its variants disallowing calling of arbitrary shell commands. python.sty requires unrestricted
to the shell in order to execute embedded Python scripts. When running python.sty you must execute ``latex`` or ``pdftex`` with
either the ``-enable-write18`` or ``-shell-escape`` command line argument to enabled access to the Python executable.

python.sty and associated scripts
=================================

Discussion and examples at http://pycurious.org/2011/12/the-ultimate-python-latex-environment/

example.tex
    Example usage of python.sty.

pytex.vim
    A Vim syntax highlighting file to correctly highlight python embedded in
    LaTeX documents.

python.sty
    A LaTeX package that allows direct embedding of python scripts in LaTeX
    documents.
