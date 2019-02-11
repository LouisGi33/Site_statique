import os

path = os.path.dirname(os.path.abspath(__file__))
listfiles = os.listdir(path)

for file in listfiles:
    if file[-3:] == ".md":
        txt = open(os.path.join(path, file), "r").read()

char = 0
baliseshtml = []
linked = 0
imglinked = 0
info = ""
verif = 0
html = open("test.html", "w+")
html.write("<html>\n")
html.write("<head>\n")
html.write('<meta charset="UTF-8"/>\n')
html.write('<title>Carapuce</title>\n')
html.write('</head>\n')
html.write('<body>\n')

while char < len(txt):
    
    balise = {"#", "-", "*", "~", "[", "]", "(", ")", "!", "h"}
    if txt[char] in balise:
        if txt[char] == "#" and (txt[char-1] == "\n" or char == 0):
            if txt[char+1] != "#":
                baliseshtml.append('<h1>')
                html.write("<h1>")
            elif txt[char+1] == "#" and txt[char+2] != "#":
                baliseshtml.append('<h2>')
                html.write("<h2>")
                char += 1
            elif txt[char+1] == "#" and txt[char+2] == "#":
                    baliseshtml.append('<h3>')
                    html.write("<h3>")
                    char += 2
        elif txt[char] == "#" and txt[char-1] != "\n" and txt[char-1] != "#" and char != 0:
            html.write("#")
                    
                
        elif txt[char] == "-":
            if txt[char+1] == "-" and txt[char+2] == "-":
                html.write("\n<hr>\n")
            else:
                html.write("-")
            
                    
        elif txt[char] == "*" and txt[char + 1] != ' ':
            CI = txt[char+1]
            if CI == "*":
                if len(baliseshtml) > 0:
                    if baliseshtml[-1] != '<strong>':
                        baliseshtml.append("<strong>")
                        html.write("<strong>")
                    else:
                        baliseshtml.remove('<strong>')
                        html.write('</strong>')
                else:
                    baliseshtml.append("<strong>")
                    html.write("<strong>")
                char += 1
            elif CI != "*":
                if len(baliseshtml) > 0:
                    if baliseshtml[-1] != '<em>':
                        baliseshtml.append("<em>")
                        html.write("<em>")
                    else:
                        baliseshtml.remove("<em>")
                        html.write('</em>')
                else:
                        baliseshtml.append("<em>")
                        html.write('<em>')
        elif txt[char] == "~":
            strike = txt[char+1]
            if strike == "~":
                if len(baliseshtml) > 0:
                    if baliseshtml[-1] != '<s>':
                        html.write("<s>")
                        baliseshtml.append('<s>')
                    else:
                        baliseshtml.remove('<s>')
                        html.write('</s>')
                else:
                    baliseshtml.append('<s>')
                    html.write('<s>')
        elif txt[char] == "h":
            html.write('h')
        #     if (txt[char] + txt[char+1] + txt[char+2] + txt[char+3] == "http" or txt[char-2] + txt[char-1] =="](") and verif == 0:
        #         # if txt[char+1] == "t":
        #         #     if txt[char+2] == "t":
        #         #         if txt[char+3] == "p":
        #         html.write('<a href="')
        #         baliseshtml.append('<a href"')
        #         html.write('h')
            # else:
            #     html.write('h')
        elif txt[char] == "!":
            if txt[char+1] != "[":
                html.write('!')
            elif txt[char+1] == "[":
                imglinked = 1
                html.write('<img src="')
                baliseshtml.append('<img src="')
        elif txt[char] == "[" and txt[char-1] != "!":
            linked = 1
            html.write('<a href="')
            baliseshtml.append('<a href="')
            verif = 1
            if txt[char] == "]":
                if txt[char+1] == "(":
                    pass
                else:
                    html.write(']')
            
        elif txt[char] == "(":
            linked = 0
                #if txt[char-1] == "]":
            #     pass
            # elif txt[char-1] != "]":
            #     html.write('(')
            #     print("1")
        elif txt[char] == ")":
            if baliseshtml[-1] == '<img src="':
                html.write('" alt="' + info + '" />')
                baliseshtml.remove('<img src="')
                imglinked = 0
                info = ""
                
            elif baliseshtml[-1] == '<a href="':
                html.write('">' + info + '</a>')
                baliseshtml.remove('<a href="')
                info = ""
                verif = 0
        

            
        
        elif txt[char] == "*" and txt[char + 1] == " ":
                if not "<ul>" in baliseshtml:
                    html.write("\n<ul>\n")
                    baliseshtml.append("<ul>")
                html.write("<li>")
                baliseshtml.append("<li>")
        
        
    





    elif txt[char] == '\n':
        if len(baliseshtml) > 0:
            if baliseshtml[-1] == '<h1>':
                html.write('</h1>\n')
                baliseshtml.remove('<h1>')
            elif baliseshtml[-1] == '<h2>':
                html.write('</h2>\n')
                baliseshtml.remove('<h2>')
            elif baliseshtml[-1] == '<h3>':
                html.write('</h3>\n')
                baliseshtml.remove('<h3>')


            
            elif baliseshtml[-1] == '<ul>':
                html.write('</ul>\n')
                baliseshtml.remove('<ul>')
            elif baliseshtml[-1] == '<li>':
                html.write('</li>\n')
                baliseshtml.remove('<li>')
            elif baliseshtml[-1] == '<s>':
                html.write('</s>\n')
                baliseshtml.remove('<s>')

            
        
            

    else:
        if linked == 1:
            info += txt[char]
        else:
            html.write(txt[char])
        
        

    char += 1

    