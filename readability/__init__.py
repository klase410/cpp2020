import check50

@check50.check()
def output_file_exists():
    """output.txt exists"""
    check50.exists("output.txt")

@check50.check(output_file_exists)
def exists():
    """readability.cpp exists"""
    check50.exists("readability.cpp")

@check50.check(exists)
def compiles():
    """readability.cpp compiles"""
    check50.run("g++ readability.cpp -lcrypt -lcs50 -lm -o readability").exit(0)

@check50.check(compiles)
def single_sentence_fileRead():
    """handles single sentence with multiple words"""
    check50.run("./readability").stdin("input1.txt").exit(0)
    check_output(open("output.txt"), open("expected_output1.txt"))
    
@check50.check(compiles)
def single_sentence_other_punctuation_fileRead():
    """handles punctuation within a single sentence"""
    check50.run("./readability").stdin("input2.txt").exit(0)
    check_output(open("output.txt"), open("expected_output2.txt"))
            
def check_output(out, expected_out):
    if (out.read() != expected_out.read()):
        raise check50.Failure("Calculated result result does not match with expected result" + out.read() + "Hello")