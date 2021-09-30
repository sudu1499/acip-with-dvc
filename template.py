import os

dir=[
    os.path.join('data','preocessed'),
    os.path.join('data','raw'),
    'notebooks',
    'src',
    'saved_models'
]
files=[
    'params.yaml',
    'dvc.yaml',
    os.path.join('src','__init__.py'),
    '.gitignore'
]

for f in dir:
    os.makedirs(f,exist_ok=True)
    with open(os.path.join(f,'gitkeep'),'w') as g:
        pass
for f in files:
    with open(f,'w') as g:
        pass