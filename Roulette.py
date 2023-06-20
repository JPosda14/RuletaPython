import random

def spin_roulette():
    options = ['Rojo', 'Negro', 'Verde']
    result = random.choice(options)
    return result

def get_bet_amount(balance):
    while True:
        bet = input(f"Ingrese la cantidad de plata de su apuesta (saldo actual: ${balance}): ")
        if bet.isdigit():
            bet = int(bet)
            if 1 <= bet <= balance:
                return bet
            else:
                print("Cantidad de plata de apuesta inválida. Intente otra vez.")
        else:
            print("Cantidad de palta apuesta inválida. Intente otra vez.")

def get_bet_option():
    while True:
        print("Opciones de apuesta:")
        print("1. Rojo")
        print("2. Negro")
        print("3. Verde")
        option = input("Seleccione el número de su opción de color para la apuesta: ")
        if option.isdigit():
            option = int(option)
            if 1 <= option <= 3:
                return option
            else:
                print("Opción inválida. Intente otra vez.")
        else:
            print("Opción inválida. Intente otra vez.")

def calculate_payout(bet, bet_option, result):
    if bet_option == 1 and result == 'Rojo':
        return bet * 2
    elif bet_option == 2 and result == 'Negro':
        return bet * 2
    elif bet_option == 3 and result == 'Verde':
        return bet * 10
    else:
        return -bet

def main():
    print("Bienvenido a la ruleta MiNacional")

    balance = 100000
    while balance > 0:
        print(f"\nSaldo actual: ${balance}")

        bet = get_bet_amount(balance)
        bet_option = get_bet_option()

        result = spin_roulette()
        print("La bola cayó en:", result)

        payout = calculate_payout(bet, bet_option, result)
        balance += payout

        if payout > 0:
            print("Bueeenaaaa, Ganaste la apuesta.")
        else:
            print("Aghhh paila, perdiste la apuesta.")

        if balance <= 0:
            print("\nNo tienes saldo para seguir jugando. ¡Hasta luego!")
            break

        play_again = input("\n¿Deseas seguir jugando? (s/n): ")
        if play_again.lower() != 's':
            break

    print("\nGracias por jugar. Chao nos vemos")

if __name__ == "__main__":
    main()
