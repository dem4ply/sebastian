modules = user

unit::
	@echo Running unit_test ....
	@coverage run --omit="fann/*,**/migrations/*,manage.py,**/test*" \
	 	manage.py test --testrunner runners.Unit_runner

report:
	@coverage report

report_html: test
	@coverage html -d .html_coverage
	@nohup firefox .html_coverage/index.html > /dev/null &

clean:
	@rm -r .coverage .html_coverage

pep8:
	@pep8 --statistics ${modules}

flakes:
	@pyflakes ${modules}
