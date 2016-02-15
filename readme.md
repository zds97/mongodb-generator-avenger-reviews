A MongoDB data generator for mocked product reviews
===================================================

This simple script will generate mock product reviews for testing purposes.

Run the commands from the folder in which you cloned this repository run the following:

### Setup the environment and get prerequisites
```bash
$ virtualenv avenger-generator
$ source avenger-generator/bin/activate
$ pip install -r requirements.txt
```

### Run the generator

You can run the script with the preset Avengers list.

```bash
$ python generator.py
```

Or specify the product name to use.

```bash
$ python generator.py Mulder
```

### Stop the generator:

Press ctrl-c

### Deactivate the Python environment

```bash
$ deactivate
```