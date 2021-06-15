setup:
	pip install -r requirements.txt
	python3 -m ipykernel install --user --name python-cadcad-hacks --display-name "Python (cadCAD Hacks)"
	jupyter labextension install jupyterlab-plotly@4.14.3

update-notebooks:
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --execute --to notebook --inplace **/*.ipynb

