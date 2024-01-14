import os
import pyaes
import glob

key = b'chavemuitosecreta'[:32].ljust(32, b'\0')

encrypted_files_pattern = '*.ransomwaretest'

encrypted_files_list = glob.glob(encrypted_files_pattern)

for encrypted_file in encrypted_files_list:
    try:
        with open(encrypted_file, 'rb') as file:
            file_data = file.read()

        os.remove(encrypted_file)

        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        output_file_name = encrypted_file[:-15]
        with open(output_file_name, 'wb') as output_file:
            output_file.write(decrypt_data)

    except Exception as e:
        print(f"Erro ao processar {encrypted_file}: {e}")

print("Processo de desencriptação concluído.")
