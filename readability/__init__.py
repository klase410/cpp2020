import check50

@check50.check()
def exists():
    """readability.cpp exists"""
    check50.exists("readability.cpp")
    check50.include("input1.txt", "input2.txt")

@check50.check(exists)
def compiles():
    """readability.cpp compiles"""
    check50.run("g++ readability.cpp -lcrypt -lcs50 -lm -o readability").exit(0)
    
@check50.check(compiles)
def single_sentence_fileRead():
    """handles single sentence with multiple words"""
    check50.run("> output.txt").exit(0)
    check50.run("./readability").stdin("input1.txt").exit(0)
    with open("output.txt") as out
        rez = out.read()
        if (rez != "Grade 7\n"):
            raise check50.Failure("Expected result: Grade 7\n, not" + str(rez))
            
@check50.check(compiles)
def single_sentence_other_punctuation_fileRead():
    """handles punctuation within a single sentence"""
    check50.run("> output.txt").exit(0)
    check50.run("./readability").stdin("input2.txt").exit(0)
    with open("output.txt") as out
        rez = out.read()
        if (rez != "Grade 9\n"):
            raise check50.Failure("Expected result: Grade 9\n, not" + str(rez))