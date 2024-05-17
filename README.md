1. Create environment

"""bash
conda create -n wineq python=3.8 -y
"""

2. Activate environment
'''bash
conda activate wineq
'''

3. Create requirements.txt

4. install the requirements
"""bash
pip install -r requirements.txt
"""

5. """bash
touch README.md
touch template.py
"""

git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m "first commit"

git add . && git commit -m "updated README.md"

git remote add origin https://github.com/kanva001/winequality.git

git branch -M main
 
git pull https://github.com/kanva001/winequality main

git pull origin main --allow-unrelated-histories

'''bash
git push -u origin main
'''bash 



