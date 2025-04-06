import argparse
import sys
import base64



def option_select():
    input_data = ""
    parser = argparse.ArgumentParser(description="base64 decoder")
    parser.add_argument('-f', '--file', type=str)
    parser.add_argument('-s', '--string', type=str)

    args = parser.parse_args()

    if args.file:
        print(f"File selected: {args.file}")
        with open(args.file, 'r') as file_object:
            data = ''.join(line.strip() for line in file_object)
            input_data += data

    if args.string:
        print(f"String Selected: {args.string} \n")
        input_data += args.string

    return input_data

def is_base64(enc_string):
    try:
        base64.b64decode(enc_string, validate=True)
        
        return True
    except Exception:
    
        return False


def decode_data(enc_data):
    while is_base64(enc_data):
        try:
            data = base64.b64decode(enc_data).decode('utf-8', errors='strict')
            data = ''.join(line.strip() for line in data)
            enc_data = data
            print(f"[+] Decoded Data: {enc_data} \n")

        except Exception as e:
            print("[-] Failed to decode any further", e)
            break
    
    return enc_data


if __name__ == "__main__":
    data = option_select()
    final_data = decode_data(data)
    print(f"[!!] Fully Decoded Data: {final_data} \n")
    