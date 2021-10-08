# Neural Nets

This code goes together with the corresponding [video talk](https://www.youtube.com/watch?v=-BLI42zJhRc).


The easiest way to run this code is to start Jupyter Notebook using [docker](https://www.docker.com/products/docker-desktop) from the current directory:

```bash
docker run -v `pwd`:/home/jovyan/work  -it --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes --user root jupyter/datascience-notebook
```

Upon startup this will print out a URL such as:
```
http://127.0.0.1:8888/lab?token=7a259fb1721c9a0810f50da9bb308608725b41d8155645a6
```

Navigate to the printed URL and open the notebook from within the web application.

Cheers!
