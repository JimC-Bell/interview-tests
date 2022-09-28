Setup
=====
- Abbility to unzip files
- Text editor or IDE of your choice. VSCode is recomended
- Install python 3.6 or greater
- Install pip


Task
=====
Complete main.py code as per in-line comments. This is a RESTful Web API using FastAPI that gets, updates and adds users to a small data table.
- The code should raise HTTP exceptions when required for invalid input data.
- You may import any libraries you require. Modify requierments.txt apropriatly.
- You may add, modify and delete any functions or classes in main.py as required.
- The code must not leave any artifacts behind but may use whatever temporary artifacts you deem nessiary as long as they are cleaned up.
- Do not alter data.json, you do not need to save any changes to the user data.
- Do not alter test.py or README.md.
- No logging is required but you may use logging functions for debugging but you MUST use the python logging modules to console for such.
- Any confuguation nessiary may be hardcoded such as file names.


Evaluation
=====
Submit main.py and requierments.txt to your Interview Contact. The following comands will be run, in order.

- `pip install -r requierments.txt`
  - Expected Result: All needed packages will be installed.

- `pytest -v test.py`
  - Expected Result: All tests pass.

- `pylama -v`
  - Expected Result: No formating errors are identified.

- `uvicron main:app`
  - Expected Result: Application loads and runs.

- `curl -X 'GET' 'http://127.0.0.1:8000/user' -H 'accept: application/json'`
  - Expected Output: `[{"name":"Joe","email":"joe@something.com","phone":"123 456-1234"},{"name":"Jane","email":"jane@nowhere.com","phone":"987 456-9876"}]`

- `curl -X 'PUT' 'http://127.0.0.1:8000/user/0' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name":"MyTest","email":"something@foo.bar","phone":"333 333-3333"}'`
  - Expected Output: `[{"name":"MyTest","email":"something@foo.bar","phone":"333 333-3333"},{"name":"Jane","email":"jane@nowhere.com","phone":"987 456-9876"}]`

- `curl -X 'POST' 'http://127.0.0.1:8000/user/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name":"MyTest2","email":"somethingelse@foo.bar","phone": "666 666-6666"}'`
  - Expected Output: `[{"name":"MyTest","email":"something@foo.bar","phone":"333 333-3333"},{"name":"Jane","email":"jane@nowhere.com","phone":"987 456-9876"},{"name":"MyTest2","email":"somethingelse@foo.bar","phone":"666 666-6666"}]`


Bonus
=====
- Add data validation to ensure email and phone numbers are valid.
- Add a delete endpoint.
- Add appropriate logging to console using relevant logging channels with clear and usefull messages that are searchable and apropriate for analytics.
