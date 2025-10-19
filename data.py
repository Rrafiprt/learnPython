from band import vokalis
from band import gitaris
from band import bassist1
from band import bassist2
from band import drummer
from band import keyboardist

class DataLoader:
    def load_band(self):
        return [
            vokalis("Andir"),
            gitaris("Rafi"),
            bassist1("Ahsan"),
            bassist2("Alfariz"),
            drummer("Fadel"),
            keyboardist("Kevin")
        ]
