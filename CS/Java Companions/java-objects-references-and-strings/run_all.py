"""Compile and run every starter program in this folder, and print exactly what happened.

Run:  python3 run_all.py            (needs a JDK: javac and java on the PATH)
Every output quoted in [[Java Objects, References and Strings]] was produced by this script.
Counter.java is a helper class that the other programs use.  BadCalls.java, SameSignature.java and StringLessThan.java are expected to be refused by the
compiler; NullDemo.java and OutOfRange.java are expected to stop with an exception.  Input.java is fed two lines, "Ada" and "17", and
YesBug.java is fed "yes", as if they had been typed.  javac is run with -g so that an exception message can name the variable involved.  Nothing is left behind."""
import subprocess, tempfile, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ORDER = ["Methods", "BadCalls", "SameSignature", "Create", "Alias", "NullDemo", "PassReference", "Strings", "Immutable", "StringEquals", "OutOfRange",
         "Compare", "StringLessThan", "Input", "YesBug", "Examples"]
STDIN = {"Input": "Ada\n17\n", "YesBug": "yes\n"}

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
            r = subprocess.run(["java", "-cp", tmp, name], input=STDIN.get(name, ""), capture_output=True, text=True)
            print(r.stdout.rstrip())
            if r.returncode != 0:
                print(f"[stopped with exit code {r.returncode}]")
                print(r.stderr.rstrip())

if __name__ == "__main__":
    main()
