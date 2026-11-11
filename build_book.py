"""Build the handbook with XeLaTeX and the Unicode Chinese index processor."""
import shutil,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parent
compiler=shutil.which('latexmk')
assert compiler,'latexmk is required'
assert shutil.which('upmendex'),'upmendex is required for Chinese pinyin sorting'
index_style=(root/'index.ist').as_posix()
index_command=f'$makeindex = \'upmendex -s "{index_style}" %O -o %D %S\';'
command=[compiler,'-norc','-e',index_command,'-xelatex','-interaction=nonstopmode','-halt-on-error','-synctex=1',f'-outdir={root / "build"}',str(root/'main.tex')]
if '--force' in sys.argv:command.insert(2,'-g')
result=subprocess.run(command,cwd=root)
print(f'BOOK BUILD: exit {result.returncode}',flush=True)
sys.exit(result.returncode)
