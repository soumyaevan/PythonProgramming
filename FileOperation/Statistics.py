'''
statistics Write a function called statistics, which takes in a file name and returns a dictionary with the number
of lines, words, and characters in the file. (Note: we've provided you with the first chapter of Alice's Adventures
in Wonderland to give you some sample text to work with. This is also the text used in the tests.)
'''

'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(inFile):
    with open(inFile) as file:
        data = file.read()
        lines = len(data.split("\n"))
        words = len(data.replace("\n", " ").split(" "))
        characters = len(data.replace("\n","").replace(" ",""))
        return {'lines': lines, 'words': words, 'characters': characters}