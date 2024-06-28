import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Sample jokes database
# Template for 100 jokes
jokes = [
    {"id": 1, "joke": "Were they really on about a mouse inside that random Mexican restaurant? *points at McDonalds*", "explanation": "McDonalds is not really a mexican place although mexican can work there giving a falsetto vibe. UCSD theory: incongruity and superiority"},
    {"id": 2, "joke": "When someone stops doing weed after being high a long time they gain superpowers: no longer need to sleep or eat. For a while at least", "explanation": "Those arent really super powers. UCSD theory: Incongruity theory and Reversal theory "},
    {"id": 3, "joke": "First World Problems: I need to go to the bathroom again because I ate to many ribs!", "explanation": "UCSD theory: inconruity Theory, Reversal Theory "},
    {"id": 4, "joke": "First World Problems: All my cloths are wet... from working out... for no reason", "explanation": "they are lifting black items aka weights in the gym for no practical purpose"},
    {"id": 5, "joke": "It was runored that Covid-19 was cause by drinking bat piss. breaking news from wuhan china: we drank the piss... alledgedly", "explanation": "they need a coke"},
    {"id": 6, "joke": "That woman is 3/4 Saddam Hussein", "explanation": "thats incest"},
    {"id": 7, "joke": "In hell there is an astrix where it says - or take the UCSD finals. and NO ONE chooses it because the UCSD final are worse than hell", "explanation": "...that's true, I've seen that sign in there"},
    {"id": 8, "joke": "The research topic of how to harness the snitch: is a semi real superpower. people just run up to you TRYING to tell you some dirt", "explanation": "TBD"},
    {"id": 9, "joke": "...the only thing I'm attracted to anymore are girls in full bankai", "explanation": "realistically... I'm going to have to settle for less"},
    {"id": 10, "joke": "You guys been sayin sus?", "explanation": "...i know what its like to not say it"},
    {"id": 11, "joke": "Blender the computer program x food joke: whenever in life someone say 'open blender' i guess things are going pretty good", "explanation": "mmm jamba juice... mmmm"},
    {"id": 12, "joke": "From shrek. I want to be like donkey, because no one has ever come up so much to be a donkey fucking a huge fire breathing dragon", "explanation": "TBD"},
    {"id": 13, "joke": "Its so hot I started sweating from reading at 9:30 am", "explanation": "TBD"},
    {"id": 14, "joke": "What kind of accent do you have? an adult swim accent", "explanation": "TBD"},
    {"id": 15, "joke": "Added cheese 'the american way' *evil laugh* MORE! MORE! muahaha", "explanation": "TBD"},
    {"id": 16, "joke": "Cheese is the only food that can cause white people to stop being hungry", "explanation": "TBD"},
    {"id": 17, "joke": "New worst insult to freckles people: 'omfg is your face covers in flees", "explanation": "TBD"},
    {"id": 18, "joke": "Umm.. what is the correct gem stoen ring to give to your GF to have a polygamy relationship?", "explanation": "TBD"},
    {"id": 19, "joke": "Some says that is 'male gaze', I'm like nah thats male straights!", "explanation": "TBD"},
    {"id": 20, "joke": "Dyslexia: *clears throat* 'lex luthor is a fag' ...'you are cured'", "explanation": "TBD"},
    {"id": 21, "joke": "*alert* all registers are down at target 'god dam skynet has been stopped'", "explanation": "TBD"},
    {"id": 22, "joke": "The visual arts studio at UCSD is surrounded by jurrassic park style defense. WTF is in there?", "explanation": "TBD"},
    {"id": 23, "joke": "20 million dollars to find out what happened to me! ...it was nothing", "explanation": "TBD"},
    {"id": 24, "joke": "Best tyoe of aids ...maids", "explanation": "that is true"},
    {"id": 25, "joke": "They say 'stop brinking coke because it is bad for you' NO! you tell cokes to change!", "explanation": "TBD"},
    {"id": 26, "joke": "Free Palestine! '...maybe they will stop if you say is has more than 0 value'", "explanation": "TBD"},
    {"id": 27, "joke": "low chairaphanalia. def: no place to sit", "explanation": "TBD"},
    {"id": 28, "joke": "We go to ask the computer 'what will i die from'. it says 'cancer'. she makes the face -_-. the computer suddenly recalculates and says 'hepatitis, aids and minor friction burns'", "explanation": ":D"},
    {"id": 29, "joke": "Cloths let fat people get away with being fat", "explanation": "TBD"},
    {"id": 30, "joke": "Warning: that is a karen in the dormant phase", "explanation": "TBD"},
    {"id": 31, "joke": "Hasbula save palestine", "explanation": "TBD"},
    {"id": 32, "joke": "My password make them say 'I consent to everything with matt' when they type it in", "explanation": "TBD"},
    {"id": 33, "joke": "The Ai tool: anus detailer. I forgot how completely nessesary that is", "explanation": "TBD"},
    {"id": 34, "joke": "Bomb sniffing pomeranian, basically super under-cover dog", "explanation": "TBD"},
    {"id": 35, "joke": "It seems like I have gained a few pounds of 'you know what' ....it's pubes. GOOD NEWS! she eats pubes! 'oh my god finally'", "explanation": "TBD"},
    {"id": 36, "joke": "Bomb threat? '...its probably in my neck and I dont even know about it'", "explanation": "TBD"},
    {"id": 37, "joke": "It's not my fault I am from the weed prohibition era", "explanation": "TBD"},
    {"id": 38, "joke": "18 wheeler joke: 'who brought this mexican buss'", "explanation": "TBD"},
    {"id": 39, "joke": "When I wrote this I was looking for 'Advance Computational Intelligence for Dummy's", "explanation": "TBD"},
    {"id": 40, "joke": "Why did the pizza end up in the oven? It was a feminist trying to get out of the kitchen, by any means possible", "explanation": "TBD"},
    {"id": 41, "joke": "Mexican food Capitalism evolution is crazy in san diego. If the food is bad at all we will go next door and they will close", "explanation": "TBD"},
    {"id": 42, "joke": "Your parent is only hot because you are great", "explanation": "TBD"},
    {"id": 43, "joke": "A new study revealed that when whales beach themself on land. it is because they are trying to get out of UCSD test anxiety", "explanation": "TBD"},
    {"id": 44, "joke": "First Sign of the Rise of the Machines: Malfunctioning auto toilet", "explanation": "TBD"},
    {"id": 45, "joke": "Mouse satan, aka the human who experiment on mouse. write the hardest test of all time", "explanation": "TBD"},
    {"id": 46, "joke": "Jesus would ask to get nailed back to the cross from the stres of UCSD. he will say 'PUT ME BACK!'", "explanation": "Benine Violation Theory, Incongruity theory, Reversal theory"},
    {"id": 47, "joke": "Team Name: 'You didn't do a good job' ...yea ...thats their team name", "explanation": "TBD"},
    {"id": 48, "joke": "Elevatoriouse, the prison", "explanation": "stuck in a evlevator at the wrong time is pretty bad"},
    {"id": 49, "joke": "Mexican accent: 'jeck' -> check", "explanation": "TBD"},
    {"id": 50, "joke": "Cunnalingus fish?  ...its cuttle fish! ...ohhhh", "explanation": "TBD"},
    {"id": 51, "joke": "With all the clout of UCSD, it still gets a dirty bathroom...", "explanation": "TBD"},
    {"id": 52, "joke": "Ancient humans say 'east side' then leaves africa", "explanation": "TBD"},
    {"id": 53, "joke": "Anyone who doesnt like it overcooks their meat! -_-   ...you bastard!", "explanation": "TBD"},
    {"id": 54, "joke": "That is not a spliff!!  ...it only has weed...", "explanation": "TBD"},
    {"id": 55, "joke": "Reading Hamlet. ...is that about a pig or something", "explanation": "TBD"},
    {"id": 56, "joke": "Extremely loose academic integrity rules like: 'did they have guns?'  ...no? NOT CHEATING! ", "explanation": "TBD"},
    {"id": 57, "joke": "This is the best laptop... for doing cocaine!", "explanation": "Incongruity Theory, Reversal Theory"},
    {"id": 58, "joke": "Did you want any? ...well it doesnt mean you can have it, I'm just checking", "explanation": "TBD"},
    {"id": 59, "joke": "In the name of all white people I hear by reclaim rice from the asians. We also like rice!", "explanation": "TBD"},
    {"id": 60, "joke": "69 is gay, it should be 68 or 89. People are stupud for that", "explanation": "TBD "},
    {"id": 61, "joke": "lofi means low finance, its bad, stop labeling yourself something bad", "explanation": "TBD"},
    {"id": 62, "joke": "Karate flop into the bed. The only reason the earth was saved was becasue the bed was there", "explanation": "TBD"},
    {"id": 63, "joke": "*Demonstraits how to escape after putting fired chicken into the chocolate fountain*", "explanation": "TBD"},
    {"id": 64, "joke": "It says that is holy ground, it sounds dangerouse, it may break your ancles", "explanation": "TBD"},
    {"id": 65, "joke": "If chick-fil-a is chicken, then what is panda express... ", "explanation": "TBD"},
    {"id": 66, "joke": "There is basically poo everywhere... at a medical level", "explanation": "TBD"},
    {"id": 67, "joke": "Its open horse AI", "explanation": "source"},
    {"id": 68, "joke": "Why does the last french fry taste so bad?", "explanation": "TBD"},
    {"id": 69, "joke": "Hollowed out books are becoming a more safe place to hide things", "explanation": "TBD"},
    {"id": 70, "joke": "Is Gary from one piece?", "explanation": "...no"},
    {"id": 71, "joke": "She says 'im nervouse' reply 'thats just my spirit pressure, reiatsu'", "explanation": "TBD"},
    {"id": 72, "joke": "I ride the trolly so you basically need an air born immune boost to go near me", "explanation": "TBD"},
    {"id": 73, "joke": "The monk on instagram says' never give up' ...wtf does he know?", "explanation": "TBD"},
    {"id": 74, "joke": "After the 5th booster shot it is possible to become addicted to the corona virus vaccine", "explanation": "TBD"},
    {"id": 75, "joke": "Seth Rogan Style: Bring open drink into the restroom and through the whole process be taking sips", "explanation": "similar to open container driving"},
    {"id": 76, "joke": "Toyota Highlander: There can be only one!", "explanation": "TBD"},
    {"id": 77, "joke": "Thats whore-able not horrible", "explanation": "TBD"},
    {"id": 78, "joke": "This is pretty much how I party *drinks from the milk gallon in the fridge*   ...now you know", "explanation": "TBD"},
    {"id": 79, "joke": "Free sandwhich? for how long?   ...free sandwhich for ONCE!", "explanation": "TBD"},
    {"id": 80, "joke": "Food is the reagent for poop ...its a poop joke", "explanation": "TBD"},
    {"id": 81, "joke": "Fake japanses: 'ho-die' family surname", "explanation": "TBD"},
    {"id": 82, "joke": "Why do you like your school? Well its not from the parking", "explanation": "TBD"},
    {"id": 83, "joke": "Stressed is deserts backwards", "explanation": "TBD"},
    {"id": 84, "joke": "Being sore from workout when everyone else is fat", "explanation": "TBD"},
    {"id": 85, "joke": "We really need to stop age and live forever so we can all just keep playing world of warcraft", "explanation": "TBD"},
    {"id": 86, "joke": "Harnes the homeless", "explanation": "TBD"},
    {"id": 87, "joke": "My role model for dating is my dog. He is a butt licker. ... with that in mind, I'm pretty sure that girl should have stayed.", "explanation": "TBD"},
    {"id": 88, "joke": "Why are all the pyramids abandonded? what a waste of time", "explanation": "TBD"},
    {"id": 89, "joke": "Why didn't anyone tell me i was the beast titan IRL", "explanation": "TBD"},
    {"id": 90, "joke": "The new anime has 11 boy characters and only 1 girl. Who sat there and drew 11 boys?", "explanation": "TBD"},
    {"id": 91, "joke": "The blue pill takes you to One Piece Land, the red pill takes you to Naruto Land", "explanation": "TBD"},
    {"id": 92, "joke": "Roomba is a bread theft! wtf cut its hands off!", "explanation": "it doesnt have hands"},
    {"id": 93, "joke": "I need to licked clean from all the sweating while doing VR work", "explanation": "TBD"},
    {"id": 94, "joke": "Run and run and run and workout and workout, then go to dennys ONCE and your are fat again", "explanation": "TBD"},
    {"id": 95, "joke": "It's a UFO!!! ...thats a to go box of pancakes... ", "explanation": "TBD"},
    {"id": 96, "joke": "We dont do butt stuff, we only do ass to mouth stuff", "explanation": "TBD"},
    {"id": 97, "joke": "Deamon nuns are not scarry, I'm abount to double dip poo into her vagina if she doesnt calm down", "explanation": "TBD"},
    {"id": 98, "joke": "If we give barrack obama a polygraph I want to ask if we can say the n-word just to see what the polygraph does.", "explanation": "TBD"},
    {"id": 99, "joke": "Hey looks its batman! no... it's the Jeepers Creepers monster. Dam thats way worse", "explanation": "TBD"},
    {"id": 100, "joke": "Worst kind of aids, financial aids", "explanation": "TBD"},
]

# Initialize main window
root = tk.Tk()
root.title("Joke Randomizer")

# Define Tkinter variables after initializing root window
joke_text = tk.StringVar()
explanation_text = tk.StringVar()

last_joke_id = None

def get_random_joke():
    global last_joke_id
    joke = random.choice(jokes)
    last_joke_id = joke['id']
    joke_text.set(joke['joke'])
    explanation_text.set("")

def get_joke_explanation():
    global last_joke_id
    if last_joke_id is not None:
        joke = next((j for j in jokes if j["id"] == last_joke_id), None)
        if joke:
            explanation_text.set(joke['explanation'])
        else:
            messagebox.showerror("Error", "Explanation not found.")
    else:
        messagebox.showinfo("Info", "You need to get a joke first!")

# Load background image and resize
nft_image_path = "jokeGUI.png"  # Ensure jokeGUI.png is in the same directory as this script
bg_image = Image.open(nft_image_path)
bg_image = bg_image.resize((1000, 1000), Image.LANCZOS)  # Resize the image with LANCZOS filter
bg_image = ImageTk.PhotoImage(bg_image)

# Create a canvas and set the background
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Joke label on the left
joke_label = tk.Label(root, textvariable=joke_text, wraplength=100, bg="white", fg="black", font=("Arial", 14))
joke_label_window = canvas.create_window(150, 200, window=joke_label, anchor="nw")

# Explanation label on the right
explanation_label = tk.Label(root, textvariable=explanation_text, wraplength=100, bg="white", fg="black", font=("Arial", 12))
explanation_label_window = canvas.create_window(850, 200, window=explanation_label, anchor="ne")

# "Tell a Joke" button
joke_button = tk.Button(root, text="Tell a Joke", command=get_random_joke, font=("Chafurin", 22), bg="black", fg="white")
joke_button_window = canvas.create_window(510, 780, window=joke_button, anchor="center")

# "Explanation" button
explanation_button = tk.Button(root, text="Explanation", command=get_joke_explanation, font=("Chafurin", 20), bg="black", fg="white")
explanation_button_window = canvas.create_window(510, 845, window=explanation_button, anchor="center")

# Start the main loop
root.mainloop()
