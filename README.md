
Stoel
=====

Todo
----

 - authentication
 - apscheduler / celery

Calculation
-----------

    download = int(round(self.download / 1000.0, 0))
    ping = int(round(self.ping, 0))
    upload = int(round(self.upload / 1000.0, 0))

Startup
-------

To update the latest netspeed.

```bash
$ poetry run python stoel/main.py
```

To start the backend server.

```bash
$ poetry run uvicorn stoel.main:app --reload
```
