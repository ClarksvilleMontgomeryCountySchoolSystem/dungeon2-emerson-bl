bad = r"""
 ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
    mls                              .$"
                                     "
"""
good = r"""

            <>=======()
           (/\___   /|\\          ()==========<>_
                 \_/ | \\        //|\   ______/ \)
                   \_|  \\      // | \_/
                     \|\/|\_   //  /\/
                      (oo)\ \_//  /
                     //_/\_\/ /  |
                    @@/  |=\  \  |
                         \_=\_ \ |
                           \==\ \|\_ snd
                        __(\===\(  )\
                       (((~) __(_/   |
                            (((~) \  /
                            ______/ /
                            '------'
"""
print("The exit is in sight. But the drawbridge - is it down?")
drawbridge_raised = True
if not drawbridge_raised:
    outcome = 'Thunder:' "The drawbride seems to be raised. You may continue"
    print(good)
else:
    outcome = 'Doom' "The drawbridge seems to be lowereed. The gaurd soon catches you. You are dead"
    print(bad)
print(outcome)
