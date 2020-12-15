#Print statement to introduce the end user to the program
print("Hello and Welcome to MadLibs Python Edition")
#The following three lines gather user input and assigns them to variables. 
adj1 = input("Type in an adjective:")
adj2 = input("Type in another adjective:")
adj3 = input("Type in the third adjective:")
noun1 = input("Type in a noun:")
noun2 = input("Type in a second noun:")
noun3 = input("Type in a third noun:")
#The next two lines populate the arrays with the users input.
adjectives = [adj1,adj2,adj3]
nouns = [noun1,noun2,noun3]
#This print statement mixes the arrays with the MadLibs writing.
print("Jeremy woke up from his nap and ate a",adjectives[0], "snack. Then he left his home to visit friends. On the way their, he ran over a ", adjectives[1],nouns[0],". After the accident, he went to a",nouns[1],". During the conversation with",nouns[1],",Jeremy looks up at the sky and sees what appears to be a ",adjectives[2],"star. After staring at the star for a while, he pulls out a ",nouns[2],"to take a picture.")
