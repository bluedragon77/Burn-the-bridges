    # You can place the script of your game in this file.

    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"
    image buildingoutside= "school.png"
    image streetcity= "streetcity.jpg"
    image eridefault= "character.png"

    # Declare characters used by this game.
    define nar = Character('Narrator', color="#c8ffc8")
    define eri = Character('Eri', color="#c77777")
    define yu = Character('Yuki', color="#c8ffc8")
    define a = Character('XY', color="#c55555")


    # The game starts here.
    label start:

        scene buildingoutside

        nar "Two young souls standing at the entrance of their new school.Wanting to leave their past behind and to live to their fullest.Little do they know what awaits them,but still they are smiling daringly looking at their future."

        show eridefault at right
        with dissolve

        eri "'So the terror duo has found a new victim,hahahahahaha...'"

        yu "'Yeah,I guess,hahaha...'"

        yu "But don't forget why we transferred schools..."

        eri "'Gee,don't worry I won't!'The atmosphere was a bit more serious suddenly,but still,quite cheerful,more like an atmosphere of exciting expectation"

        nar "The both of them could not wait to enter their new life in a completely new environment,where everything,except the each of them themselves was new and foreign!"

        eri "You know,they say that if you want to escape your past you gotta burn all the bridges.Don't worry I think we did that nicely."

        yu "'Agh,you are right.' I said that in a relaxed manner."

        yu "But we also have to change,ourselves,you know as people."

        eri "Change is the only thing that is inevitable...kind of romantic,don't you think!"

        yu "'---Um huh,I guess---'I admit I became flustered at this point'We aren't a couple,just childhood friends.'"

        eri "Of course,haha,sorry for the accidental inuendo,haha"

        yu "'Um yeah no problem.'I took out my phone to see what is the time.'Damn we came early,there is still an hour left until our introduction."

        eri "'Weren't you the one who wanted to come early?'Staring at him with an accusing look."

        scene buildingoutside

        yu "Yeah but we came way too early,I did not realise it was such a short trip from the train station up to here."

        eri "'Hmm...'pouting'Well at least the way up here does not look too boring,there are many shops and entertainment areas around here.'"

        yu "Well,schools do seem to attract bussinesses.And at least now we have time to talk."

        eri "Well duh,we're in the middle of Tokyo...Also our schoo seems to be fairly new!"

        scene buildingoutside

        yu "It is a welcome change from the ancient schools we were in before1!"

        eri "You got that right,I am still not over the screeching sounds of the planks in our old school."

        yu "Or the windows you can't even open anymore.Now that I think about it our old school would be an ideal setting for a horror story right?"

        eri "The walking planks...In our school you don't walk on planks,the planks walk on you :P"

        yu "Hahaha"

        eri "Do you have any idea which clubs you will join?"

        yu "Not really,maybe I will maybe I won't join one...How about you?"

        eri "I do want to join one,but only if I find a fitting one,so basically,no idea at all."

        yu "It seems some people are already here for morning club activities."

        eri "Ofcourse...I wonder how many good friends will I meet here,or bitter rivals,they shall see who is the better one."

        yu "Wow you are on fire..."

        yu "I just wonder how many fine women will I meet around here?"

        yu "Ouch that hurt!"

        eri "'Sorry,it was just a reflex' Said with a blank face"

        yu "Yeah very funny"

        eri "I can't help it,it's a curse not a blessing!"

        yu "'Well don't think that's got my spirits down.' Said while smiling from cheek to cheek"

        eri "Now I am sure,you are ready for the mental institution."
        yu "Yeah whatever."
        eri "So what should we do now?"
        menu:
            "What to do?"
            "Let's go for a coffee?":
                yu "Let's go for a coffee break?"
                eri "Sure."
                eri "I am sure all those coffee shops will be very convenient while we wait for trains."
                yu "Sure.I hope at least one of them has Irish cappuccino."
                yu "I just love that sweet smell it has"
                eri "And billiards,they must have billiards."
                eri "And if any of them has Snooker,they will immediately become my favorite."
                yu "Sure,but don't think you will ever be able to beat me."
                eri "Beating you would be an understatement.I will go for nothing less than total humilliation."
                yu "Sure,if you can."
                yu "This place looks nice,shall we go in?"
                eri "Yea..."
                nar "Suddenly there is a huge explosion in the background!"
                yu "Shit,shit,shit,shit,..."
                eri "WTF?"
                nar "troll end"#I will put more here
                return
            "Check our documents.":
                yu "Why don't we check our documents?"
                eri "Yeah,but let's go trough the check list again."
                eri "Personal id-check,Previous schools grades-check,Transfer admittance-check,Old student id-Check,Extra pictures for the new id-check...Man,transfering is a hassle"
                yu "Bad things happen if you forget your documents."
                eri "Well it's not like it's the end of the world."
                yu "That would be ridiculous."


        return
