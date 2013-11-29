moveit_web
==========

Web-based tools using the MoveIt planning framework


Demo
----

### Installation

TBD

### Running

Start the MoveIt! backend and all dependencies:

    roslaunch moveit_web everything.launch

Start the django server

    cd src/moveit_web/django
    ./run.sh

Open a browser and point to the URDF viewer at
http://localhost:8080/static/urdf.html

Web-UI
------

To run the web UI alone (without connecting to a backend), you'll need to make sure the app is configured for debuggin. This involves editing the `webui/index.html`, where app initialization occurs:

```html
        <script>
        ...
        config.debug = true;
	    app.init(config);
        ...
        </script>
```

After this, navigate to the webui directory and run `python2 -m SimpleHTTPServer` for a fast and cheap file server. Navigating your WebGL enabled browser to `localhost:8000` will give you access to the web UI.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/etoccalino/moveit_web/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

