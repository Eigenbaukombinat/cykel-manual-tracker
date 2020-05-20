Small helper to set tracker positions in cykell. Usage:


.. code-block::

  git clone <path>
  cd <repo>
  cp config.py.example config.py
  # edit config.py to set endpoint url and api key
  python3 -m venv .
  bin/pip install -r requirements.txt
  FLASK_APP=tracker.py bin/flask run
  
Now access your browser on the displayed address (normally http://localhost:5000), enter a tracker name (which must of course exist in your cykell instance) and click on the map to set the new location. You can also change the battery voltage of the given tracker.
