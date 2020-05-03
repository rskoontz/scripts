#!/usr/bin/env python3

def remove_the_key():
    input_file = "juniper.log"
    output_file = "juniper_clean.log"
    remove_list = ["ssh-rsa", "ssh-ecdsa"]
    fin = open(input_file)
    fout = open(output_file, "w+")

    for line in fin:
        for word in remove_list:
            line = line.replace(word, "")
        fout.write(line)
    fin.close()
    fout.close()




if __name__ == "__main__":
    remove_the_key()
