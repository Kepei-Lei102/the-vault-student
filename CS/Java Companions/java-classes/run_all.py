"""Compile and run every starter program in this folder, and print exactly what happened.

Run:  python3 run_all.py            (needs a JDK: javac and java on the PATH)
Every output quoted in [[Java Classes]] was produced by this script.
BankAccount.java is the class the card writes; UseAccount.java drives it.  Private.java, NoDefault.java, OutOfScope.java, MissingReturn.java
and StaticRules.java are expected to be refused by the compiler.  Nothing is left behind."""
import subprocess, tempfile, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ORDER = ["UseAccount", "Private", "Defaults", "NoDefault", "Shadow", "Scope", "OutOfScope", "Return", "MissingReturn", "CopyOrShare", "StaticRules", "Counter"]

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
            r = subprocess.run(["java", "-cp", tmp, name], capture_output=True, text=True, timeout=30)
            print(r.stdout.rstrip())
            if r.returncode != 0:
                print(f"[stopped with exit code {r.returncode}]")
                print(r.stderr.rstrip())

if __name__ == "__main__":
    main()
