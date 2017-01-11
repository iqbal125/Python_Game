#Python Quiz
import sys

#Easy Questions
easy_quiz = """To print the number 7 you will type print _1_.
    To print the word hello you will type _2_ hello.
    Control flow uses an _3_ statement.
    A collection of elements is a _4_"""

#Easy answers
easy_answers = ["7", "print", "if", "list"]

#Medium Questions
medium_quiz = """A true or false statement will print _1_.
                A true and false statement will print _2_.
                To print the length of a list you use the _3_ function.
                A function starts with the word _4_."""

#Medium answers
medium_answers = ["true", "false", "len", "def"]

#Hard Questions
hard_quiz = """To iterate over a list you use a _1_ loop.
                True and false statements are known as _2_.
                The dominant paradigm programmers use is _3_ oriented programming.
                The _4_ statement executes a code as long as a certain condition is true."""

#Hard Answers
hard_answers = ["for", "booleans", "object", "while"]

#Blanks
blanks = ["_1_", "_2_", "_3_", "_4_"]


#Opening Message
print "Hello and welcome to the python quiz. All questions will be fill in the blank."

#Quiz Engine
def play_game(quiz, answers, blanks):
    #To keep track of which question user is on
    index = 0
    #To make sure the app doesnt run past the total number of questions
    Total_Questions = 4
    #To print quiz without answers
    print quiz
    while True:
        #Prints out question and question number
        user_answer = raw_input("Please type in answer for " + blanks[index])
        if user_answer == answers[index]:
            print "That is correct!"
            #To print out the correct answer in the blank space
            quiz = quiz.replace(blanks[index], user_answer)
            print quiz
            #To keep track of the question
            index += 1
            #Exit Condition
            if index == Total_Questions:
                print "Congrats you completed the quiz"
                sys.exit(0)
        #Unlimited attempts
        else:
            print "Sorry that is incorrect, please try again."

#Difficulty Selector
def UserSelection():
    user_input = raw_input("Please select difficulty of quiz, easy | medium | hard: ")
    if user_input == "easy":
        play_game(easy_quiz, easy_answers, blanks)
    elif user_input == "medium":
        play_game(medium_quiz,medium_answers,blanks)
    elif user_input == "hard":
        play_game(hard_quiz, hard_answers, blanks)
    else:
        print ("I don't understand, Please select difficulty")

print UserSelection()
