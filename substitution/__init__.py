import check50

@check50.check()
def exists():
    """substitution.cpp exists"""
    check50.exists("substitution.cpp")
    check50.include("input1.txt", "input2.txt")
    check50.include("expected_output1.txt", "expected_output2.txt")

@check50.check(exists)
def compiles():
    """substitution.cpp compiles"""
    check50.run("g++ substitution.cpp -lcrypt -lcs50 -lm -o substitution").exit(0)

@check50.check(compiles)
def encrypt1():
    """encrypts "A" as "Z" using ZYXWVUTSRQPONMLKJIHGFEDCBA as key"""
    check50.run("./substitution ZYXWVUTSRQPONMLKJIHGFEDCBA").stdin("input1.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output1.txt").read())

@check50.check(compiles)
def encrypt2():
    """encrypts "a" as "z" using ZYXWVUTSRQPONMLKJIHGFEDCBA as key"""
    check50.run("./substitution ZYXWVUTSRQPONMLKJIHGFEDCBA").stdin("input2.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output2.txt").read())


def check_output(out, expected_out):
    if (out != expected_out):
        raise check50.Failure("Calculated result does not match with expected result\nOutput: " + out + "\nExpected output: " + expected_out)
