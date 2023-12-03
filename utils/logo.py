import os
import fade

_LOGO_ = """                                                


                      |))    |))
        .             |  )) /   ))
        \\   ^ ^      |    /      ))
         \\(((  )))   |   /        ))
          / G    )))  |  /        ))
         |o  _)   ))) | /       )))
          --' |     ))`/      )))
           ___|              )))
          / __\             ))))`()))
         /\@   /             `(())))
         \/   /  /`_______/\   \  ))))
              | |          \ \  |  )))
              | |           | | |   )))
              |_@           |_|_@    ))
             /_/           /_/_/
       Imhunterand BLU3C0RN (imhunterand@cyberservices.com)
"""

def print_logo():
    os.system("clear||cls")
    faded_logo = fade.water(_LOGO_)
    print(faded_logo)

if __name__ == "__main__":
    logo()
    



