define e = Character("Elliot")
define m = Character("Mr.Robot")
define w = Character("White Rose")

image start = Movie(size=(1280, 720), play="videos/start.webm")
image Move_the_barrel = Movie(size=(1280, 720), play="videos/Move The Barrel.mkv")
image Enter_tunnel = Movie(size=(1280, 720), play="videos/Enter_Tunnel.mkv")
image Read_note = Movie(size=(1280, 720), play="videos/Read_Note.mkv")
image Move_on = Movie(size=(1280, 720), play="videos/Move_On.mkv")
image Look = Movie(size=(1280, 720), play="videos/Look.mkv")
image Get_On_The_Ship = Movie(size=(1280, 720), play="videos/Get_On_The_Ship.mkv")
image Return_and_search_the_dungeon = Movie(size=(1280, 720), play="videos/Return_and_search_the_dungeon.mkv")
image Enter_Tunnel_2 = Movie(size=(1280, 720), play="videos/Enter_Tunnel_2.mkv")
image Read_Note_2 = Movie(size=(1280, 720), play="videos/Read_Note_2.mkv")
image Light_A_Match_2 = Movie(size=(1280, 720), play="videos/Light_A_Match_2.mkv")
image Leave_Crawl = Movie(size=(1280, 720), play="videos/Leave_Crawl.mkv")
image Stay = Movie(size=(1280, 720), play="videos/Stay.mkv")
image Scout_the_way_to_the_exit_2 = Movie(size=(1280, 720), play="videos/Scout_the_way_to_the_exit_2.mkv")
image Look_2 = Movie(size=(1280, 720), play="videos/Look_2.mkv")
image Get_on_the_ship_2 = Movie(size=(1280, 720), play="videos/Get_on_the_ship_2.mkv")
image Jump_off_the_ship = Movie(size=(1280, 720), play="videos/Jump_off_the_ship.mkv")
image Return_to_a_friend = Movie(size=(1280, 720), play="videos/Return_to_a_friend.mkv")
image Stay_with_a_friend = Movie(size=(1280, 720), play="videos/Stay_with_a_friend.mkv")
image Return_to_a_friend_2 = Movie(size=(1280, 720), play="videos/Return_to_a_friend_2.mkv")
image Return_to_the_beach = Movie(size=(1280, 720), play="videos/Return_to_the_beach.mkv")
image Put_the_barrel_back = Movie(size=(1280, 720), play="videos/Put_the_barrel_back.mkv")
image Move_the_barrel_2 = Movie(size=(1280, 720), play="videos/Move_the_barrel_2.mkv")
image Search_the_dungeon = Movie(size=(1280, 720), play="videos/Search_the_dungeon.mkv")
image Sit_down_next_to_my_friend = Movie(size=(1280, 720), play="videos/Sit_down_next_to_my_friend.mkv")
image Light_a_match = Movie(size=(1280, 720), play="videos/Light_a_match.mkv")
image Scout_the_way_to_the_exit = Movie(size=(1280, 720), play="videos/Scout_the_way_to_the_exit.mkv")
image Enter_tunnel_3 = Movie(size=(1280, 720), play="videos/Enter_tunnel_3.mkv")
image Continue_scouting_the_path = Movie(size=(1280, 720), play="videos/Continue_scouting_the_path.mkv")
image Sit_down_next_to_my_friend_2 = Movie(size=(1280, 720), play="videos/Sit_down_next_to_my_friend_2.mkv")
image Search_the_dungeon_2 = Movie(size=(1280, 720), play="videos/Search_the_dungeon_2.mkv")
image Sit_down_next_to_my_friend_3 = Movie(size=(1280, 720), play="videos/Sit_down_next_to_my_friend_3.mkv")
image Move_the_barrel_3 = Movie(size=(1280, 720), play="videos/Move_the_barrel_3.mkv")
image Enter_the_door = Movie(size=(1280, 720), play="videos/Enter_the_door.mkv")







# The game starts here.

label start:
    scene start
    pause 4.0
    "You`re trapped in a dungeon with your friend. You see a barrel. What do you do?"
    
    menu:
        "Move the barrel":
            jump Move_the_barrel
        "Search the dungeon":
            jump Search_the_dungeon_2
        "Sit down next to my friend":
            jump Sit_down_next_to_my_friend_3

    return


#seyam choice tree
label Sit_down_next_to_my_friend_3:
    scene Sit_down_next_to_my_friend_3
    show black behind Sit_down_next_to_my_friend_3
    "Friend hands you a note. But it's too dark to read in here. What do you do?"
    menu:
        "Move the barrel":
            jump Move_the_barrel_3
        "Search the dungeon":
            jump Search_the_dungeon_2
    return

label Move_the_barrel_3:
    scene Move_the_barrel_3
    "The barrel rolls aside and you find a secret tunnel. What do you do?"
    menu:
        "Enter tunnel":
            jump Enter_tunnel
    return

#dwam choice tree
label Search_the_dungeon_2:
    scene Search_the_dungeon_2
    "The dungeon is empty, but in your pocket you find a box with one match. What do you do?"
    menu:
        "Move the barrel":
            jump Move_the_barrel_2
        "Sit down next to my friend":
            jump Sit_down_next_to_my_friend
    return


#first choice tree

label Move_the_barrel:

    scene Move_the_barrel

    "The barrel rolls aside and you find a secret tunnel. What do you do?"
    menu:
        "Enter tunnel":
            jump Enter_tunnel
        "Search the dungeon":
            jump Search_the_dungeon
        "Sit down next to my friend":
            jump Sit_down_next_to_my_friend_2
    return

    label Sit_down_next_to_my_friend_2:
        scene Sit_down_next_to_my_friend_2
        show black behind Sit_down_next_to_my_friend_2
        "Friend hands you a note. But it's too dark to read in here. What do you do?"
        menu:
            "Enter tunnel":
                jump Enter_tunnel
            "Search the dungeon":
                jump Search_the_dungeon
        return

#first choice from above Move_the_barrel
label Enter_tunnel:
    scene Enter_tunnel
    pause 0.5
    "You start to escape but your friend is too weak to go with you. He hand you a note. What do you do?"
    menu:
        "Read note":
            jump Read_note
        "Return and search the dungeon":
            jump Return_and_search_the_dungeon
    return



#first choice from above Enter_tunnel

label Read_note:
    scene Read_note
    show black behind Read_note
    "It is too dark to read the note. What do you do?"
    menu:
        "Move on":
            jump Move_on
    return


label Move_on:
    scene Move_on
    show black behind Move_on
    "You crawl through the tunnel and the tunnel leads to a beach. What do you do?"
    menu:
        "Look":
            jump Look
    return

label Look:
    scene Look
    "In the water you see a ship. What do you do?"
    menu:
        "Get on the ship":
            jump Get_on_the_ship
    return

label Get_on_the_ship: #ending
    scene Get_On_The_Ship
    "You boarded a ship that is going to a new world, but was spotted by the crew. They approach with their weapons drawn."
    return

#second choice from Enter_tunnel
label Return_and_search_the_dungeon:
    scene Return_and_search_the_dungeon
    "The dungeon is empty, but in your pocket you find a box with one match. What do you do?"
    menu:
        "Enter tunnel":
            jump Enter_tunnel_2
        "Put the barrel back":
            jump Put_the_barrel_back
    return 

label Put_the_barrel_back:
    scene Put_the_barrel_back
    "In silence you hear..."
    m "Is any of it real? I mean, look at this."
    m "Look at it!"
    m "A world built on fantasy. Synthetic emotions in the form of pills."
    m "Psychological warfare in the form of advertising."
    m "Mind-altering chemicals in the form of... food!"
    m "Brainwashing seminars in the form of media."
    m "Controlled isolated bubbles in the form of social networks."
    m "Real? You want to talk about reality?"
    m "We haven't lived in anything remotely close to it since the turn of the century."
    m "We turned it off, took out the batteries,"
    m "snacked on a bag of GMOs while we tossed the remnants in the ever-expanding dumpster of the human condition."
    m "We live in branded houses trademarked by corporations"
    m "built on bipolar numbers jumping up and down on digital displays,"
    m "hypnotizing us into the biggest slumber mankind has ever seen."
    m "You have to dig pretty deep, kiddo, before you can find anything real."
    m "We live in a kingdom of bullshit."
    m "A kingdom you've lived in for far too long."
    m "So don't tell me about not being real."
    m " I'm no less real than the fucking beef patty in your Big Mac."
    menu:
        "Move the barrel":
            jump Move_the_barrel_2
    return
return

label Move_the_barrel_2:
    scene Move_the_barrel_2
    "The barrel rolls aside. You see a secret tunnel. What do you do?"
    menu:
        "Enter tunnel":
            jump Enter_tunnel_2 #labo ending'y sare dachi 
    return

#second choice from above Move_the_barrel

label Search_the_dungeon:
    scene Search_the_dungeon
    "The dungeon is empty, but in your pocket you find a box with one match. What do you do?"
    menu:
        "Enter tunnel":
            jump Enter_tunnel_2
        "Sit down next to my friend":
            jump Sit_down_next_to_my_friend
    return

label Enter_tunnel_2:
    scene Enter_Tunnel_2
    
    "You start to escape but your friend is too weak to go with you. He hand you a note. What do you do?"
    menu:
        "Read Note":
            jump Read_Note_2
    return

label Read_Note_2:
    scene Read_Note_2
    show black behind Read_Note_2
    "It is too dark to read the note. What do you do?"
    menu:
        "Move on":
            jump Move_on #labo ending'y sarawa dachi
        "Light a match":
            jump Light_a_match_2
    return

label Light_a_match_2:
    scene Light_A_Match_2
    show black behind Light_A_Match_2
    "The note says, 'Don`t leave me here.' Do you leave your friend or stay?"
    menu:
        "Leave":
            jump Leave
        "Stay":
            jump Stay
        "Scout the way to the exit":
            jump Scout_the_way_to_the_exit_2
    return


label Leave:
    scene Leave_Crawl
    show black behind Leave_Crawl
    "You crawl through the tunnel and the tunnel leads to a beach. What do you do?"
    menu:
        "Look":
            jump Look
    return

label Stay:
    scene Stay
    pause 4.0
    "Here nothing can be considered 'real', all this is just ILLUSION. Illusion is dispelled. You see the eXit."
    menu:
        "Enter the door":
            jump Enter_the_door #labo ending
    return

label Scout_the_way_to_the_exit_2:
    scene Scout_the_way_to_the_exit_2
    show black behind Scout_the_way_to_the_exit_2
    "You crawl through the tunnel and the tunnel leads to a beach. What do you do?"
    menu:
        "Look":
            jump Look2
    return


#second choice from Search_the_dungeon

label Sit_down_next_to_my_friend:
    scene Sit_down_next_to_my_friend
    show black behind Sit_down_next_to_my_friend
    "Friend hands you a note. But it's too dark to read in here. What do you do?"
    menu:
        "Light a match":
            jump Light_a_match

    return

label Light_a_match:
    
    scene Light_a_match
    show black behind Light_a_match
    "The note says, 'Don`t leave me here.' Do you leave your friend or stay?"
    menu:
        "Scout the way to the exit":
            jump Scout_the_way_to_the_exit
        "Leave":
            jump Leave
        "Stay":
            jump Stay
    return


label Scout_the_way_to_the_exit:
    scene Scout_the_way_to_the_exit
    "You see a secret tunnel. What do you do?"
    menu:
        "Enter tunnel":
            jump Enter_tunnel_3
        "Stay with a friend":
            jump Stay_with_a_friend
    return

label Enter_tunnel_3:
    scene Enter_tunnel_3
    "You start to escape but your friend is too weak to go with you. What do you do?"
    menu:
        "Continue scouting the path":
            jump Continue_scouting_the_path
        "Stay with a friend":
            jump Stay_with_a_friend
    return

label Continue_scouting_the_path:
    scene Continue_scouting_the_path
    show black behind Continue_scouting_the_path
    "You crawl through the tunnel and the tunnel leads to a beach. What do you do?"
    menu:
        "Look":
            jump Look2
    return


label Look2:
    scene Look_2
    "In the water you see a ship. What do you do?"
    menu:
        "Get on the ship":
            jump Get_on_the_ship_2
        "Return to a friend":
            jump Return_to_a_friend_2
    return

label Return_to_a_friend_2:
    scene Return_to_a_friend_2
    "Your friend is too weak to go with you. What do you do?"
    menu:
        "Return to the beach":
            jump Return_to_the_beach
        "Stay with a friend":
            jump Stay_with_a_friend #labo edning'y dwam
    return


label Return_to_the_beach:
    scene Return_to_the_beach
    "In the water you see a ship. What do you do?"
    menu:
        "Get on the ship":
            jump Get_on_the_ship_2 #endling'y dwam dachi
    return

    
label Get_on_the_ship_2:
    scene Get_on_the_ship_2
    "You boarded a ship that is going to a new world, but was spotted by the crew. They approach with their weapons drawn."
    menu:
        "Jump off the ship":
            jump Jump_off_the_ship #labo endlingy dwam dachi
    return


label Jump_off_the_ship:
    scene Jump_off_the_ship
    "You swim to the beach and watch the ship sail away. What do you do?"
    menu: 
        "Return to a friend":
            jump Return_to_a_friend #labo endlingy dwam dachi
    return

label Return_to_a_friend:
    scene Return_to_a_friend
    "Your friend is too weak to go with you. What do you do?"
    menu:
        "Stay with the friend":
            jump Stay_with_a_friend #labo edning'y dwam dachi
    return

#ending'y dwam
label Stay_with_a_friend:
    scene Stay_with_a_friend
    pause 4.0
    "ILLUSION is dispelled. You see the eXit. Consciousness opened the door. You can leave the current matrix in The Out and create a new world inside yourself."
    menu:
        "Enter the door":
            jump Enter_the_door
    return

label Enter_the_door:
    scene Enter_the_door
    w "I`ve always found doors fascinating inventions. They hold the entry to unlimited imagination. Before you open any door, a world filled with possibilities sits right behind it. And it isn`t until you open it, they are realized."

return
    