menu = int(input(""" 
                MENU
            1 -> Phonebook
            2 -> Messages 
            3 -> Chat
            4 -> Call register
            5 -> Tones
            6 -> Settings
            7 -> Call divert
            8 -> Games
            9 -> Calculator
           10 -> Reminders
           11 -> Clock
           12 -> Profiles
           13 -> SIM services
           99. Ends the program
           Press a number to access the menu options: """
            ))
the_phone_is_on = True
while(the_phone_is_on):
    match(menu):
        case 99:
            the_phone_is_on = False
            print("Goodbye")
        case 1: 
            #in_the_phonebook = True
            #while(in_the_phonebook):
                print("Phonebook")
                phonebook = int(input("""

                            1. Search
                            2. Service Nos.1
                            3. Add name
                            4. Erase
                            5. Edit
                            6. Assign tone
                            7. Send b’card
                            8. Options
                            9. Speed dials
                            10. Voice tags
                            Enter a number to access Phonebook: """
                             ))
                
                match(phonebook):
                    case 1: print('Search')
                    case 2: print('Service Nos.1')
                    case 3: print('Add name')
                    case 4: print('Erase')
                    case 5: print('Edit')
                    case 6: print('Assign tone')
                    case 7: print('Send b’card')
                    case 8: 
                        #in_options = True
                        #while(in_options):
                            print('Options')
                            options = int(input("""
                                        1. Type of view
                                        2. Memory status
                                        Enter a number to access the Options menu: 
                                        """
                                         ))
                                
                            match(options):
                                case 1: print("Type of view")
                                case 2: print("Memory status")
                                #case 0: 
                                    #in_options = False
                                    #print("Go back")
                                case _: print("Not valid")
                    case 9: print('Speed dials')
                    case 10: print('Voice tags')
                    #case 0: 
                        #in_the_phonebook = False
                        #print('Go back')
                    case _: print('Not Valid')#done with phonebook 
        case 2:
              print("Messages")
              messages = int(input("""

                        1. Write messages
                        2. Inbox
                        3. Outbox
                        4. Picture messages
                        5. Templates
                        6. Smileys
                        7. Message settings
                        8. Info service
                        9. Voice mailbox number
                        10.Service command editor
                        Enter a number to access message option: """
                        ))
              match(messages):
                    case 1: print('Write messages')
                    case 2: print('Inbox')
                    case 3: print('Outbox')
                    case 4: print('Picture messages')
                    case 5: print('Templates')
                    case 6: print('Smileys')
                    case 7: print('Message settings')
                    case 8: print('Info service')
                    case 9: print('Assign tone')
                    case 10: print('Send b’card')
                    #case 0: 
                        #in_the_messages = False
                        #print('Go back')
                    case _: print('Not Valid')
        case 3: print("Chat")
        case 4: print("Call register")
        case 5: print("Tones")
        case 6: print("Settings")
        case 7: print("Call divert")
        case 8: print("Games")
        case 9: print("Calculator")
        case 10: print("Reminders")
        case 11: print("Clock")
        case 12: print("Profile")
        case 13: print("SIM services")
        case _: print('not valid')
