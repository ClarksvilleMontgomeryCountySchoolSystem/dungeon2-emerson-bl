print("The exit is in sight. But the drawbridge - is it down?")
drawbridge_raised = True
if not drawbridge_raised:
    outcome = 'Thunder:' "The drawbride seems to be raised. You may continue"
else:
    outcome = 'Doom' "The drawbridge seems to be lowereed. The gaurd soon catches you. You are dead"
print(outcome)