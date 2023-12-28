import sys
from lisp_lexer import lexer
from lisp_parser import parser

if __name__ == "__main__":
    test_file = sys.argv[1] if len(sys.argv) > 1 else './test.lsp'
    with open(f'{test_file}', 'r') as f:
        code = f.read()
        try:
            result = parser.parse(code)
        except Exception as e:
            result = [e]
        finally:
            with open(f'./test.out', 'w') as out:
                for result in result:
                    if not isinstance(result, str):
                        out.write(str(result))
                        out.write('\n')

