"""Compile and run every starter program in this folder, and print exactly what happened.

Run:  python3 run_all.py            (needs a JDK: javac and java on the PATH)
Every output quoted in [[Java Control Flow]] was produced by this script.
NotBoolean.java and ScopeError.java are expected to be refused by the compiler; GuardSecond.java and StringOffByOne.java are expected
to stop with an exception.  WhileLoops.java is fed the lines 72, 45, 91, 50, 38, -1 as if they had been typed.  Nothing is left behind."""
import subprocess, tempfile, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ORDER = ["Misleading", "Semicolon", "NotBoolean", "AssignTrap", "Branches", "DanglingElse", "ShortCircuit", "GuardSecond", "DeMorgan",
         "WhileLoops", "NeverEqual", "ForLoops", "ScopeError", "StringLoops", "StringOffByOne", "Nested"]
STDIN = {"WhileLoops": "72\n45\n91\n50\n38\n-1\n"}

def main():
    only = sys.argv[1:] or ORDER
    with tempfile.TemporaryDirectory() as tmp:
        for name in only:
            print(f"\n===== {name}.java =====")
            c = subprocess.run(["javac", "-g", "-d", tmp, str(HERE / f"{name}.java")], capture_output=True, text=True)
            if c.returncode != 0:
                print("javac refused it:")
                print(c.stderr.replace(str(HERE) + "/", "").rstrip())
                continue
            r = subprocess.run(["java", "-cp", tmp, name], input=STDIN.get(name, ""), capture_output=True, text=True, timeout=30)
            print(r.stdout.rstrip())
            if r.returncode != 0:
                print(f"[stopped with exit code {r.returncode}]")
                print("\n".join(l for l in r.stderr.rstrip().splitlines() if "jdk.internal" not in l))

if __name__ == "__main__":
    main()
