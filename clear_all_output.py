import glob
from nbformat import read, write

for notebook in glob.glob('*.ipynb'):

    print("Clearing output from {0}".format(notebook))

    with open(notebook, 'r') as f:
        nb = read(f, 4)

    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell.execution_count = None
            cell.outputs = []
            if 'prompt_number' in cell:
                cell.pop('prompt_number')

    with open(notebook, 'w') as f:
        write(nb, f)