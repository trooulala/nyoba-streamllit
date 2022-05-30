import streamlit as st
import string

st.write(
    """
    # Lexical Analyzer dan Parser Sederhana untuk Teks Bahasa Alami

    Selamat datang, silahkan lakukan chek validasi kata dengan menginputkan kata yang ada dalam daftar.
    Berikut adalah daftar kata yang bisa dichek pada lexical analyzer ini:

    kulo, sampeyan, dheweke, awakdhewe, gawe, budhal, saged, saiki, pasar, sawah
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
transition_table[('q0', 'g')]= 'q29'
transition_table[('q29', 'a')]= 'q28'
transition_table[('q28', 'w')]= 'q21'
transition_table[('q21', 'e')]= 'q33'


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

#lexical analysis
idx_char = 0
state = 'q0'
current_token = ' '
while state!='accept':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    if state=='q34':
        st.write('current token: ', current_token, ', valid')
        current_token =''
    if state == 'error':
        st.write('current token: ', current_token, ', error')
        st.write('Maaf, kata yang anda masukan tidak valid')
        st.write('Silahkan periksa kembali kata yang anda masukan')
        break
    idx_char = idx_char + 1

#conclusi
if state == 'accept':
    st.write('semua token di input: ', kalimat, ', valid')

#PARSER GRAMMAR CHEKER
#input example
#x = input()
#x = str(x)
#sentence = x
print()
print('-----------------------------------------------------------------------------------------------------')
print(                    'Check validasi kata dengan analyzer lexical telah selesai                         ')
print('                           Selanjutnya akan dichek aturan grammarnya                                 ')
print('-----------------------------------------------------------------------------------------------------')
tokens = kalimat.lower().split()
tokens.append('EOS')

#symbols definition
non_terminals = ['S', 'NN', 'VB', 'OB']
terminals = ['kulo', 'sampeyan', 'awakhedewe', 'dheweke', 'gawe', 'budhal', 'saged', 'saiki', 'pasar', 'sawah', 'EOS']

#parse table definition
parse_table = {}

parse_table[('S', 'kulo')] = ['NN', 'VB', 'OB']
parse_table[('S', 'sampeyan')] = ['NN', 'VB', 'OB']
parse_table[('S', 'awakhedewe')] = ['NN', 'VB', 'OB']
parse_table[('S', 'dheweke')] = ['NN', 'VB', 'OB']
parse_table[('S', 'gawe')] = ['error']
parse_table[('S', 'budhal')] = ['error']
parse_table[('S', 'saged')] = ['error']
parse_table[('S', 'saiki')] = ['error']
parse_table[('S', 'pasar')] = ['error']
parse_table[('S', 'sawah')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'kulo')] = ['kulo']
parse_table[('NN', 'sampeyan')] = ['sampeyan']
parse_table[('NN', 'awakhedewe')] = ['error']
parse_table[('NN', 'dheweke')] = ['error']
parse_table[('NN', 'gawe')] = ['error']
parse_table[('NN', 'budhal')] = ['error']
parse_table[('NN', 'saged')] = ['error']
parse_table[('NN', 'saiki')] = ['error']
parse_table[('NN', 'pasar')] = ['error']
parse_table[('NN', 'sawah')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'kulo')] = ['error']
parse_table[('VB', 'sampeyan')] = ['error']
parse_table[('VB', 'awakhedewe')] = ['error']
parse_table[('VB', 'dheweke')] = ['error']
parse_table[('VB', 'gawe')] = ['gawe']
parse_table[('VB', 'budhal')] = ['budhal']
parse_table[('VB', 'saged')] = ['error']
parse_table[('VB', 'saiki')] = ['error']
parse_table[('VB', 'pasar')] = ['error']
parse_table[('VB', 'sawah')] = ['error']
parse_table[('VB', 'EOS')] = ['error']

parse_table[('OB', 'kulo')] = ['error'] 
parse_table[('OB', 'sampeyan')] = ['error']
parse_table[('OB', 'awakhedewe')] = ['error']
parse_table[('OB', 'dheweke')] = ['error']
parse_table[('OB', 'gawe')] = ['error']
parse_table[('OB', 'budhal')] = ['error']
parse_table[('OB', 'saged')] = ['error']
parse_table[('OB', 'saiki')] = ['saiki']
parse_table[('OB', 'pasar')] = ['pasar']
parse_table[('OB', 'sawah')] = ['sawah']
parse_table[('OB', 'EOS')] = ['error']

#stack initialization
stack = []
stack.append('#')
stack.append('S')

#input reading initialization
idx_token = 0
symbol = tokens[idx_token]

#parsing process
try :
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        st.write('top = ', top)
        st.write('symbol = ', symbol)
        if top in terminals:
            st.write('top adalah simbol terminal')
            if top==symbol:
                stack.pop()
                idx_token = idx_token + 1
                symbol = tokens[idx_token]
                if symbol == 'EOS':
                    st.write('isi stack: ', stack)
                    stack.pop()
            else:
                st.write('error')
                break
        elif top in non_terminals:
            st.write('top adalah simbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbols_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                    stack.append(symbols_to_be_pushed[i])
            else:
                st.write('error')
                break
        else:
            st.write('error')
            break
        st.write('isi stack: ', stack)
        st.write()
except KeyError :
    st.write('Kata tidak ditemukan dalam sistem')

#conclusion
st.write()
if symbol == 'EOS' and len(stack) == 0:
    st.write('-----------------------------------------------------------------------------------------------------')
    st.write('Input string: ', kalimat)
    st.write('Selamat!!!')
    st.write('Kalimat yang anda masukan diterima, karna sesuai Grammar')
    st.write('Terimakasih')
    st.write('-----------------------------------------------------------------------------------------------------')
else :
    st.write('-----------------------------------------------------------------------------------------------------')
    st.write('Error, input string: ', kalimat)
    st.write('Mohon Maaf')
    st.write('Kalimat yang anda masukan tidak diterima, karna tidak sesuai Grammar')
    st.write('atau terdapat kata yang tidak valid')
    st.write('Silahkan chek kembali kalimat yang anda masukan')
    st.write('Terimakasih')
    st.write('-----------------------------------------------------------------------------------------------------')
