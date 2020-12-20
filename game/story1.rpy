label act1:
    stop music
    scene black
    with dissolve_scene_full

    mc "Another day, another dollar."
    mc "Nothing new is going to happen today."
    mc "Unless, yeah, something interesting happens."
    mc "{i}Let's fucking goooooooooo!!!{/i}"
    show bg class_day with wipeleft_scene
    play music t2

    menu:
        "Are you sure you want to play this?"
        "Yes":
            pass
        "No":
            $ renpy.quit()

    $ s_name = "???"
    s "Hey there!"
    $ s_name = "Sayori"
    mc "Hello, Sayori."
    show sayori 1b at t11
    s "How's your day today, [player]?"
    s 4r "I hope it was very interesting!!"
    show sayori
    mc "Meh, kinda. It's still the same."
    s 1a "Uuhh... You should change it somehow, [player]!" 
    mc "How? Everything is the same, go to school, survive by the boredom, and then go home."
    show natsuki 1g at l31
    n "Are we boring?!"
    show sayori 4r at hf11
    s "Chimken time!"
    show sayori 1q at t11
    show natsuki 5e at f21
    show sayori at t22
    n "Sayori, not now! I'm waiting for an answer from [player]!"
    n 5g "But, what if I want?"
    show natsuki at t21
    mc "... are you okay? You're arguing with yourself at this point."
    show sayori at f22
    s 3x "Oh, I'm okay."
    show sayori 1q at t22
    show natsuki 1z at hf21
    n "Chimken time!"
    show natsuki at t21
    mc "I'll just go to take my stuff."
    show natsuki at lhide
    hide natsuki
    show sayori at t11
    s 4q "{i}{grad=#fdfff5-#f8efce}drinks milk{/grad} {/i}" 
    show sayori at t22
    show funny_cow:
        yalign 0.4
        xanchor 1.0
        xpos 0.5
        zoom 2.0
    s 4s "Funny Cow."
    show sayori 4q
    show natsuki 1v at l41
    show funny_cow:
        easein 0.25 xanchor 0.5
    show sayori at t44
    show natsuki at f41
    n "Nooooo!"
    n "There goes the employees of Literature corp!"
    show funny_cow at thide
    hide funny_cow
    show monika 1r at rightin(880)
    show sayori at rhide
    hide sayori
    show natsuki at t21
    show monika at f22
    m "Llama isn't a llama. Fuckin' Hell."
    show monika 1i at t22
    show yuri 2l at l21
    show natsuki at lhide
    hide natsuki
    show yuri at f21
    y "We all know that Llama is horny!"
    show yuri 2g at t21
    show monika at f22
    m "How horny????"
    show monika at t22
    "Very."
    window hide
    pause 2.0
    m 1p "...Is the script broken?"
    show yuri at t31
    show natsuki 5w at f32
    show monika at t33
    show yuri at f31
    ny "Shit man, Monika be awarin'."
    show yuri at t31
    show natsuki at t32
    show monika at f33
    m 1i "Stop this right here."
    show monika at t33
    show natsuki 4o
    show yuri 1f
    mc "How bout' faak u?"
    show monika at f33
    m "...No."
    show sayori 1b at rightin(1080)
    show yuri at t41
    show natsuki at t42
    show monika at t43
    show sayori at f44
    s "Shit [player], you got toasted."
    show sayori at rhide
    hide sayori
    show yuri at t31
    show natsuki at t32
    show monika at t33
    pause 0.35
    show natsuki 1v at hf11
    n "SHUT."
    show natsuki 1v at hf11
    n "THE DAMN."
    show natsuki 1v at hf11
    n "UP."
    m 4m "Yes, Natsuki's right! Calm down, everyone!"
    show natsuki 1r
    m 4n "You won't like me when I'm horny…"
    show yuri at t41
    show natsuki at t42
    show sayori 1u at f43
    show monika 4m at t44
    s 1u "..."
    s 4w "MMMCUSE ME???"
    show sayori at t43
    show yuri at f41
    y 3k "{i}plays the only thing they fear is you{/i}"
    y 3f "Hey guys… let's all calm down for now."
    $ style.say_dialogue = style.edited
    y 1y1 "You're interrupting my third eye opening, you little sluts..."
    $ style.say_dialogue = style.normal
    show yuri at t41
    show monika 1i at f44
    m "W-What.. this isn't Yuri… And I never tampered with her.."
    show monika at t44

    mc "Then, fix her?"
    show monika at f44
    m 5b "I- It seems that I've been locked out of my console!"
    show monika at t44
    mc "Wait, so… she's gonna be like this forever?"
    show sayori at f43
    s 3x "YOOO THAT'S POG :pog:{nw}"
    show sayori at t43
    show natsuki at f42
    n 2h "... Lemme."
    show natsuki at t42
    mc "Sayori, shut the fuck up if you please?"
    show sayori 5
    n 4x "Won't work. You all are just jerks."
    show natsuki at rhide
    hide natsuki
    show yuri at t31
    show sayori at t32
    show monika at t33
    mc "Everyone stop being {b}horny{/b}!"
    mc "Natsuki's gone."
    show yuri at f31
    y ":pog:"
    show yuri at t31
    mc "Yurk. Hand me my {i}{color=#5b5d5c}lead{/color} pipe{/i}."
    show black zorder 10:
        alpha 0.7
    show motherfucker onlayer front:
        xcenter 640
        alpha 0.0
        easein 0.25 alpha 1.0
    "Wallace" "Hello, I'm Wallace." 
    mc "Go away, Wallace." 
    mc 'You can go fuck yourself!'
    show motherfucker at launch onlayer front
    hide motherfucker onlayer front
    pause 0.35
    hide black
    show sayori at f32
    s "Didn't Soldat say that no other characters are allowed?"
    show sayori at t32
    mc "That's why he doesn't have a sprite."
    mc "Um..., But since Soldat is reading this, hes probably gonna add the Wallace sprite now :L"
    show yuri at f31
    y 1y3 "Mustard on my feet."
    $ style.say_dialogue = style.edited
    y "Yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    $ style.say_dialogue = style.normal
    show natsuki 1f at l41
    show yuri at t42
    show sayori at t43
    show monika at t44
    show natsuki at f41
    n "That's my fetish, get over here Yuri.."
    show natsuki 1f at t41
    show yuri at f42
    y 3y4 "When you got back?!"
    show natsuki 1f at f41
    show yuri at t42
    n "{i}COME ON!!!{/i}{nw}"
    show yuri 3o
    extend " Those Natsuri Simps aren't gonna please themselves."
    show natsuki:
        subpixel True
        on hide:
            easeout .5 xcenter -300
    show yuri:
        subpixel True
        on hide:
            easeout .5 xcenter -300
    hide natsuki
    hide yuri
    show sayori at f43
    s 3l "So uhm, is this all gonna be out of context?"
    show sayori at f21
    show monika at t22
    s 3s "Amor Fati MC when?"
    $ style.say_dialogue = style.edited
    s 1x "I missed the way he used to watch me pee…"
    $ style.say_dialogue = style.normal
    hide sayori
    hide monika
    with wipeleft
    show afmc at t11
    "Amor Fati MC" "Hi?"
    mc "WHAT THE FUCKKK THIS DOESNT MAKE ANY SENSE!"
    show afmc at t21
    show emmc at f22
    "Exit Music MC" '"Henlo"'
    show emmc at t22
    show afmc at f21
    "Armor Fatty MC & Regular MC" '"Fuck off, you\'re a walking copyright infringement!"'
    scene black with wipeleft_scene
    stop music
    window hide
    pause 2.00
    window show 
    "Hello."
    "It seems that you've reached a very unfortunate stage of the mod."
    "This is where you get CBTed."
    "We're currently finding a way to restore some of the personalities back."
    "All the shenanigans that have occurred will be all officially circumcised and obliterated as soon as possible."
    "And now we shall call this…"
    "An actual… {w} DDLC mod."
    "Llama & Straw" "This is where you applaud now."
    window hide
    scene end with dissolve_scene_full
    pause 0.5
    window show
    "HA!{w=1.0} Imagine if it didn't end, funniest shit I've ever seen."
    return
