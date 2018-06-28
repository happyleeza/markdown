from markdown_adapter import run_markdown
ret = run_markdown('*this should be wrapped in em tags*')
print (type(ret), ret)