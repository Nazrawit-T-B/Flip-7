#Layout file for the card structure depending on the number of players
WIDTH=800
HEIGHT=800
CENTER_X=WIDTH//2
CENTER_Y=HEIGHT//2

LAYOUTS={
    2:{
        "players":[
            (400,700),
            (400,100)
        ],
        "deck":(CENTER_X, CENTER_Y),

    },
    3:{
        "players":[
            (400,700),
            (400,100),
            (120,400)
        ],
        "deck":(CENTER_X, CENTER_Y),    
    },
    4:{
        "players":[
            (400,700),
            (400,100),
            (120,400),
            (680,400)
        ],
        "deck":(CENTER_X, CENTER_Y),
    },
    5:{
        "players":[
            (400,700),
            (400,100),
            (120,250),
            (120,550),
            (680,400)
        ],
        "deck":(CENTER_X, CENTER_Y),
    },
    6:{
        "players":[
            (400,700),
            (400,100),
            (120,250),
            (120,550),
            (680,250),
            (680,550)
        ],
        "deck":(CENTER_X,CENTER_Y  )
    }
}