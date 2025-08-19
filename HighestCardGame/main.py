"""
Gana el jugador de la carta más grande:
Hay 2 jugadores.
Cada uno tiene un juego stándar de 52 cartas.
En cada turno, ambos jugadores muestran una carta.
El ganador del turno es quien tenga la carta más grande y se lleva la carta del otro jugador.
Si hay empates, se sacan cartas de nuevo hasta desempatar, el ganador del desempate se lleva todas las cartas lanzadas hasta el momento.
El juego se acaba cuando un jugador se queda con las 104 cartas.
¿Cuántos turnos tarda en terminar el juego?
"""

import random


class Card:
    suits = ["♥", "♠", "♣", "♦"]
    ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    def __init__(self, suit, rank):
        if suit not in self.suits:
            raise ValueError(f"El símbolo debe ser uno de: {self.suits}")

        if rank not in self.ranks:
            raise ValueError(f"El numero debe ser entre {self.ranks}")

        self.suit = suit
        self.rank = rank

    def getCard(self):
        return f"{self.suit}{self.rank}"

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return f"Card({self.suit}, {self.rank})"

    def get_numeric_value(self):
        """Retorna el valor numérico de la carta para comparaciones"""
        if self.rank == "A":
            return 1
        elif self.rank == "J":
            return 11
        elif self.rank == "Q":
            return 12
        elif self.rank == "K":
            return 13
        else:
            return self.rank


class Deck:
    cards = []

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        self.suffle()

    def get(self):
        return self.cards

    def suffle(self):
        random.shuffle(self.cards)

    def popCard(self):
        return self.cards.pop()

    def pushCard(self, card: Card):
        if isinstance(card, list):
            for c in card:
                self.cards.insert(0, c)
        else:
            self.cards.insert(0, card)


class Player:
    _id = None
    deck = None

    def __init__(self, id):
        self._id = id
        self.deck = Deck()

    def showCard(self):
        return self.deck.popCard()

    def pushCards(self, cards: Card):
        self.deck.pushCard(cards)

    def getCards(self):
        return self.deck.cards

    def __str__(self):
        return f"{self._id}: {len(self.getCards())} cards"

    def __repr__(self):
        return f"Player({self._id}: {len(self.getCards())} cards)"


class Game:
    players: list[Player] = []
    round = 0

    def __init__(self, players: list[Player]) -> None:
        self.players = players

    def runRound(self):
        self.round += 1

        # Encontrar el jugador con la carta de mayor rank
        cards_in_table = []
        while True:
            for player in self.players:
                if len(player.getCards()) == 0:
                    break
                cards_in_table.append({"player": player, "card": player.showCard()})

            max_rank = max(
                card_info["card"].get_numeric_value() for card_info in cards_in_table
            )

            winners = [
                card_info
                for card_info in cards_in_table
                if card_info["card"].get_numeric_value() == max_rank
            ]

            print("Winners: ", winners)
            print("Cards in table: ", cards_in_table)

            if len(winners) == 1:
                # Solo hay un ganador
                winner = winners[0]
                player: Player = winner.get("player")
                cards = [round.get("card") for round in cards_in_table]
                player.pushCards(cards)
                print("🏆 Round Winner 🏆: ", player)
                break

    def run(self):
        try:
            winner: Player = None
            while all(len(player.getCards()) > 0 for player in self.players):
                self.runRound()
                print("Ronda: ", self.round)
                for player in self.players:
                    if len(player.getCards()) == 104:
                        winner = player
                        break

            print("\n" + "🎊" * 20)
            print("🏆" * 5 + " ¡TENEMOS UN GANADOR! " + "🏆" * 5)
            print("🎊" * 20)
            print()
            print(f"🎉 ¡FELICIDADES {winner._id.upper()}! 🎉")
            print(f"🃏 Has conquistado todas las {len(winner.getCards())} cartas!")
            print(f"🏁 El juego terminó después de {self.round} rondas épicas!")
            print()
            print("🌟 ¡Eres el maestro supremo de las cartas! 🌟")
            print("=" * 50)
        except KeyboardInterrupt:
            print()
            print(f"⏹️ Juego interrumpido por el usuario despues de {self.round} rondas")
            print()
            print(f"{self.players}")
            print("👋 ¡Gracias por jugar!")
        except Exception as e:
            print(f"\n💥 Error crítico en el juego: {e}")
            print("🔄 Por favor, reinicia el juego")
            print("📝 Si el problema persiste, revisa la configuración del juego")


if __name__ == "__main__":
    player_1 = Player("Camilo")
    player_2 = Player("Daniel")
    game = Game([player_1, player_2])
    game.run()
