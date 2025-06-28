### BANK QUERY APP RESTFUL API

## How to run

1.  fork code repo

2.  create and activate virtual environment
    ```
        python -m venv renv
    ```

    Windows:
    ```
        renv/scripts/activate
    ```
    linux:
    ```
        source renv/bin/activate
    ```
3. Install dependecies
    In same dir as reqs.txt, run
    ```
        pip install -r reqs.txt
    ```

4. Configure env
    Create a .env file in same directory as manage.py
    AH stands for Allowed Hosts
    CO stands for Cross Origin

    You can have more than one of each, seperate with a comma if you do.
    If you have only one, no need for a comma
    ```
        AH=allowedhostone,allowedhost2
        CO=https://crossoriginone,https://crossorigintwo
    ```

    Full example

    ```
        AH=192.168.0.3,127.0.0.1    # Do not append port
        CO=http://localhost:8081
    ```

5.  Run server against any of the hosts. This example uses 192.168.0.3

    ```
        python manage.py runserver 192.168.0.3:8000 # append port
    ```
