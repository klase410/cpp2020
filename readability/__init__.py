import check50

@check50.check()
def exists():
    """readability.cpp exists"""
    check50.exists("readability.cpp")
    check50.include("input.txt")
    check50.include("expected_output1.txt", "expected_output2.txt", "expected_output3.txt", "expected_output4.txt", "expected_output5.txt", "expected_output6.txt", "expected_output7.txt", "expected_output8.txt", "expected_output9.txt", "expected_output10.txt")

@check50.check(exists)
def compiles():
    """readability.cpp compiles"""
    check50.run("g++ readability.cpp -lcrypt -lcs50 -lm -o readability").exit(0)

@check50.check(compiles)
def single_sentence_fileRead():
    """handles single sentence with multiple words"""
    generate_input("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output1.txt").read())
    
@check50.check(compiles)
def single_sentence_other_punctuation_fileRead():
    """handles punctuation within a single sentence"""
    generate_input("There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output2.txt").read())
    
@check50.check(compiles)
def single_sentence_complex_fileRead():
    """handles more complex single sentence"""
    generate_input("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \"and what is the use of a book,\" thought Alice \"without pictures or conversation?\"")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output3.txt").read())

@check50.check(compiles)
def multiple_sentences_fileRead():
    """handles multiple sentences"""
    generate_input("Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output4.txt").read())

@check50.check(compiles)
def multiple_sentences_complex_fileRead():
    """handles multiple more complex sentences"""
    generate_input("It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output5.txt").read())

@check50.check(compiles)
def longer_passages_fileRead():
    """handles longer passages"""
    generate_input("When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output6.txt").read())

@check50.check(compiles)
def sentence_punctuation_fileRead():
    """handles multiple sentences with different punctuation"""
    generate_input("Congratulations! Today is your day. You're off to Great Places! You're off and away!")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output7.txt").read())

@check50.check(compiles)
def sentence_punctuation_fileRead():
    """handles questions in passage"""
    generate_input("Would you like them here or there? I would not like them here or there. I would not like them anywhere.")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output8.txt").read())

@check50.check(compiles)
def before1_fileRead():
    """handles reading level before Grade 1"""
    generate_input("One fish. Two fish. Red fish. Blue fish.")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output9.txt").read())

@check50.check(compiles)
def grade16plus_fileRead():
    """handles reading level at Grade 16+"""
    generate_input("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.")
    check50.run("./readability").exit(0)
    check_output(open("output.txt").read(), open("expected_output10.txt").read())


def check_output(out, expected_out):
    if (out != expected_out):
        raise check50.Failure("Calculated result does not match with expected result\nOutput: " + out + "\nExpected output: " + expected_out)

        
def generate_input(input):
    open("input.txt", "w").write(input)