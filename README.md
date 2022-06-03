This project is made for Ideco as a test task.
It is an asyncronous web service able to scan machines on 
the Internet. 

- To run application:
    - run python3 -m venv venv in project folder
    - run source venv/bin/activate
    - get dependencies with pip install -r requirements.txt
    - run server with python sswa/run_server.py

Tests are available with python3 -m unittest test.py

- To make rpm packages(automaticly generating spec files
in build/bdist.linux-x86_64/rpm/SPECS/):
   - Make sure you have rpm-build installed
   - run python3 setup.py bdist_rpm
