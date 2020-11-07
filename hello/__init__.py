import check50

@check50.check()
def exists():
    """hello.cpp exists"""
    check50.exists("hello.cpp")

@check50.check(exists)
def compiles():
    """hello.cpp compiles"""
    check50.run("g++ hello.cpp -lcrypt -lcs50 -lm -o hello").exit(0)

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./hello").stdin("Emma").stdout("Emma").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./hello").stdin("Rodrigo").stdout("Rodrigo").exit()
