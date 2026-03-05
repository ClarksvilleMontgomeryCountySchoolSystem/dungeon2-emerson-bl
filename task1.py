print("You wake up on a cold stone floor. Your torch may be lit - and that changes everything.")
torch_lit =  True
if torch_lit:
    outcome = 'Flicker:' "You light the torch with a lighter. You may continue"
else:
    outcome = 'Doom:' "You couldnt find a lighter. You are dead"
print(outcome)
