Create environment
```bash
conda create -n wineq python=3.8 -y
```

Activate environment
```bash
conda activate wineq
```

Create requirements.txt

install the requirements
```bash
pip install -r requirements.txt
```

```bash
touch README.md
touch template.py
```

```bash
git init
```

```bash
dvc init
```
```bash
dvc add data_given/winequality.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

```bash
git add . && git commit -m "updated README.md" && git push -u origin main
```

```bash
git remote add origin https://github.com/kanva001/winequality.git
```

```bash
git branch -M main
```
```bash 
git pull https://github.com/kanva001/winequality main
```

```bash
git pull origin main --allow-unrelated-histories
```

```bash
git push -u origin main
```


tox command - 

```bash
tox
```

for rebuilding the env 
```bash
tox -r
```
```bash
pytest -v
```
```bash
pip install -e .
```

To build own pacjages, use the command

```bash
python setup.py sdist bdist_wheel
```
