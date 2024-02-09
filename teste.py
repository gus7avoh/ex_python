import pydoc
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

while True:
    funcao = input('\033[1;34m Função (Fim): \033[m').strip().lower()
    if funcao == 'fim':
        break
    help_text = pydoc.render_doc(funcao)
    colored_help = highlight(help_text, PythonLexer(), TerminalFormatter())
    print(colored_help)
