# Project structure

- Input:
	- train.csv
	- test.csv
- src:
	- create_folds.py
	- train.py
	- inference.py
	- models.py
	- config.py
	- model_dispatcher.py
- models:
	- model_rf.bin
	- model_et.bin
- notebooks:
	- exploration.ipynb
	- check_dat.ipynb
- README.md
- LICENCE

![[Images/AI_in_production/ML_project_structure.jpeg|400]]

# Structure explanation

## Input

This folder consists of all the input files and data for your machine learning project:
- NLP: embedding.
- CV: all images in a subfolder of this.

## src

All python scripts are kept here.

## models

This folder keeps all trained models

## notebooks

All jupyter notebooks are stored here

## README.md

This is a markdown file where you can describe your project and write instructions on how to train model or to serve this in a production environment

## LICENSE

Simple text file consists of a license for the project

#

---
Status: #done

Tags: #machine_learning #how_to #project #code_structure

References: [Arranging your machine learning project](https://twitter.com/abhi1thakur/status/1358481012410490881?s=19)

Related:
