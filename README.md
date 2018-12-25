# DiprellaTest1
Testing Framework for studying purposes
Steps to setup a project:
- Create new project in Pycharm from the files in "page_objects" and "test" folders with setup file;
- Run setup file to install the required packages for the project;
- Download chromedriver and geckodriver for tests run;
- Make sure you've added executable webdriver path to eviromental variables on your PC; 
- Run tests using the following command in Pycharm terminal (Windows OS): 
pytest -v test/test_pages.py --log-level=INFO --alluredir=(indicate your path to allure reports) --google-chrome --webdriver-location=(indicate your path to webdriver location on your PC)
- Analyze test results in allure reports; 
