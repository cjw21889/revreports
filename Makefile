# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* revreports/*.py

black:
	@black scripts/* revreports/*.py

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit=$(VIRTUAL_ENV)/lib/python*

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr revreports-*.dist-info
	@rm -fr revreports.egg-info

install:
	@pip install . -U

all: clean install test black check_code


uninstal:
	@python setup.py install --record files.txt
	@cat files.txt | xargs rm -rf
	@rm -f files.txt

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u lologibus2

pypi:
	@twine upload dist/* -u lologibus2

# ----------------------------------
#      GCP Commands
# ----------------------------------
LOCAL_PATH = nov22.csv
BUCKET_NAME = revreports
BUCKET_FOLDER = actuals_20
PROJECT_ID = revreports
TOTAL_ACCTUALS = actuals_2020.csv
CURRENT_ACCTUALS = actuals_2020.csv

upload_data:
	# -@gsutil cp train_1k.csv gs://wagon-ml-my-bucket-name/data/train_1k.csv
	-@gsutil cp ${LOCAL_PATH} gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${UPLOADED_FILE_NAME}

merge_actuals:
	-@gsutil compose gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${TOTAL_ACCTUALS} gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${LOCAL_PATH} gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${TOTAL_ACCTUALS}
	@echo gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${TOTAL_ACCTUALS}
	@echo gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${LOCAL_PATH}


