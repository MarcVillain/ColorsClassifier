ColorsClassifier
===

Simple script that lets you order images based on color.

# Install (Manual)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install .
```

# Install (MacOS)

The easy route would be to use the manual install. Otherwise, find someone who can create the app for you.

First, build the app:
```
make build_osx
```

Then, share the generated `.app` in the `dist/` folder by any mean you want.

> :warning: The .app file must be placed in the `Applications` folder before doing the last step.

Finally, have the user run the following command. (replace `PATH_TO_APP` with the full path to the `.app` file. This can be found with `Right-Click > Get Info > Where`.)
```
/PATH_TO_APP/Contents/MacOS/ColorsClassifier
```

This script can take a little while to start as its downloading the necessary tools to run this script in a python virtualenv.

# Run

Make sure you have activated your venv first.

```bash
colorsclassifier --help
```

# Authors

* Marc Villain <marc.villain@epita.fr>
