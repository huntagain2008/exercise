"""Say you're a geography teacher with 35 students in your class and you want to give
a pop quiz on US state capitals. Alas, your class has a few bad eggs in it. and you
can't trust the students not to cheat. You'd like to randomize the order of questions
so that each quiz is unique, making it impossible for anyone to crib answers from 
anyone else. Of course, doing this by hand would be a lengthy and boring affair."""
# Create 35 different quizzes.
# Create 50 multiple-choice questions for each quiz, in random order.
# Provides the correct answer and three random wrong answers each question, in random order
# Writes the quizzes to 35 text files
# Writes the answer keys to 35 text files

#! python3
# Create quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data, Keys are states and values are their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
              'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
              'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
              'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
              'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
              'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
              'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
              'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
              'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
              'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
              'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
              'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
              'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
              'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
              'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    
    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each
    for questionNum in range(50):

        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # write the question and answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum +1,
                       states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')    

        # write the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1,
                                          'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()



