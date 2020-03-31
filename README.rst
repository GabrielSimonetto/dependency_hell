This is a demo repo to ilustrate dependency hell and try and solve it

To see what I mean:

0- If you don't already have poetry:

``
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
echo 'export PATH=$PATH:$HOME/.poetry/bin' >> ~/.bashrc
source ~/.bashrc
``

1- Run `poetry install`

2- On branch master, run `poetry run python dependency_hell/my_dir/demo1.py`, it should work just fine

3- Move to the `wanted_changes` branch, run `poetry run python dependency_hell/demo2.py`, notice I changed `dependency_hell/my_dir/__init__.py` to suit my demonstration, and created a cyclic dependency on the process
