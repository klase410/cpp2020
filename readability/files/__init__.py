import check50

@check50.check()
def exists():
    """readability.cpp exists"""
    check50.exists("readability.cpp")
    check50.include("input.txt")
    check50.include("expected_output.txt")

@check50.check(exists)
def input_test():
	"""Contents of input.txt are valid"""
    with open('input.txt').read() as f:
        if not (f = "In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.")
            raise check50.Failure("Contents of input.txt file are not valid\nExpected input: In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.")

@check50.check(exists)
def compiles():
    """readability.cpp compiles"""
    check50.run("g++ readability.cpp -lcrypt -lcs50 -lm -o readability").exit(0)

@check50.check(compiles)
def single_sentence_fileRead():
    """handles single sentence with multiple words"""
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output.txt").read())


def check_output(out, expected_out):
    if (out != expected_out):
        raise check50.Failure("Calculated result does not match with expected result\nOutput: " + out + "\nExpected output: " + expected_out)