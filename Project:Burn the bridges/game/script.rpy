﻿    # You can place the script of your game in this file.

    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"
    image buildingoutside= "school.JPG"
    image streetcity= "streetcity.jpg"
    image schoolyard= "1.jpg"
    image nuclear= "nuclear.jpg"
    image hallway1= "hallway1.jpg"
    image eridefault= "something.png"
    image yudefault= "dgh.png"
    image teacher= "sensei.png"
    image ara= "arai.png"

    # Declare characters used by this game.
    define nar = Character('Narrator', color="#c8ffc8")
    define eri = Character('Eri', color="#c77777")
    define yu = Character('Yuki', color="#c8ffc8")
    define teach = Character('XY', color="#c55555")
    define arai = Character('Arai-sensei', color="#c5f5f5")

    # Declaring the flags

    # The game starts here.
    label start:
        # Declaring the flags
        $ intel = 0
        $ reflexes = 0
        $ computer_skills = 0
        $ literature = 0
        $ proactive = 0
        scene buildingoutside

        nar "Two young souls standing at the entrance of their new school.Wanting to leave their past behind and to live to their fullest.Little do they know what awaits them,but still they are smiling daringly looking at their future."

        show eridefault at right
        with dissolve
        show yudefault at left
        with dissolve

        eri "'So the terror duo has found a new victim,hahahahahaha...'"

        yu "'Yeah,I guess,hahaha...'"

        yu "But don't forget why we transferred schools..."

        eri "'Gee,don't worry I won't!'The atmosphere was a bit more serious suddenly,but still,quite cheerful,more like an atmosphere of exciting expectation"

        nar "The both of them could not wait to enter their new life in a completely new environment,where everything,except the each of them themselves was new and foreign!"
        "A sudden silence"
        menu:
            "Break the silence":
                 eri "You know,they say that if you want to escape your past you gotta burn all the bridges.Don't worry I think we did that nicely."
                 $ literature +=1
                 yu "'Agh,you are right.' I said that in a relaxed manner."

                 yu "But we also have to change,ourselves,you know as people."

                 eri "Change is the only thing that is inevitable...kind of romantic,don't you think!"
                 yu "We sound almost poetic."

                 yu "'---Um huh,I guess---'I admit I became flustered at this point'We aren't a couple,just childhood friends.'"

                 eri "Of course,haha,sorry for the accidental inuendo,haha"
            "Wait.":
                 "You decide not to break the silence."
        yu "'I wonder what's the time?.'I took out my phone to see what is the time.'Damn we came early,there is still an hour left until our introduction."

        eri "'Weren't you the one who wanted to come early?'Staring at him with an accusing look."



        yu "Yeah but we came way too early,I did not realise it was such a short trip from the train station up to here."

        eri "'Hmm...'pouting'Well at least the way up here does not look too boring,there are many shops and entertainment areas around here.'"

        yu "Well,schools do seem to attract bussinesses.And at least now we have time to talk."

        eri "Well duh,we're in the middle of Tokyo..."

        eri "Should we check in which class we are right now or later?"
        menu:
            "Right now sounds fine.":
                $ proactive +=1
                yu "Let's do it right now,even though it is already crowded."
                yu "hmmm...OH,we are in the same class."
                eri "Cool."
            "We have time.":
                yu "We have time."
        scene schoolyard
        show eridefault at right
        with dissolve
        show yudefault at left
        with dissolve
        eri "This school seems to be pretty new,doesn't it? Though the outside here seems to try to emulate older architecture."

        yu "It is a welcome change from the ancient schools we were in before!"

        eri "True,I am still not over the screeching sounds of the planks in our old school."

        yu "Or the windows you can't even open anymore.Now that I think about it our old school would be an ideal setting for a horror story right?"

        eri "The walking planks...In our school you don't walk on planks,the planks walk on you :P"

        #yu "Hahaha"

        eri "Do you have any idea which clubs will you join?"

        yu "Not really,maybe I will maybe I won't join one...How about you?"

        eri "I do want to join one,but only if I find a fitting one,so basically,no idea at all."

        yu "It seems some people are already here for morning club activities."

        eri "Ofcourse...I wonder how many good friends will I meet here,or bitter rivals,kuku."

        yu "Wow you are on fire..."

        yu "I just wonder how many fine women will I meet around here?"

        yu "Ouch that hurt!"

        eri "'Sorry,it was just a reflex' Said with a blank face"

        yu "Yeah very funny"

        eri "I can't help it,it's a curse not a blessing!"

        yu "Well don't think that's got my spirits down."

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
                scene nuclear
                show eridefault at right
                with dissolve
                show yudefault at left
                with dissolve
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
                yu "Let's head over to the faculty office to complete our paperwork."
                yu "We should find a teacher first."
                show yudefault at center
                eri "Here is one."
                eri "Good morning,could you perhaps tell us where the faculty office is?"
                teach "Oh,good morning.Are you exchange students by any chance?Of course,let me show you the way."
                scene hallway1
                show eridefault at right
                with dissolve
                show yudefault at center
                with dissolve
                show teacher at left
                yu "The stairs here look tight and they are  padded with iron.."
                teach "Yeah you children should not run around here.The contractor made some construction errors.They weren't big enough to cancel the whole construction though.It will be fixed eventually."
                "As you walk by you see some teachers assembling around a computer room."
                yu "Sensei,what is happening there?"
                teach "Well,I am not very technical,but we are having network problems today.Our LAN works but we have no internet connection."
                menu:
                    "I am not technical either":
                        "I decide to ignore all of it."
                    "I am not sure but,have they tried just turning everything on and off again?":
                        $ proactive +=1
                        yu "Have they tried turning everything on and off again?"
                        teach "They did restart the router..."
                        yu "Not just the router,I mean everything."
                        teach "I don't think they did...I will suggest that to them."
                    "Have they tried flushing the DNS cache?":
                        $ computer_skills = 0
                        yu "They should try to flush the DNS cache if they haven't already. Or in general they should try to look at the DNS settings."
                        yu "That is what usually causes such an issue."
                        teach "Oh ok,I will suggest that to them later."
                eri "Sensei, do we have roof access in this school?"
                teach "Our roof is mostly safe, so we give roof keys to club leaders.So basically yes, because it gives the clubs more freedom to work on their projects."
                eri "Oh and what kind of clubs do you have?"
        teach "We have all kinds of clubs,if you wish,later you can see a list of clubs on the panel by the school entrance."
        teach "Oh,and in our school you can join 2 clubs instead of just one."
        menu:
                "You look around and think..."
                "The walls in here are quite colourful.":
                        "You are impresed by the artistic walls."
                "There are no cameras.":
                        $ intel += 1
                        eri "Sensei,are there cameras in this school?"
                        teach "There is only one camera at the front entrance.The area around here has been very peaceful so far so there was no need for one so far."
                        "That opens up many options."
        menu:
                "You suddenly notice a student screaming at someone who looks like a teacher."
                "Must be because of a bad grade.":
                        "You just go on."
                "I wonder what the circumstances were.":
                        $ intel += 1
                        "You continue while wondering what happened."
        teach "Here is the faculty room,now please wait while I get Arai sensei."
        "A minute passes by while you wait for your new homeroom teacher."
        "The person that comes out looks like an insomnia victim."
        scene hallway1
        show eridefault at right
        with dissolve
        show yudefault at center
        with dissolve
        show ara at left
        yu "Good morning,my name is Yuki Takada,I am 15 years old and I am the new transfer student this year."
        eri "Good morning,I am Eri Fujimoto,I am 16 years old and I am also transferring here"
        arai "Oh,good morning,you must be the new kids. My full name is Makoto Arai, 37. Do you have your documents, so I can pass them on to the school secretary?"
        eri "Ofcourse, here they are for the both of us."
        arai "You two seem quite well acquainted."
        arai "sigh..."
        "Suddenly it was like a weird presence surrounded the hallway."
        arai "Listen you two,I have done a background check on you two.Your teachers considered the both of you to be quite talented and inteligent,however..."
        arai "You Yuki were described as very deconcentrated and even aggressive.I heard a story of how once in middle school you showed a student trough a glass door on pure impulse."
        eri "~grin~"
        arai "And you young lady have nothing to smile for either.You were described as almost sadistic and very egotistical.I have heard everything about how you sometimes sabotaged even whole classes."
        arai "Well let me tell something to the both of you,I SHALL NOT ALLOW THAT AROUND HERE!!"
        "This man is definitely not to be trifled with.However Yuki get's just enough courage to speak up."
        yu "Don't worry sir,that is exactly why we have transferred.We want to run away from our past and turn a new leaf in our lives."
        eri "sigh"
        arai "sigh... Well we will see if those words remain just words. Changing yourself is a long term process you know."
        arai "Anyhow, before second period starts come in front of class 2A.You can find it on the second floor in the southern wing.You are free for now,don't do any mischief on your first day."
        yu "Eri,should we go explore the school grounds?"
        "Eri was still in a slight state of shock"
        eri "ha...ha...How did he...how did he know all of that?Did you say anything?"
        yu "I said, shall we go and explore the school grounds before the beginning of second period?"
        if intel>0:
                yu "And he probably just had contacts from our old school."
                eri "That seems reasonable."
        eri "Ok,let's go explore for a bit."
# I should put this line of text somewhere...        eri "I have been thinking,I mean after seing those three teachers today.Teachers aren't superhumans.They are also just humans with their own range of emotions,strenths and weaknesses.
        "As whom do you want to play from this point on?"
        scene schoolyard
        show eridefault at right
        with dissolve
        show yudefault at left
        with dissolve
        menu:
                "Eri":
                        "You decided to play as Eri"
                        yu "Let's walk around the school first."
                        menu:
                            "Sure.":
                                eri "Yes,it's not like we have anything better to do."
                                $ proactive += 1
                            "Nah I don't feel like it.":
                                "I am already quite tired"
                                eri "I don't feel like walking any more."
                                yu "Come on,it's our first school day at a new school,we must explore the environment."
                                "He seems quite insistent."
                                "Ok,why not."
                                eri "OK,but my feet are going to hurt."
                                menu:
                                    "Will you give me a massage later?":
                                        eri "But you will have to give me a massage later."
                                        yu "No."
                                    "Say nothing.":
                                        "I stay quiet with my thought and give in to his demands."
                                eri "Let's go then."
                        eri "That teacher was quite scary.Wasn't he?"
                        yu "Yes indeed, he had a scary aura."
                        "We decide to take a lap around the school starting left from the main entrance."
                        "The first thing we discovered were the tennis courts.There were no safety nets around them, and the students were practicing their serves."
                        "Some of them were quite good, and there were lot's of them."

                "Yu" :
                        "You decided to play as Yu"
                        eri "Let's walk around the school first."
                        yu "I don't know.After this episode I have lost motivation."
                        eri "Oh come on.You suggested it in the first place."
                        menu:
                               "Oh alright...":
                                    yu "Oh well,whatever,we don't have anything better to do."
                                    $ proactive += 1
                               "Nah I don't feel like it.":
                                    "Why would I?"
                                    yu "Nah,I don't want to."
                                    eri "Come on,you suggested it in the first place."
                                    "She seems quite insistent."
                                    "Ok,why not."
                                    yu "Alirght,alright..."
                                    "As she drags me all around the place."
         

#soon chapter 2 should be here.
        "Chapter 1 ends here.I hope you will visit us again for chapter 2 :) "
        "In chapter 2 we will have character introductions and you will choose your route."
        "Credits:"
        "bluedragon77-Writing and programming,as well as learning python"
        "1stsonamyfan-Graphics"
        "Coffeine-making me not fall down unconscious."
        "Humanity-for being human."                
        "My family,friends and my colleagues and teachers at the Polytechnic of Zagreb,Technical University in Clausthal and Faculty of Organisation and informatics in Varaždin."

        return
