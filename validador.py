import re
import sys

def validar_cartao(numero):
    """
    Valida e identifica o tipo de cartão de crédito.
    
    Args:
    numero (str): Número do cartão de crédito.
    
    Returns:
    str: Tipo do cartão de crédito ou 'Inválido' se o número não for válido.
    """
    numero = numero.replace(" ", "")
    
    # Expressões regulares para diferentes tipos de cartões
    patterns = {
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "Enroute": r"^(?:2014|2149)[0-9]{11}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Voyager": r"^8699[0-9]{11}$",
        "Hipercard": r"^(606282\d{10}(\d{3})?)|(3841\d{15})$",
        "Aura": r"^50[0-9]{14,17}$"
    }
    # Função para validar o número do cartão usando o algoritmo de Luhn
    def luhn_check(numero):
        total = 0
        reverse_digits = numero[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    if luhn_check(numero):
        for tipo, pattern in patterns.items():
            if re.match(pattern, numero):
                return tipo
    
    return "Inválido"

# Exemplo de uso
#numero_cartao = "4556 9116 7819 3706"
#tipo_cartao = validar_cartao(numero_cartao)
#print(f"O cartão {numero_cartao} é do tipo: {tipo_cartao}")

def main():
    if len(sys.argv) != 2:
        print("Uso: python validador.py <numero_cartao>")
        sys.exit(1)
    
    numero_cartao = sys.argv[1]
    tipo_cartao = validar_cartao(numero_cartao)
    print(f"O cartão {numero_cartao} é do tipo: {tipo_cartao}")

if __name__ == "__main__":
    main()