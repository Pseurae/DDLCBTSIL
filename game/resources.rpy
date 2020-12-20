default persistent.rickRollPos = 0
python early:
    quit_fake = False

    def _quit_hook(relaunch=False, status=0, save=False):
        global quit_fake
        if save and (renpy.store._quit_slot is not None):
            renpy.loadsave.save(renpy.store._quit_slot, getattr(renpy.store, "save_name", ""))

        if renpy.has_label("quit"):
            renpy.call_in_new_context("quit")
        
        if quit_fake:
            renpy.show_screen('dialog', message='Nope. You can go fuck yourself.', ok_action=Hide('dialog'))
            return

        raise renpy.game.QuitException(relaunch=relaunch, status=status)

    renpy.quit = _quit_hook

init python:
    import time
    import pygame

    def hex_to_RGB(hex):
        return list([int(hex[i:i+2], 16) for i in range(1,6,2)])

    def linear_gradient(start, finish=Color("#FFFFFF"), n=10):
        s = [int(val * 255) for val in start.rgb]
        f = [int(val * 255) for val in finish.rgb]
        RGB_list = [s]
        for t in range(1, n):
            curr_vector = tuple([int(s[j] + (float(t)/(n-1))*(f[j]-s[j])) for j in range(3)])
            RGB_list.append(curr_vector)
        return RGB_list

    def color_tag(tag, argument, contents):
        rv = [ ]
        startColor, _, endColor = argument.partition('-')
        if not startColor or not endColor:
            return contents
        startColor = Color(startColor)
        endColor = Color(endColor)
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                buffer = ''
                grad_list = linear_gradient(startColor, endColor, len(text.replace(" ", '')))
                color_index = 0
                for letter in text:
                    if letter != ' ':
                        rv += [(renpy.TEXT_TAG, u"color={}".format(Color(tuple(grad_list[color_index])).hexcode)), (renpy.TEXT_TEXT, letter), (renpy.TEXT_TAG, u"/color")]
                        color_index += 1
                    else:
                        rv.append((renpy.TEXT_TEXT, letter))
            else:
                rv.append(kind, text)
        return rv
    
    config.custom_text_tags["grad"] = color_tag

    def stop_shaking_after_shooting(pos=None):
        while renpy.music.get_pos('sound') < pos and not config.skipping:
            pass
        renpy.show_layer_at([])
        return

    def set_nat_yuri_pos():
        time.sleep(0.25)
        if not config.skipping:
            renpy.show('natsuki', at_list=[t32])
            renpy.show('yuri 1a', at_list=[t33])

    stolen_positions = ['Lead Dev', 'Lead Artist', 'Lead Writer', 'Lead Coder',
                        'Artist #1', 'Artist #2', 'Artist #3',
                        'Writer #1', 'Writer #2', 'Writer #3',
                        'Coder #1', 'Coder #2', 'Coder #3',
                        'Dropkicked a Llama', 'Killed a Moose', 'Then Killed a blonde anime girl',
                        'Brazilian', 'jk from \'MURICA', 'Moe Lester',
                        'Doki Sitter', 'Yuri Tarded', 'Mike Oxshort',
                        'Jack Goff', 'Hugh Jazz', 'Fortnite Master',
                        'Who da fuq plays Fortnite?', 'Joe Mama',
                        'Polish Cow', 'Doesn\'t Like Milk', 'Hates KGK']

    creds_list = [   {  'name':'Stuff',
                        'nation': 'No',
                        'age': '[[REDACTED]]',
                        'sex': 'All day',
                        'hobby':'Gaming, Procrastinating, Drinking milk, Taking femurs, Selling femurs, Eating femurs, Taking kidneys, Selling kidneys, Eating kidneys.',
                        'favdoki': '{s}Mr Cow{/s} Mademoiselle Moo',
                        'mods': '{a=https://discord.gg/vac4AKbEpN}Doki Doki Milk{/a}',
                        'logo_path': 'mod_assets/dokidokimilk.png'},

                        {'name': 'Atsukari',
                        'nation': '[[REDACTED]]',
                        'age': '17',
                        'sex': 'Yes',
                        'hobby': 'Videogames and anime, yes i know it\'s cliche fuck you.',
                        'favdoki': 'Natsuki',
                        'mods': 'Doki Doki Silky Heart',
                        'logo_path': 'mod_assets/silkyheart.png'},

                        {'name': 'RedLeader',
                        'nation': 'Vodka Drinkers',
                        'age': '19',
                        'sex': 'Always',
                        'hobby': 'Gaming and coding',
                        'favdoki': 'The one beaten with lead pipe.',
                        'mods': '{a=https://discord.gg/4GCWc2n}Doki Doki Cold Heart{/a}',
                        'logo_path': 'mod_assets/cold_heart.png'},

                        {'name': 'ThoMysteriousY [[Tom]]',
                        'nation': '[[REDACTED]]',
                        'age': '[[REDACTED]]',
                        'sex': 'Male',
                        'hobby': 'Photoshop editing, Listening to power metal music, Watching videos, Doing exercise, Getting better in Photoshop.',
                        'favdoki': 'Yuri',
                        'mods': 'The Walking Doki Literature Club',
                        'logo_path': 'mod_assets/TWDLCLogo.png'},

                        {'name': 'Llama',
                        'nation': 'American',
                        'age': '69',
                        'sex': 'For sure',
                        'hobby': 'Graphic design, Video editing, Messing with Straw',
                        'favdoki': 'Llama',
                        'mods': '{a=https://discord.gg/SNH87wJcXZ}Literature Association{/a}',
                        'logo_path': 'mod_assets/lit_association.png'},

                        {'name': 'Soldat',
                        'nation': 'Tacolover',
                        'age': '13+',
                        'sex': 'Chibi (M)',
                        'hobby': 'Videogames, Animation, Kayak row',
                        'favdoki': 'Sayori',
                        'mods': '{a=https://discord.gg/tC65T8BTqT}Prison Architect{/a}',
                        'logo_path': 'mod_assets/prisonarchitect.png'},

                        {'name': 'That One Engineer',
                        'nation': '2Fort',
                        'age': '???',
                        'sex': 'Wrench',
                        'hobby': 'Putting people on the naughty or nice list',
                        'favdoki': 'Logic',
                        'mods': 'Abyssal Attendant, MS Paint Club'},

                        {'name': 'RyzekNoavek',
                        'nation': 'A fucking jungle',
                        'age': 'Hoping I\'ll live long enough to give birth then outlive my child',
                        'sex': 'Fuckable',
                        'hobby': 'Eating grass, cannibalism, anime, coding',
                        'favdoki': 'MC',
                        'mods': '{a=https://discord.gg/FEMAgFj}Doki Doki Sinking Love{/a}',
                        'logo_path': 'mod_assets/titanic_pog.png'}]

    stickerDict = {':pog:': 'mod_assets/pog.png'}

    def createScaledImage(key, img, upscaled=False):
        def scale(width, height):
            if upscaled:
                targetWidth = style.say_dialogue.size * 3
            else:
                targetWidth = style.say_dialogue.size
            height = float((height * targetWidth) / width)
            width = targetWidth
            return width, int(height)

        newSize = scale(*renpy.image_size(img))
        return im.Scale(img, *newSize)

    for key, value in stickerDict.items():
        renpy.display.image.images[(key,)] = createScaledImage(key, value, True)
        renpy.display.image.images[(key + '_scaled',)] = createScaledImage(key + '_scaled', value)

    def fr_text_filter(text):
        for key, value in stickerDict.items():
            if key in text:
                if key == text.replace(" ", ""):
                    text = text.replace(key, "{{image={0}}}".format(key))
                else:
                    text = text.replace(key, "{{image={0}}}".format(key+'_scaled'))

        return text

    config.say_menu_text_filter = fr_text_filter

    def logRickRollPos():
        try:
            while renpy.music.is_playing('rickroll') and 'mod_assets/Weiss_Asslee.ogg' in renpy.music.get_playing('rickroll'):
                if renpy.music.get_pos('rickroll'):
                    persistent.rickRollPos = renpy.music.get_pos('rickroll')
        except:
            pass
        return
    
    def playRickroll():
        if type(persistent.rickRollPos) in (int, float):
            if persistent.rickRollPos >= (213 * 7 / 8):
                persistent.rickRollPos = 0
            renpy.music.play("<from {}>mod_assets/Weiss_Asslee.ogg".format(persistent.rickRollPos), channel='rickroll', loop=False, fadein=2.0)
            renpy.music.queue("mod_assets/Weiss_Asslee.ogg", channel='rickroll', loop=True)
        else:
            renpy.music.play("mod_assets/Weiss_Asslee.ogg", channel='rickroll')

    renpy.music.register_channel('rickroll', mixer='rickroll', loop=True, tight=False)
    renpy.music.set_pause(True, 'rickroll')
    _preferences.set_volume('rickroll', 1.0)

init 999 python:
    char_list = []
    def autozorder_char(event, interact=True, **kwargs):
        global transformTracker, autofocusedChars, focusOnNextDialogue

        tag = kwargs.get('image')

        if not interact:
            return

        if event == "begin":
            for char in char_list:
                if renpy.showing(tag): renpy.show(tag, zorder=0)

            if renpy.showing(tag):
                renpy.show(tag, zorder=3)

        return

    for obj in globals().values():
        if isinstance(obj, renpy.character.ADVCharacter) and obj.image_tag:
            obj.display_args['callback'] = autozorder_char
            obj.cb_args['image'] = obj.image_tag
            char_list.append(obj.image_tag)

transform weiss_anim(fract, total_time, prev_frac=0.0):
    subpixel True
    on show:
        xanchor 1.0 xpos 0.0
        parallel:
            linear total_time * (fract - prev_frac) xanchor 1.0 - fract xpos fract
        parallel:
            block:
                linear total_time * (fract - prev_frac) rotate 360.0 * 3 * fract
    on hide:
        parallel:
            linear total_time * (fract - prev_frac) xanchor 1.0 - fract xpos fract
        parallel:
            block:
                linear total_time * (fract - prev_frac) rotate 360.0 * 3 * fract

transform credits_scroll(t):
    subpixel True
    ypos 1.0
    linear t yanchor 1.0 ypos 0.0

transform wiggle_loop():
    block:
        linear 0.1 xoffset -2 yoffset 2
        linear 0.1 xoffset 3 yoffset -4 
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 4
        linear 0.1 xoffset 0 yoffset 0
        repeat
    on replaced:
        linear 0.1 xoffset 0 yoffset 0

transform rush(x=640, z=0.80):
    yanchor 1.0 subpixel True transform_anchor True
    alpha 1.00
    parallel:
        easein_cubic .15 xcenter x zoom z*1.00
    parallel:
        easein .05 yoffset 0 ypos 1.03

transform falldown:
    on hide:
        transform_anchor True
        parallel:
            linear 0.25 rotate 75.0
        parallel:
            easein 0.75 xoffset 200
        parallel:
            easein 0.5 yoffset 400

transform falldown_sayo:
    on hide:
        transform_anchor True
        parallel:
            linear 0.5 rotate 75.0
        parallel:
            easein 1.25 xoffset 200
        parallel:
            easein 1.0 yoffset 400

transform out_of_face(x=640, z=0.80, y=500):
    subpixel True
    parallel:
        easein .1 yoffset -20
    parallel:
        easein .35 zoom z*1.00 xcenter x yanchor 1.0 ypos 1.03

transform launch():
    on hide:
        easein_cubic 0.25 yanchor 1.0 ypos -0.1

transform ryze_up(x=640, z=0.80):
    ypos 1.1 xcenter x zoom z*1.00
    easein_cubic .35 yanchor 1.0 ypos 1.03

transform death_wiggle():
    subpixel True
    xoffset 0
    easein 0.05 xoffset 10
    easeout 0.05 xoffset 0
    easein 0.05 xoffset -5
    easeout 0.05 xoffset 0

transform fall(z=0.80, pause=0.2):
    on hide:
        parallel:
            easein .25 zoom 1.05 * z
        parallel:
            death_wiggle
        parallel:
            pause pause
            easeout_cubic 0.5 ypos 2.5

transform slow_walk1(z=0.80):
    xalign 1.0 xpos 0.0 yoffset -5 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        easeout 0.5 xpos 0.15
        0.1
        easeout 0.5 xpos 0.3
        0.1
        easeout 0.5 xpos 0.45
        0.1
        easeout 0.5 xpos 0.6
        0.1
        easeout 0.5 xpos 0.75
        0.1

transform pickup():
    transform_anchor True
    linear 0.25 xoffset -50 yoffset 50
    linear 0.75 rotate 75.0 xpos 300 yoffset -100 xoffset -0

transform slow_walk2(z=0.80):
    parallel:
        easeout 0.5 xoffset 240
        0.1
        easeout 0.5 xoffset 480
        0.1
        easeout 0.5 xoffset 720
        0.1
        easeout 0.5 xoffset 1060
        0.1
        easeout 0.5 xoffset 1200
        0.1

transform delayed_show(delay=0.0, duration=5.0):
    subpixel True
    yanchor 0.0 ypos 1.0 zoom 0.5
    pause delay
    easein 5.0 yalign 0.5 zoom 1.0
    pause duration
    easeout 5.0 ypos 0.0 yanchor 1.0 zoom 0.5

image weiss_chibi normal = 'mod_assets/weiss_chibi.png'
image weiss_chibi shot = 'mod_assets/shot_weiss_chibi.png'

screen last_screen():
    on 'show' action Function(playRickroll), SetVariable('quit_fake', True)

screen credits_scene():
    zorder 150
    $ delay = 2.0
    $ duration = 5.0
    $ x = 0.0
    add 'game_menu_bg'
    frame:
        xpadding 100
        background Solid('#0007')
        for i, cred_dict in enumerate(creds_list):
            frame at delayed_show(delay, duration):
                background None
                ysize 720
                xfill True
                vbox:
                    style_prefix 'final_credits'
                    spacing 15
                    yalign 0.5
                    vbox:
                        spacing 5
                        label 'Name' text_underline True
                        text cred_dict['name']
                    vbox:
                        spacing 5
                        label 'Nationality' text_underline True
                        text cred_dict['nation']
                    vbox:
                        spacing 5
                        label 'Age' text_underline True
                        text cred_dict['age']

                    vbox:
                        spacing 5
                        label 'Sex' text_underline True
                        text cred_dict['sex']

                    vbox:
                        spacing 5
                        label 'Hobbies' text_underline True
                        text cred_dict['hobby']

                    vbox:
                        spacing 5
                        label 'Favorite Doki' text_underline True
                        text cred_dict['favdoki']

                    vbox:
                        spacing 5
                        label 'Mods' text_underline True
                        text cred_dict['mods']
                
                if 'logo_path' in cred_dict:
                    add cred_dict['logo_path']:
                        size (384, 384)
                        xalign 1.0 yalign 0.01
                else:
                    add 'mod_assets/DDLCBTSIL.png':
                        size (384, 384)
                        xalign 1.0 yalign 0.01

            $ delay += duration + 7.0
    timer delay + duration action Return()
    on "show" action SetVariable('quit_fake', True), Function(hide_windows_enabled, enabled=False),  PauseAudio('music', True), Function(playRickroll), Function(renpy.invoke_in_thread, logRickRollPos)
    on "hide" action SetVariable('quit_fake', False), Function(hide_windows_enabled, enabled=True), PauseAudio('music', False), Function(playRickroll), Function(renpy.music.stop, 'rickroll', 2.0)

style final_credits_label is gui_label
style final_credits_label_text is gui_label_text
style final_credits_text is gui_text

style final_credits_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size 28
    color "#fff"
    outlines [(2, "#b59", 0, 0), (2, "#b59", 0, 0)]
    yalign 0.5


screen fake_cred_tear(number=10, offtimeMult=0.25, ontimeMult=0.25, offsetMin=0, offsetMax=150, srf=None):
    zorder 150
    add Tear(number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf) size (1280,720)
    timer 0.1 action Hide("fake_cred_tear")

screen fake_cred(char):
    default astley_flag = renpy.random.randint(0, 5) == 1
    add Solid("#000")

    vbox at credits_scroll(35.0):
        xfill True
        spacing 5
        null height 100
        for pos in stolen_positions:
            label pos:
                xalign 0.5
                text_size 36
                text_underline True

            if astley_flag:
                text 'Rick Astley':
                    xalign 0.5
                    size 28
            else:
                text char:
                    xalign 0.5
                    size 28

            null height 5
        null height 100

    timer 35.0 action Return()

    if astley_flag:
        timer 7.0 action Show('fake_cred_tear'), SetScreenVariable('astley_flag', False)

    on "show" action SetVariable('quit_fake', True), Function(hide_windows_enabled, enabled=False),  PauseAudio('music', True), Function(playRickroll), Function(renpy.invoke_in_thread, logRickRollPos)
    on "hide" action SetVariable('quit_fake', False), Function(hide_windows_enabled, enabled=True), PauseAudio('music', False), Function(playRickroll), Function(renpy.music.stop, 'rickroll', 2.0)

image pacman:
    "mod_assets/Pacman/frame_00_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_01_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_02_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_03_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_04_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_05_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_06_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_07_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_08_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_09_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_10_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_11_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_12_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_13_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_14_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_15_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_16_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_17_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_18_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_19_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_20_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_21_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_22_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_23_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_24_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_25_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_26_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_27_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_28_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_29_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_30_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_31_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_32_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_33_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_34_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_35_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_36_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_37_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_38_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_39_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_40_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_41_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_42_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_43_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_44_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_45_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_46_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_47_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_48_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_49_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_50_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_51_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_52_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_53_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_54_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_55_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_56_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_57_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_58_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_59_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_60_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_61_delay-0.1s.png"
    pause 0.1
    "mod_assets/Pacman/frame_62_delay-0.1s.png"
    pause 0.1
    repeat

image funny_cow:
    "mod_assets/Funny Cow/frame_00_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_01_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_02_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_03_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_04_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_05_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_06_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_07_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_08_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_09_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_10_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_11_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_12_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_13_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_14_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_15_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_16_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_17_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_18_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_19_delay-0.1s.png"
    0.1
    "mod_assets/Funny Cow/frame_20_delay-0.1s.png"
    0.1
    repeat

image motherfucker = 'mod_assets/motherfucker/1.png'

image monika 1aa = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), 'mod_assets/monika/aa.png')
image monika 1ab = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), 'mod_assets/monika/ab.png')
image monika 1ac = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), 'mod_assets/monika/ac.png')
image monika 1ad = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), 'mod_assets/monika/angry1.png')
image monika ae = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), 'mod_assets/monika/angry2.png')
image monika yand = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), 'mod_assets/monika/yandere.png')

image natsuki 1lewd = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/1lewd.png")
image natsuki 2lewd = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/lewd_biatch.png")

image sayori yand = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), 'mod_assets/sayori/yandere_face.png')

image afmc = im.FactorScale('mod_assets/AFMC/1a.png', 0.95)
image emmc = im.FactorScale('mod_assets/EMMC/1a.png', 0.95)

image tom 1a = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/a.png")
image tom 1b = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/b.png")
image tom 1c = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/c.png")
image tom 1d = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/d.png")
image tom 1e = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/e.png")
image tom 1f = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/f.png")
image tom 1g = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/g.png")
image tom 1h = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/h.png")
image tom 1i = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/i.png")
image tom 1j = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/j.png")
image tom 1k = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/k.png")
image tom 1l = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/l.png")
image tom 1m = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/m.png")
image tom 1n = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/n.png")
image tom 1o = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/o.png")
image tom 1p = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/p.png")
image tom 1q = im.Composite((960, 960), (0, 0), "mod_assets/tom/1.png", (0, 0), "mod_assets/tom/q.png")

image tom 2a = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/a.png")
image tom 2b = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/b.png")
image tom 2c = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/c.png")
image tom 2d = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/d.png")
image tom 2e = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/e.png")
image tom 2f = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/f.png")
image tom 2g = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/g.png")
image tom 2h = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/h.png")
image tom 2i = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/i.png")
image tom 2j = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/j.png")
image tom 2k = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/k.png")
image tom 2l = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/l.png")
image tom 2m = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/m.png")
image tom 2n = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/n.png")
image tom 2o = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/o.png")
image tom 2p = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/p.png")
image tom 2q = im.Composite((960, 960), (0, 0), "mod_assets/tom/2.png", (0, 0), "mod_assets/tom/q.png")

image tom 3a = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/a.png")
image tom 3b = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/b.png")
image tom 3c = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/c.png")
image tom 3d = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/d.png")
image tom 3e = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/e.png")
image tom 3f = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/f.png")
image tom 3g = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/g.png")
image tom 3h = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/h.png")
image tom 3i = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/i.png")
image tom 3j = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/j.png")
image tom 3k = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/k.png")
image tom 3l = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/l.png")
image tom 3m = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/m.png")
image tom 3n = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/n.png")
image tom 3o = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/o.png")
image tom 3p = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/p.png")
image tom 3q = im.Composite((960, 960), (0, 0), "mod_assets/tom/3.png", (0, 0), "mod_assets/tom/q.png")

image tom 4a = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/a.png")
image tom 4b = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/b.png")
image tom 4c = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/c.png")
image tom 4d = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/d.png")
image tom 4e = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/e.png")
image tom 4f = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/f.png")
image tom 4g = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/g.png")
image tom 4h = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/h.png")
image tom 4i = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/i.png")
image tom 4j = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/j.png")
image tom 4k = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/k.png")
image tom 4l = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/l.png")
image tom 4m = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/m.png")
image tom 4n = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/n.png")
image tom 4o = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/o.png")
image tom 4p = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/p.png")
image tom 4q = im.Composite((960, 960), (0, 0), "mod_assets/tom/4.png", (0, 0), "mod_assets/tom/q.png")

image yuri shot = "mod_assets/shuri.png"
image sayori shot = "mod_assets/shotyori.png"
image monika shot = "mod_assets/shotika.png"
image natsuki shot = 'mod_assets/shotsuki.png'

image straw think = 'mod_assets/straw/thinkemoji.png'
image straw normal = 'mod_assets/straw/strawdisgusted.png'

image llama = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/llama.png")

image stuff = 'mod_assets/stuff.png'

image wiess = "mod_assets/wiess.png"

image atsu normal = 'mod_assets/atsu/atsu.png'
image atsu angry = 'mod_assets/atsu/atsu_angry.png'

image bg bean = "mod_assets/bean.jpg"

image bg raid_shadow_legend = 'mod_assets/raid_shadow_legend.png'

image eyeopen:
    'black'
    alpha 1.0
    pause 1.0
    block:
        easein_cubic 0.85 alpha 0.0

define tom = Character('ThoMysteriousY', image='tom', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_outlines=[(3, '#080838', 0, 0), (1, '#080838', 1, 1)])
define straw = Character('StrawCup', image='straw', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_outlines=[(3, '#b10011', 0, 0), (1, '#b10011', 1, 1)])
define llama = Character('TheLlamaOfficial', image='llama', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_outlines=[(3, '#9dcce9', 0, 0), (1, '#9dcce9', 1, 1)])
define atsu = Character('Atsukari', image='atsu', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_outlines=[(3, '#eb81c7', 0, 0), (1, '#eb81c7', 1, 1)])
define stuff = Character('Stuff', image='stuff', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_outlines=[(3, '#f7f700', 0, 0), (1, '#f7f700', 1, 1)])