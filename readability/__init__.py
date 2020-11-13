import check50

@check50.check()
def exists():
    """readability.cpp exists"""
    check50.exists("readability.cpp")
    check50.include("input1.txt", "input2.txt")
    check50.include("expected_output1.txt", "expected_output2.txt")

@check50.check(exists)
def compiles():
    """readability.cpp compiles"""
    check50.run("g++ readability.cpp -lcrypt -lcs50 -lm -o readability").exit(0)

@check50.check(compiles)
def single_sentence_fileRead():
    """handles single sentence with multiple words"""
    check50.run("./readability").stdin("input1.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output1.txt").read())
    
@check50.check(compiles)
def single_sentence_other_punctuation_fileRead():
    """handles punctuation within a single sentence"""
    check50.run("./readability").stdin("input2.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output2.txt").read())
    
@check50.check(compiles)
def single_sentence_complex_fileRead():
    """handles more complex single sentence"""
    check50.run("./readability").stdin("input3.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output3.txt").read())

@check50.check(compiles)
def multiple_sentences_fileRead():
    """handles multiple sentences"""
    check50.run("./readability").stdin("input4.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output4.txt").read())

@check50.check(compiles)
def multiple_sentences_complex_fileRead():
    """handles multiple more complex sentences"""
    check50.run("./readability").stdin("input5.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output5.txt").read())

@check50.check(compiles)
def longer_passages_fileRead():
    """handles longer passages"""
    check50.run("./readability").stdin("input6.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output6.txt").read())

@check50.check(compiles)
def sentence_punctuation_fileRead():
    """handles multiple sentences with different punctuation"""
    check50.run("./readability").stdin("input7.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output7.txt").read())

@check50.check(compiles)
def sentence_punctuation_fileRead():
    """handles questions in passage"""
    check50.run("./readability").stdin("input8.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output8.txt").read())

@check50.check(compiles)
def before1_fileRead():
    """handles reading level before Grade 1"""
    check50.run("./readability").stdin("input9.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output9.txt").read())

@check50.check(compiles)
def grade16plus_fileRead():
    """handles reading level at Grade 16+"""
    check50.run("./readability").stdin("input10.txt").exit(0)
    check_output(open("output.txt").read(), open("expected_output10.txt").read())


def check_output(out, expected_out):
    if (out != expected_out):
        raise check50.Failure("Calculated result does not match with expected result\nOutput: " + out + "\nExpected output: " + expected_out)