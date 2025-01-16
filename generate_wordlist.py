import string
from itertools import product

def get_user_choice():
    """
    Ask the user to choose between generating a wordlist for Vivo or Claro networks.
    Returns the user's choice as a string.
    """
    print("Choose the type of network to generate the wordlist for:")
    print("1 - Vivo")
    print("2 - Claro")
    choice = input("Enter 1 or 2: ")
    if choice not in ["1", "2"]:
        print("Invalid choice. Please try again.")
        return get_user_choice()  # Recursive call to ensure a valid input
    return choice

def get_adjusted_name_vivo():
    """
    Prompt the user for the MAC address of a Vivo network.
    Adjust and clean the MAC for further processing.
    """
    mac = input("Enter the network MAC (format XX:XX:XX:XX:XX:XX): ")
    # Extract a substring and remove colons
    adjusted_mac = mac[3:17].replace(":", "")
    print(f"Adjusted MAC (Vivo): {adjusted_mac}")
    return adjusted_mac

def get_adjusted_name_claro():
    """
    Prompt the user for the Claro network name.
    Extract the required part for wordlist generation.
    """
    name = input("Enter the Claro network name: ")
    # Extract the 8th to 14th characters (as per Claro's logic)
    adjusted_name = name[8:14]
    print(f"Adjusted Name (Claro): {adjusted_name}")
    return adjusted_name

def generate_wordlist_vivo(filename, adjusted_name, chars):
    """
    Generate a wordlist for Vivo networks.
    This includes combinations of two characters with the MAC (uppercase and lowercase).
    """
    with open(filename, "w") as file:
        # Add direct variations of the MAC
        file.write(f"{adjusted_name}\n")
        file.write(f"{adjusted_name.upper()}\n")
        file.write(f"{adjusted_name.lower()}\n")
        # Generate combinations: prefix (2 characters) + adjusted MAC
        for prefix in product(chars, repeat=2):
            prefix_str = ''.join(prefix)
            file.write(f"{prefix_str}{adjusted_name.upper()}\n")
            file.write(f"{prefix_str}{adjusted_name.lower()}\n")

    print(f"Wordlist generated: {filename}")

def generate_wordlist_claro(filename, adjusted_name, chars):
    """
    Generate a wordlist for Claro networks.
    This includes combinations of two characters with the adjusted name.
    """
    with open(filename, "w") as file:
        # Generate combinations: prefix (2 characters) + adjusted name
        for prefix in product(chars, repeat=2):
            prefix_str = ''.join(prefix)
            file.write(f"{prefix_str}{adjusted_name}\n")

    print(f"Wordlist generated: {filename}")

if __name__ == "__main__":
    # Define the allowed characters: letters (upper/lower) and digits
    chars = string.ascii_letters + string.digits

    # Ask the user to choose between Vivo or Claro
    user_choice = get_user_choice()

    if user_choice == "1":  # Vivo network logic
        adjusted_name = get_adjusted_name_vivo()  # Process the MAC address
        filename = "wordlist_vivo.txt"  # Output file for Vivo
        generate_wordlist_vivo(filename, adjusted_name, chars)

    elif user_choice == "2":  # Claro network logic
        adjusted_name = get_adjusted_name_claro()  # Process the network name
        filename = "wordlist_claro.txt"  # Output file for Claro
        generate_wordlist_claro(filename, adjusted_name, chars)
