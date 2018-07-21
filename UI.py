#!/usr/bin/env python
action = raw_input('What would you like to do? Enter here---> ')

if action == 'send':
    plainOrAttachment = raw_input('Would you like to have an attachement?  (y/n):  ')
    if plainOrAttachment == 'n':
        import plainEmail
    elif plainOrAttachment == 'y':
        import richEmail
elif action == 'view':
    import viewer
    