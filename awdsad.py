import os.path as op
CWD = op.dirname(__file__)
with open(op.join(CWD, "output", "matched.txt"), "r") as f:
    for line in f:
        _split = line.strip().split()
        try:
            print(_split[1])
        except IndexError:
            continue
        if _split[0].startswith("sub_") and not _split[1].startswith("sub_"):
            print(f"Renamed")