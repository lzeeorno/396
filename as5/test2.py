import subEval,simpleSubHacker
ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
input_files = ["alpha_cipher","beta_cipher","gamma_cipher","delta_cipher","epsilon_cipher"]


for input_file in input_files:
    output_file = input_file.replace("cipher","decipher")
    plantext_file = input_file.replace("cipher","plain")

    simpleSubHacker.w

    compare = subEval.evalFile(output_file,plantext_file)

    print(compare)
