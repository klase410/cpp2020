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

@check50.check(compiles)
def encrypt3():
    """encrypts "ABC" as "NJQ" using NJQSUYBRXMOPFTHZVAWCGILKED as key"""
    check50.run("./substitution NJQSUYBRXMOPFTHZVAWCGILKED").stdin("input3.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output3.txt").read())

@check50.check(compiles)
def encrypt4():
    """encrypts "XyZ" as "KeD" using NJQSUYBRXMOPFTHZVAWCGILKED as key"""
    check50.run("./substitution NJQSUYBRXMOPFTHZVAWCGILKED").stdin("input4.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output4.txt").read())

@check50.check(compiles)
def encrypt5():
    """encrypts "This is CS50" as "Cbah ah KH50" using YUKFRNLBAVMWZTEOGXHCIPJSQD as key"""
    check50.run("./substitution YUKFRNLBAVMWZTEOGXHCIPJSQD").stdin("input5.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output5.txt").read())

@check50.check(compiles)
def encrypt6():
    """encrypts "This is CS50" as "Cbah ah KH50" using yukfrnlbavmwzteogxhcipjsqd as key"""
    check50.run("./substitution yukfrnlbavmwzteogxhcipjsqd").stdin("input6.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output6.txt").read())

@check50.check(compiles)
def encrypt7():
    """encrypts "This is CS50" as "Cbah ah KH50" using YUKFRNLBAVMWZteogxhcipjsqd as key"""
    check50.run("./substitution YUKFRNLBAVMWZteogxhcipjsqd").stdin("input7.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output7.txt").read())

@check50.check(compiles)
def encrypt8():
    """encrypts all alphabetic characters using DWUSXNPQKEGCZFJBTLYROHIAVM as key"""
    check50.run("./substitution DWUSXNPQKEGCZFJBTLYROHIAVM").stdin("input8.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output8.txt").read())

@check50.check(compiles)
def handles_no_argv():
    """handles lack of key"""
    check50.run("./substitution").exit(1)

@check50.check(compiles)
def handles_invalid_length():
    """handles invalid key length"""
    check50.run("./substitution QTXDGMKIPV").exit(1)

@check50.check(compiles)
def handles_invalid_key_chars():
    """handles invalid characters in key"""
    check50.run("./substitution ZWGKPMJRYISHFEXQON2DLUACVT").exit(1)

@check50.check(compiles)
def handles_duplicate_chars():
    """handles duplicate characters in key"""
    check50.run("./substitution YFDTSMPBVIEERGHWONUAKLQXCZ").exit(1)
    
@check50.check(compiles)
def handles_multiple_duplicate_chars():
    """handles multiple duplicate characters in key"""
    check50.run("./substitution BBCCEFGHIJKLMNOPQRSTUVWXYZ").exit(1)

def check_output(out, expected_out):
    if (out != expected_out):
        raise check50.Failure("Calculated result does not match with expected result\nOutput: " + out + "\nExpected output: " + expected_out)
