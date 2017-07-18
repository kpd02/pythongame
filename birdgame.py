
#text that starts the game
print("You are a young birdy who has just learned how to fly. Your mommy has just dropped you out of your tree, which you have never left. Your little wings are not quite strong enough to support you. What do you do? \n")

ans1 = input("type A to try and fly or type B to try to break your fall \n")

#start of flying branch
if ans1 == "A":
    print("NO WAY! Your wings worked. Must have been all the extra worms your mommy fed you. Where are you going to fly now? \n")
    ans2 = input("type R to fly to the right and type L to fly to the left \n")

    #Flying to the right
    if ans2 == "R":
        print("Trees! Trees! Trees! You are flying like a rollercoaster, dodging trees left and right. You are having so much fun you forget to remember the path back to your home tree. Yikes! Mommy is about to feed you. What do you do? \n")
        ans3 = input("type A to fly to the top of the nearest tree to look for the top of your tree, and type B to try and retrace your steps under the forest cover \n")

        #start flying to the top of the nearest tree
        if ans3 == "A":
            print("Wait! Is that your home tree? Didn't your momma put a piece of string on the top so she could find it when returning from her hunting trip? You are tired from your rollercoaster flying experience, what do you do?\n")
            ans4 = input("Press A to try and fly above the trees home and press B to stay and cry for mommy")

            #Go home
            if ans4 == "A":
                print("Why did you do that? Night has fallen and the hungry owls are out. You stop for a break and accidentally land on the head on an owl. At least your death was quick.\n")
                print("GAME OVER")

            #stay there
            elif ans4 == "B":
                print("You start to shiver and regret your choice, but a few hours later you hear your mother's distinctive screech. You cry out and she swoopes down and gives you a ride home.\n")
                print("CONGRATS! YOU WON")

        #start retracing steps
        elif ans3 == "B":
            print("You start trying to retrace your steps (or flies, how does this work for birds?) but because of your initial windy path, the going gets rough. You are kind of tired, and are scared of getting more lost.\n")
            ans5 = input("Press A to try and build a nest to snuggle in for the night, and press B to forge ahead\n")

            #stop due to fatigue
            if ans5 == "A":
                print("Never stop in the forest at night! Isn't that how 7 of your older siblings died? You fall out of the tree due to your poor nest and break your neck\n")
                print("GAME OVER \n")

            #continue towards your nest
            elif ans5 == "B":
                print("Smart choice. You always keep moving in the forest. 30 minutes later, you run into your older sister, who adopts you as one of her own. Although you never see your mother again, you at least didn't die??\n")
                print("CONGRATS YOU WON \n")


    #flying to the left
    elif ans2 == "L":
        print("Where did all the trees go? You are flying through an open field! What is this magic? You fly and fly chasing little bugs until your tiny body gets tired. What do you do? \n")
        ans4 = input("type A to take a rest on a log in the marshy area, type B to turn around and find your way home \n")

        #take a rest
        if ans4 == "A":
            print("Bubble bubble. The log starts to sink into the muddy marsh! What is this? You don't know how to swim. What do you do?\n")
            ans6 = input("Press A to try and stay on the log and press B to test your swimming skills\n")

            #drown in the marsh
            if ans6 == "A":
                print("AAAH! Your feet are stuck on the log and you drown. This is not how you thought you'd go out \n")

            #eaten by snake
            elif ans6 == "B":
                print("That bubble bubble was the sound of a snake swimming up. It smells fear and gobbles you in one bit. I guess that's what a snake belly looks like \n")

        #find home
        elif ans4 == "B":
            print("Good choice...for now. Since you are so tired, you are really struggling to get home \n")
            ans7 = input("Press A to hop on the ground accross the field and press B to try to fly \n")

            #hop on the ground
            if ans7 == "A":
                print("You start to feel the ground collapse under you and you drown in the marsh. Should have trusted yourself more \n")
                print("YOU LOST\n")

            #use your wings
            elif ans7 == "B":
                print("What doesn't kill you makes you stronger! You find your way home and are united with your mom!\n")
                print("CONGRATS YOU WON \n")

else:
#start of story if you aim for cushion
    print("Break your fall? You are 20 feet in the air and weigh 1 pound. Thought you would be beating the game by selecting this. Unfortunately your death is slow and painful. Try again. \n")
    print("GAME OVER TRY AGAIN")
