rem chrome
pytest -v -s -m "Regression" --html=./Reports/report.html Testcases/ --browser chrome

rem edge

pytest -v -s -m "sanity" --html=./Reports/report.html Testcases/ --browser edge




