# cadCAD Hacks
The most comprehensive collection of intermediate level cadCAD methodologies on the web. If you're using cadCAD professionally, this is where you pick up the latest tips&amp;tricks.

See https://www.cadcad.education/course/cadcad-hacks

## Contents

* Season 1 notebooks: [`season-1/`](season-1/)

## Environment Setup

For a comprehensive setup tutorial using [Anaconda](https://anaconda.com) see [cadCAD Complete Foundations Bootcamp](https://www.cadcad.education/course/bootcamp) - Section 2: Environment Setup.

### 1. Get the Hacks

Clone or download the cadCAD Hacks GitHub repo:

**Clone**
```bash
git clone git@github.com:cadCAD-edu/cadCAD-Hacks.git
```

**Download**
https://github.com/cadCAD-edu/cadCAD-Hacks/archive/refs/heads/main.zip

### 2. Install Python Dependencies

Create a Python 3 virtual environment inside the Hacks folder:
```bash
cd ./cadCAD-Hacks/
python3 -m venv venv
```

Activate your virtual environment (operating system dependent, works on macOS/Unix OS):
```bash
source venv/bin/activate
```

Install the Python dependencies from [requirements.txt](requirements.txt) file:
```bash
python3 -m pip install requirements.txt
```

### 3. Start Jupyter Notebook

Start your Jupyter Notebook environment using the CLI:
```bash
jupyter notebook
```

Or start Jupyter Notebook using another method of your choice.

## Contributions

We gladly accept contributions of bug fixes!

1. Create an issue or a PR
2. Describe the issue or bug fix, including all relevant context
3. Add your name to the `CONTRIBUTORS.md` document along with relevant commits

## License

GNU General Public License v3.0 (GPL v3.0)

See [LICENSE](LICENSE)
