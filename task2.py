print("The door is ahead. Whether you make it through depends on one thing - do you have the key?")
has_key = True
if has_key:
    outcome = 'Click:' "You find the key laying around. You put the key through the hole. You may continue"
else:
    outcome = 'Doom:' "You could not find the key. You are dead"
print(outcome)
