"""Compile and run every starter program in this folder, and print exactly what happened.

Run:  python3 run_all.py            (needs a JDK: javac and java on the PATH)
Every output quoted in [[Java Values and Expressions]] was produced by this script.
SyntaxError.java, WontCompile.java and Uninitialised.java are expected to be refused by the compiler; DivideByZero.java and Documented.java
are expected to stop with an exception.  Nothing is left behind: classes go to a temporary folder."""
import subprocess, tempfile, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ORDER = ["Output", "Variables", "IntDivision", "Casting", "Overflow", "CompoundAssign", "MathDemo",
         "Documented", "SyntaxError", "WontCompile", "Uninitialised", "DivideByZero", "LogicError"]

def main():
    only = sys.argv[1:] or ORDER
    with tempfile.TemporaryDirectory() as tmp:
        for name in only:
            src = HERE / f"{name}.java"
            print(f"\n===== {name}.java =====")
            c = subprocess.run(["javac", "-d", tmp, str(src)], capture_output=True, text=True)
            if c.returncode != 0:
                print("javac refused it:")
                print(c.stderr.replace(str(HERE) + "/", "").rstrip())
                continue
            r = subprocess.run(["java", "-cp", tmp, name], capture_output=True, text=True)
            print(r.stdout.rstrip())
            if r.returncode != 0:
                print(f"[stopped with exit code {r.returncode}]")
                print(r.stderr.rstrip())

if __name__ == "__main__":
    main()
