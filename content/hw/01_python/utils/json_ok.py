import json
from pathlib import Path

ROOT = Path("ok/answers")
ROOT.mkdir(parents=True, exist_ok=True)


def dump(varname, globals):
    obj = eval(varname, globals)
    fname = varname + ".json"
    with open(ROOT / fname, "w") as f:
        json.dump(obj, f)


def load(filename):
    fpath = ROOT / (filename + ".json")
    with open(fpath, "r") as f:
        obj = json.load(f)
    return obj
