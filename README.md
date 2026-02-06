# Playwright Learning Playground

Personal playground-learning project focused on mastering Playwright. All tests are written against the [QA Practice Site](https://practice.qabrains.com/).

## Create and activate venv
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Running tests

```bash
pytest test_qabrains.py 
```

Run specific tags:
```bash
pytest -m login test_qabrains.py 
pytest -m "not login" test_qabrains.py 
```

## Reporting

### Save simple html report

```bash
pytest test_qabrains.py --html=report.html --self-contained-html
```

### Recording a trace (interactive report)

```bash
pytest test_qabrains.py --tracing on
cd test-results/<REPLACE_WITH_ACTUAL_FOLDER_NAME>
playwright show-trace trace.zip
```

**Note:** Replace `<REPLACE_WITH_ACTUAL_FOLDER_NAME>` with the actual folder name from `test-results/` directory. 
For example, if you see a folder named `test_login_button-1234567890`, use:
```bash
cd test-results/test_login_button-1234567890
playwright show-trace trace.zip
```
