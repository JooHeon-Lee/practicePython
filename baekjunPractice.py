# print("|\\_/|");
# print("|q p|   /}");
# print("( 0 )\"\"\"\\");
# print("|\"^\"`    |");
# print("||_/=\\\\__|")

# \    /\
#  )  ( ')
# (  /  )
#  \(__)|

# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|
while 1:
    b = input()
    if b == 'EOI':break
    b = b.lower()
    if 'nemo' in b:
        print('Found')
    else: print('Missing')