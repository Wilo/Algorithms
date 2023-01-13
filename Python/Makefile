test:
	pytest --full-trace --no-header -vv

coverage cov cover:
	pytest --cov-config=.coveragerc --cov-report term --cov=. tests/

report:
	pytest --cov-config=.coveragerc --cov-report html:cov_html --cov=. tests/

profile:
	pytest --full-trace --no-header -vv --profile-svg