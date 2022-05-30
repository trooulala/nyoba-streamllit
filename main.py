import streamlit as st
import string

st.write(
    """
    # Lexical Analyzer dan Parser Sederhana untuk Teks Bahasa Alami

    Selamat datang, silahkan lakukan chek validasi kata dengan menginputkan kata yang ada dalam daftar.
    Berikut adalah daftar kata yang bisa dichek pada lexical analyzer ini:
    kulo, sampeyan, dheweke, awakdhewe, saged, budhal, gawe, saiki
    """
)

kalimat = st.text_input('masukkan kalimat:')
st.write('kaimat yang anda masukkan: ', kalimat)
input_string = kalimat.lower() + '#'

state_list = [
    'q0','q1','q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14',
    'q15', 'q16','q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 
    'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q40'
]

transition_table = {}

alphabet_list = list(string.ascii_lowercase)
for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

# #spaces before input string
transition_table['q0', ' ']='q0'

#update the transition table for the following token: kulo
transition_table[('q0', 'k')]= 'q30'
transition_table[('q30', 'u')]= 'q31'
transition_table[('q31', 'l')]= 'q32'
transition_table[('q32', 'o')]= 'q33'
transition_table[('q33', ' ')]= 'q34'
transition_table[('q33', '#')]= 'accept'
transition_table[('q34', ' ')]= 'q34'
transition_table[('q34', '#')]= 'accept'

#transation for new token
transition_table[('q34', 's')]= 'q1'
transition_table[('q34', 'b')]= 'q11'
transition_table[('q34', 'p')]= 'q35'
transition_table[('q34', 'd')]= 'q16'
transition_table[('q34', 'a')]= 'q22'
transition_table[('q34', 'g')]= 'q29'
transition_table[('q34', 'k')]= 'q30'


#update the transition table for the following token: sampeyan
transition_table[('q0', 's')]= 'q1'
transition_table[('q1', 'a')]= 'q2'
transition_table[('q2', 'm')]= 'q3'
transition_table[('q3', 'p')]= 'q4'
transition_table[('q4', 'e')]= 'q5'
transition_table[('q5', 'y')]= 'q6'
transition_table[('q6', 'a')]= 'q7'
transition_table[('q7', 'n')]= 'q33'

#update the transition table for the following token: gawe
transition_table[('q0', 'g')]= 'q30'
transition_table[('q30', 'a')]= 'q31'
transition_table[('q31', 'w')]= 'q32'
transition_table[('q32', 'e')]= 'q33'


#update the transition table for the following token: budhal
transition_table[('q0', 'b')]= 'q11'
transition_table[('q11', 'u')]= 'q12'
transition_table[('q12', 'd')]= 'q13'
transition_table[('q13', 'h')]= 'q14'
transition_table[('q14', 'a')]= 'q15'
transition_table[('q15', 'l')]= 'q33'


#update the transition table for the following token: saged
transition_table[('q0', 's')]= 'q1'
transition_table[('q1', 'a')]= 'q2'
transition_table[('q2', 'g')]= 'q8'
transition_table[('q8', 'e')]= 'q9'
transition_table[('q9', 'd')]= 'q33'

#update the transition table for the following token: saiki
transition_table[('q0', 's')]= 'q1'
transition_table[('q1', 'a')]= 'q2'
transition_table[('q2', 'i')]= 'q9'
transition_table[('q9', 'k')]= 'q10'
transition_table[('q10', 'i')]= 'q33'

#update the transition table for the following token: pasar
transition_table[('q0', 'p')]= 'q35'
transition_table[('q35', 'a')]= 'q36'
transition_table[('q36', 's')]= 'q37'
transition_table[('q37', 'a')]= 'q38'
transition_table[('q38', 'r')]= 'q33'

#update the transition table for the following token: sawah
transition_table[('q0', 's')]= 'q1'
transition_table[('q1', 'a')]= 'q2'
transition_table[('q2', 'w')]= 'q39'
transition_table[('q39', 'a')]= 'q40'
transition_table[('q40', 'h')]= 'q33'

#update the transition table for the following token: awakdhewe
transition_table[('q0', 'a')]= 'q22'
transition_table[('q22', 'w')]= 'q23'
transition_table[('q23', 'a')]= 'q24'
transition_table[('q24', 'k')]= 'q25'
transition_table[('q25', 'd')]= 'q26'
transition_table[('q26', 'h')]= 'q27'
transition_table[('q27', 'e')]= 'q28'
transition_table[('q28', 'w')]= 'q21'
transition_table[('q21', 'e')]= 'q33'

#update the transition table for the following token: dheweke
transition_table[('q0', 'd')]= 'q16'
transition_table[('q16', 'h')]= 'q17'
transition_table[('q17', 'e')]= 'q18'
transition_table[('q18', 'w')]= 'q19'
transition_table[('q19', 'e')]= 'q20'
transition_table[('q20', 'k')]= 'q21'
transition_table[('q21', 'e')]= 'q33'




# #update the transition table for the following token: ich
# transition_table[('q0', 'i')]= 'q1'
# transition_table[('q1', 'c')]= 'q2'
# transition_table[('q2', 'h')]= 'q40'
# transition_table[('q40', ' ')]= 'q41'
# transition_table[('q40', '#')]= 'accept'
# transition_table[('q41', ' ')]= 'q41'
# transition_table[('q41', '#')]= 'accept'

# #transation for new token
# transition_table[('q41', 'i')]= 'q1'
# transition_table[('q41', 'e')]= 'q19'
# transition_table[('q41', 'm')]= 'q9'
# transition_table[('q41', 'd')]= 'q3'
# transition_table[('q41', 't')]= 'q30'
# transition_table[('q41', 'p')]= 'q4'
# transition_table[('q41', 'k')]= 'q24'
# transition_table[('q41', 's')]= 'q12'
# transition_table[('q41', 'n')]= 'q35'

# #update the transition table for the following token: du
# transition_table[('q0', 'd')]= 'q3'
# transition_table[('q3', 'u')]= 'q40'

# #update the transition table for the following token: trinke
# transition_table[('q0', 't')]= 'q30'
# transition_table[('q30', 'r')]= 'q31'
# transition_table[('q31', 'i')]= 'q32'
# transition_table[('q32', 'n')]= 'q33'
# transition_table[('q33', 'k')]= 'q18'
# transition_table[('q18', 'e')]= 'q40'

# #update the transition table for the following token: tragen
# transition_table[('q31', 'a')]= 'q34'
# transition_table[('q34', 'g')]= 'q37'

# #update the transition table for the following token: physik
# transition_table[('q0', 'p')]= 'q4'
# transition_table[('q4', 'h')]= 'q5'
# transition_table[('q5', 'y')]= 'q6'
# transition_table[('q6', 's')]= 'q7'
# transition_table[('q7', 'i')]= 'q8'
# transition_table[('q8', 'k')]= 'q40'

# #update the transition table for the following token: saft
# transition_table[('q0', 's')]= 'q12'
# transition_table[('q12', 'a')]= 'q13'
# transition_table[('q13', 'f')]= 'q14'
# transition_table[('q14', 't')]= 'q40'

# #update the transition table for the following token: studie
# transition_table[('q12', 't')]= 'q15'
# transition_table[('q15', 'u')]= 'q16'
# transition_table[('q16', 'd')]= 'q17'
# transition_table[('q17', 'i')]= 'q18'
# transition_table[('q18', 'e')]= 'q40'

# #update the transition table for the following token: nahen
# transition_table[('q0', 'n')]= 'q35'
# transition_table[('q35', 'a')]= 'q36'
# transition_table[('q36', 'h')]= 'q37'
# transition_table[('q37', 'e')]= 'q38'
# transition_table[('q38', 'n')]= 'q40'

# #update the transition table for the following token: kleider
# transition_table[('q0', 'k')]= 'q24'
# transition_table[('q24', 'l')]= 'q25'
# transition_table[('q25', 'e')]= 'q26'
# transition_table[('q26', 'i')]= 'q27'
# transition_table[('q27', 'd')]= 'q28'
# transition_table[('q28', 'e')]= 'q29'
# transition_table[('q29', 'r')]= 'q40'

# #update the transition table for the following token: koche
# transition_table[('q24', 'o')]= 'q22'
# transition_table[('q22', 'c')]= 'q23'
# transition_table[('q23', 'h')]= 'q18'
# transition_table[('q18', 'e')]= 'q40'

# #update the transition table for the following token: ernte
# transition_table[('q0', 'e')]= 'q19'
# transition_table[('q19', 'r')]= 'q20'
# transition_table[('q20', 'n')]= 'q21'
# transition_table[('q21', 't')]= 'q18'

# #update the transition table for the following token: mais
# transition_table[('q0', 'm')]= 'q9'
# transition_table[('q9', 'a')]= 'q10'
# transition_table[('q10', 'i')]= 'q11'
# transition_table[('q11', 's')]= 'q40'

# #lexical analysis
# idx_char = 0
# state = 'q0'
# current_token = ' '
# while state!='accept':
#   current_char = input_string[idx_char]
#   current_token += current_char
#   state = transition_table[(state, current_char)]
#   if state=='q40':
#     print('current token: ', current_token, ', valid')
#     current_token =' '
#   if state == 'error':
#     print('current token: ', current_token, ', error')
#     print('Maaf, kata yang anda masukan tidak valid')
#     print('Silahkan periksa kembali kata yang anda masukan')
#     break;
#   idx_char = idx_char + 1

# #conclusion
# if state == 'accept':
#   print('semua token di input: ', sentence, ', valid')

# #PARSER GRAMMAR CHEKER
# #input example
# #x = input()
# #x = str(x)
# #sentence = x
# print()
# print('-----------------------------------------------------------------------------------------------------')
# print('Chek validasi kata dengan analyzer lexical telah selesai')
# print('Selanjutnya akan dichek aturan grammarnya')
# print('-----------------------------------------------------------------------------------------------------')
# tokens = sentence.lower().split()
# tokens.append('EOS')

# #symbols definition
# non_terminals = ['S', 'SB', 'VB', 'OB']
# terminals = ['ich', 'du', 'kleider', 'physik', 'saft', 'mais', 'studie', 'trinke', 'ernte', 'koche', 'nahen', 'tragen']

# #parse table definition
# parse_table = {}

# parse_table[('S', 'ich')] = ['SB', 'VB', 'OB']
# parse_table[('S', 'du')] = ['SB', 'VB', 'OB']
# parse_table[('S', 'kleider')] = ['error']
# parse_table[('S', 'physik')] = ['error']
# parse_table[('S', 'saft')] = ['error']
# parse_table[('S', 'mais')] = ['error']
# parse_table[('S', 'studie')] = ['error']
# parse_table[('S', 'trinke')] = ['error']
# parse_table[('S', 'ernte')] = ['error']
# parse_table[('S', 'koche')] = ['error']
# parse_table[('S', 'nahen')] = ['error']
# parse_table[('S', 'tragen')] = ['error']
# parse_table[('S', 'EOS')] = ['error']

# parse_table[('SB', 'ich')] = ['ich']
# parse_table[('SB', 'du')] = ['du']
# parse_table[('SB', 'kleider')] = ['error']
# parse_table[('SB', 'physik')] = ['error']
# parse_table[('SB', 'saft')] = ['error']
# parse_table[('SB', 'mais')] = ['error']
# parse_table[('SB', 'studie')] = ['error']
# parse_table[('SB', 'trinke')] = ['error']
# parse_table[('SB', 'ernte')] = ['error']
# parse_table[('SB', 'koche')] = ['error']
# parse_table[('SB', 'nahen')] = ['error']
# parse_table[('SB', 'tragen')] = ['error']
# parse_table[('SB', 'EOS')] = ['error']

# parse_table[('VB', 'ich')] = ['error']
# parse_table[('VB', 'du')] = ['error']
# parse_table[('VB', 'kleider')] = ['error']
# parse_table[('VB', 'physik')] = ['error']
# parse_table[('VB', 'saft')] = ['error']
# parse_table[('VB', 'mais')] = ['error']
# parse_table[('VB', 'studie')] = ['studie']
# parse_table[('VB', 'trinke')] = ['trinke']
# parse_table[('VB', 'ernte')] = ['ernte']
# parse_table[('VB', 'koche')] = ['koche']
# parse_table[('VB', 'nahen')] = ['nahen']
# parse_table[('VB', 'tragen')] = ['tragen']
# parse_table[('VB', 'EOS')] = ['error']

# parse_table[('OB', 'ich')] = ['error']
# parse_table[('OB', 'du')] = ['error']
# parse_table[('OB', 'kleider')] = ['kleider']
# parse_table[('OB', 'physik')] = ['physik']
# parse_table[('OB', 'saft')] = ['saft']
# parse_table[('OB', 'mais')] = ['mais']
# parse_table[('OB', 'studie')] = ['error']
# parse_table[('OB', 'trinke')] = ['error']
# parse_table[('OB', 'ernte')] = ['error']
# parse_table[('OB', 'koche')] = ['error']
# parse_table[('OB', 'nahen')] = ['error']
# parse_table[('OB', 'tragen')] = ['error']
# parse_table[('OB', 'EOS')] = ['error']

# #stack initialization
# stack = []
# stack.append('#')
# stack.append('S')

# #input reading initialization
# idx_token = 0
# symbol = tokens[idx_token]

# #parsing process
# try :
#   while (len(stack) > 0):
#     top = stack[len(stack)-1]
#     print('top = ', top)
#     print('symbol = ', symbol)
#     if top in terminals:
#       print('top adalah simbol terminal')
#       if top==symbol:
#         stack.pop()
#         idx_token = idx_token + 1
#         symbol = tokens[idx_token]
#         if symbol == 'EOS':
#           print('isi stack: ', stack)
#           stack.pop()
#       else:
#         print('error')
#         break;
#     elif top in non_terminals:
#       print('top adalah simbol non-terminal')
#       if parse_table[(top, symbol)][0] != 'error':
#         stack.pop()
#         symbols_to_be_pushed = parse_table[(top, symbol)]
#         for i in range(len(symbols_to_be_pushed)-1,-1,-1):
#           stack.append(symbols_to_be_pushed[i])
#       else:
#         print('error')
#         break;
#     else:
#       print('error')
#       break;
#     print('isi stack: ', stack)
#     print()
# except KeyError :
#     print('Kata tidak ditemukan dalam sistem')

# #conclusion
# print()
# if symbol == 'EOS' and len(stack) == 0:
#   print('-----------------------------------------------------------------------------------------------------')
#   print('Input string: ', sentence)
#   print('Selamat!!!')
#   print('Kalimat yang anda masukan diterima, karna sesuai Grammar')
#   print('Terimakasih')
#   print('-----------------------------------------------------------------------------------------------------')
# else :
#   print('-----------------------------------------------------------------------------------------------------')
#   print('Error, input string: ', sentence)
#   print('Mohon Maaf')
#   print('Kalimat yang anda masukan tidak diterima, karna tidak sesuai Grammar')
#   print('atau terdapat kata yang tidak valid')
#   print('Silahkan chek kembali kalimat yang anda masukan')
#   print('Terimakasih')
#   print('-----------------------------------------------------------------------------------------------------')
