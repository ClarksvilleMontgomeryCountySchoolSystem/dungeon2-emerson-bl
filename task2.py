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
print("The door is ahead. Whether you make it through depends on one thing - do you have the key?")
has_key = True
if has_key:
    outcome = 'Click:' "You find the key laying around. You put the key through the hole. You may continue"
    print(good)
else:
    outcome = 'Doom:' "You could not find the key. You are dead"
    print(bad)
print(outcome)