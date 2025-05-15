import re  # Importing the 're' module for regular expressions
import sys  # Importing 'sys' to use 'sys.exit()' for program termination

# Ask the user to input a CPF in the format '746.824.890-70'
entrada = input('CPF [746.824.890-70]: ')

# Remove non-numeric characters (dots, dashes, spaces) from the input CPF
cpf_enviado_usuario = re.sub(
    r'[^0-9]',  # Regular expression that matches anything that is not a digit
    '',         # Replace those characters with an empty string
    entrada     # The user-provided CPF
)

# Check if the CPF has all identical digits (e.g., "111.111.111-11")
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

# If CPF is sequential (same digits), exit the program
if entrada_e_sequencial:
    print('You entered sequential data.')  # Inform user that the CPF is invalid
    sys.exit()  # Exit the program

# Extract the first 9 digits of the CPF to start calculating the check digits
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10  # Start the first check digit calculation with weight 10

# Calculate the first check digit
resultado_digito_1 = 0  # Variable to accumulate the weighted sum
for digito in nove_digitos:  # Iterate through the first 9 digits
    resultado_digito_1 += int(digito) * contador_regressivo_1  # Weighted sum
    contador_regressivo_1 -= 1  # Decrease the weight (from 10 to 9, 9 to 8, etc.)

# Calculate the first check digit using the formula: (sum * 10) % 11
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0  # If the result is > 9, set to 0

# Add the first check digit to the 9 digits and calculate the second check digit
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11  # Start the second check digit calculation with weight 11

# Calculate the second check digit
resultado_digito_2 = 0  # Variable to accumulate the weighted sum for the second digit
for digito in dez_digitos:  # Iterate through the first 10 digits
    resultado_digito_2 += int(digito) * contador_regressivo_2  # Weighted sum
    contador_regressivo_2 -= 1  # Decrease the weight (from 11 to 10, 10 to 9, etc.)

# Calculate the second check digit using the formula: (sum * 10) % 11
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0  # If the result is > 9, set to 0

# Generate the complete CPF with the calculated check digits
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# Compare the input CPF with the generated CPF to check validity
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} is valid')  # If valid, print success message
else:
    print('Invalid CPF')  # If invalid, print error message
