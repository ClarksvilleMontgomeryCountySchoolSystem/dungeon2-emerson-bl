print("You're in the corridor now. Somewhere ahead, a guard is patrolling.")
guard_awake = False
if not guard_awake:
    outcome = 'Shadow:' "Be careful...he's asleep. You were able to be quiet. You may continue"
else:
    outcome = 'Doom:' "Be careful...he's awake. You were not quiet. You are dead"
print(outcome)
