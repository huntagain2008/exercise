import random

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

# create 35 quizFiles and answers
for quizNum in range(35):
    quizFile = open('quiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('answer%s.txt' % (quizNum + 1), 'w')

    # header
    quizFile.write('Date:\n\nName:\n\n')
    quizFile.write((' ' * 20) + 'State capital form%s\n\n' % (quizNum + 1))

    # randomize the order of the question and multiple choice options
    states = list(capitals)
    random.shuffle(states)

    for questionNum in range(50):
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
                                                             states[questionNum]))
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        answerOptions = [correctAnswer] + random.sample(wrongAnswers, 3)
        random.shuffle(answerOptions)

        for i in range(4):
            quizFile.write('%s. %s\n' % ('ABCD'[i], answerOptions[i]))

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index
                                                                  (correctAnswer)]))
            
    quizFile.close()
    answerKeyFile.close()
    
