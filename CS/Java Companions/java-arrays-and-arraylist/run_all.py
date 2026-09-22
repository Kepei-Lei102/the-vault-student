"""Compile and run every starter program in this folder, and print exactly what happened.

Run:  python3 run_all.py            (needs a JDK: javac and java on the PATH; run from any folder)
Every output quoted in [[Java Arrays and ArrayList]] was produced by this script.
Tally.java is a helper class.  WrongType.java and NoImport.java are expected to be refused by the compiler; ArrayBasics,
ReadFile, ListBasics, ListTraversal and Grid are expected to end with an exception after printing their real output.
ReadFile.java reads marks.txt from this folder.  Nothing is left behind."""
import subprocess, tempfile, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ORDER = ["ArrayBasics", "Traversals", "ArrayAlgorithms", "ReadFile", "Wrappers", "ListBasics", "ListTraversal", "ListAlgorithms",
         "Grid", "SearchSort", "WrongType", "NoImport"]

def main():
    only = sys.argv[1:] or ORDER
    with tempfile.TemporaryDirectory() as tmp:
        for name in only:
            print(f"\n===== {name}.java =====")
            c = subprocess.run(["javac", "-g", "-d", tmp, "-sourcepath", str(HERE), str(HERE / f"{name}.java")], capture_output=True, text=True)
            if c.returncode != 0:
                print("javac refused it:")
                print(c.stderr.replace(str(HERE) + "/", "").rstrip())
                continue
            r = subprocess.run(["java", "-cp", tmp, name], capture_output=True, text=True, timeout=30, cwd=HERE)
            print(r.stdout.rstrip())
            if r.returncode != 0:
                print(f"[stopped with exit code {r.returncode}]")
                print("\n".join(l for l in r.stderr.rstrip().splitlines() if "java.base" not in l))

if __name__ == "__main__":
    main()
