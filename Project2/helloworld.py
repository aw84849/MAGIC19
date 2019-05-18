import random
response = raw_input("Welcome to my little insignifcant book and movie recommendation generator. Can I recommend a book or a movie for you? ") 
while True:
  books_response = ["books", "Books", "book", "Book", "BOOKS", "BOOK"]
  if response in books_response : 
      genre = raw_input("What genre of books do you like? Valid answers: Fantasy, Dystopian Fiction. Enter any other genre for a random reccomendation, but I can't promise you'll like it. ")
      fantasy_response = ["Fantasy", "fantasy", "FANTASY"]
      dystopian_fiction_response = ["Dystopian Fiction", "Dystopian fiction", "dystopian fiction", "dystopian Fiction", "dystopian", "DYSTOPIAN", "DYSTOPIAN FICTION", "DYSTOPIANFICTION", "dystopianfiction"]
      if genre in fantasy_response :
        fantasy_recomendation = ["Dealing with Dragons by Patricia C. Wrede", "Harry Potter and The Sorcerer's Stone by Harry Potter", "Eragon by Christopher Paolini", "The Land of Stories, The Wishing Spell by Chris Colfer", "Artemis Fowl by Eoin Colfer", "The Golden Compass by Phillip Pullman", "The Inquisitor's Tale by Adam Gidwitz", "The Girl Who Drank the Moon by Kelly Barnhill", "Wings of Fire. The Dragonet Prophecy by Tui T. Sultherland"]
        print ("I like Fantasy books too! I think you'll like a book called %s" % (random.choice(fantasy_recomendation)))
      elif genre in dystopian_fiction_response :
        dystopian_fiction_recomendation = ["The City of Ember by Jeanne DuPrau", "Renegades by Marissa Meyer", "Cinder by Marissa Meyer", "The Mysterious Benedict Society by Trenton Lee Stewart", "The House of The Scorpion by Nancy Farmer", "Divergent by Veronica Roth", "The Hunger Games by Suzanne Collins", "The Eighth Day by Dianne K. Salerni", "The Darkest Minds by Alexandra Bracken"]
        print ("Dystopian Books are great, but sometimes creepy. I think you'll like a book called %s" % (random.choice(dystopian_fiction_recomendation)))
      else :
        other_types_of_books = ["The Thing About Leftovers by C. C. Payne", "Click Here To Start by Denis Markell", "The Fourteenth Goldfish by Jennifer L. Holm", "Flora and Ulysses by Kate DiCamillo", "The Phantom Tollbooth By Norton Juster", "Lucky Strike by Bobbie Pyron", "Island of the Aunts by Eva Ibbotson", "Greenglass House by Kate Milford", "Treasure Hunters by James Patterson and Chris Grabenstien", "Ungifted by Gordon Kormon", "Restart by Gordon Korman", "How To Train Your Dragon by Cressida Cowell", "Percy Jackson and The Olympians, The Lightning Thief by Rick Riordan (One of My ALL TIME FAVORITE Authors", "Pegasus, The Flame of Olympus by Kate O'Hearn", "The Bad Beginning by Lemony Snicket (Great Author, Really recommend.)"]
        print ("That genre needs help. You need help, but I am willing to recommend a book for you. If it isn't in your prefered genre, whoop di do. That's your problem. Read %s. Also, I warned you." % (random.choice(other_types_of_books)))
      break
  
  else :
      genre_movies = raw_input("Why would you chose movies? Fine. What genre of movies do you like? Valid answers: Live Action, Disney, and Superhero ")
      live_action_response = ["Live Action", "Live action", "live action", "live Action" "LIVEACTION", "liveaction", "LIVE  ACTION"]
      disney_response = ["Disney", "disney", "DISNEY"]
      superhero_response = ["Superhero", "superhero", "Super Hero", "super hero", "super Hero", "SUPERHERO", "SUPER HERO"]
      cartoons_response = ["Cartoons", "cartoons"]
      if genre_movies in live_action_response :
        live_action_recommedation = ["Paddington (One and Two, Both are equally good.)", "The Labyrinth (DAVID. BOWIE. Is the villan. He sings. So good.)", "The Greatest Showman (O. M. G. The songs! There's Zendaya, Zac Efron, HUGH JACKMAN, and Keala Settle. 11/10 would reccomend)", "Star Wars: A New Hope( YESSSS. WATCH THEM ALL)", "Harry Potter and the Sorcerers Stone (WATCH THEM ALL. WATCH THEM ALL.)", "The Hunger Games (Jennifer Lawrence. Need I say more?)", "Jurassic Park (The first one is a bit gory, but still good)", "The Goonies (HILARIOUS)", "Ferris Bueller's Day Off (ONE OF THE BEST.)", "Miss Congeniality (SANDRA BULLOCK)", "Pratical Magic (SANDRA BULLOCK)", "While You Were Sleeping (SANDRA BULLOCK)", "Fantasic Beast And Where To Find Them (One and Two)", "Pitch Perfect (Anna Kendrick, and Rebel Wilson. Awesome singing)", "Willow (Mild jumpscare, but really good)", "The Princess Bride (I laughed, I cried, it was beautiful. Amazing love story)", "Mamma Mia (one and two. do yourself a favor and watch this. One has Meryl Streep, and Two has Meryl Streep AND CHER!)"]
        print ("I still disagree with the choice of movies. If you must, watch %s" % (random.choice(live_action_recommedation)))
      elif genre_movies in disney_response : 
        disney_recomendations = ["Inside Out", "Brave", "Avatar (NOT the last airbender. yeesh. It's the one directed by James Cameron)", "Tangled", "Maleficent", "The Princess and The Frog", "Up (sad opening montauge.)", "The Incredibles (ONE and TWO. I REPEAT ONE AND TWO)", "The Lion King (Original Only)", "Frozen (Yes, There is a sequel, no it isn't out yet (as of April 2019), yes you should watch it.)", "Aladdin (Both cartoon and live action, which as of April of 2019 isn't out yet, but will be)", "Big Hero 6 (The television series is good too, but this is better)", "Cinderella (Live action only. Animated is okay, but live action has LILY JAMES)", "Beauty and the Beast (Live action. Animated is good, but live action has Emma Watson and Dan Stevens and Luke Evens and Josh Gad and Emma Watson and Ian McKellen and Emma Thompson and Emma Watson and Ewan McGregor and Audra McDonald and did I mention Emma Watson?)", "Moana (OKAY LISTEN UP. THIS MOVIE HAS MUSIC WRITTEN BY LIN. MANUEL. MIRANDA. YOU BEST WATCH IT)", "Zootopia (not zootropolis, very good.)", "The Aristocats (very sassy lassy, good plot, evil butler.)", "Mary Poppins (both one and two. One has Julie Andrews and Dick Van Dyke. Two has EMILY BLUNT AND LIN MANUEL MIRANDA)", "Parent Trap (Both are good, one has a great plot, the other has a great plot AND Lindsay Lohan", "ALL THE DISNEY MOVIEs EVER MADE (They're really good)"]
        print ("Disney movies are okay. I don't really care, but it's not my place to say. Watch %s" % (random.choice(disney_recomendations)))
      elif genre_movies in superhero_response :
        superhero_recommendation = ["Wonder Woman (SOOOOOOO GOOD)", "ALL THE MARVEL MOVIES. EVERY. SINGLE. ONE. YOU MAY THINK I'M KIDDING. I'M NOT", "Spiderman: Into the Spiderverse (Hilarious 11/10 would recommend)", "Shazam (Just so amazing, and hilarious and Zachery Levi and Dave from Gilmore Girls and amazing)"]
        print ("Superhero movies are great. Just remember MARVEL IS BOSS. Watch %s. Go. go." % (random.choice(superhero_recommendation)))
      else :
        print "I gave extremely clear instructions. Why would you enter something else? Unless you entered T.V., then watch Gilmore Girl. Coffee. Quick wit. Love. It's a masterpiece."
      break    
  response = raw_input("That's not what we're here for. Can I recommend a book or movie for you? Try again. ")

  

