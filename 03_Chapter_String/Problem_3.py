sentence="i am a  boy."
print(sentence.find("  "))
#Find is used to get index,it does not give boolean,here we have used to ust ensure double space is present or not

print("  " in sentence)
#It will give boolean output

print(sentence.index("  "))
#if it find then give the index and if not find then give error it is the difference from "find"
