def analisar_lexico(expressao):
    estado = 'INICIAL'
    tokens = []
    buffer = ''
    i = 0
    erro = False
    
    while i < len(expressao):
        char = expressao[i]
        
        if estado == 'INICIAL':
            if char.isdigit():
                estado = 'NUM_INT'
                buffer += char
            elif char in '+-*/':
                tokens.append(('OPERADOR', char))
            elif char == '(':
                tokens.append(('ABRE_PAR', char))
            elif char == ')':
                tokens.append(('FECHA_PAR', char))
            elif char.isspace():
                pass  
            else:
                tokens.append(('ERRO', char))
                erro = True
        
        elif estado == 'NUM_INT':
            if char.isdigit():
                buffer += char
            elif char == '.':
                estado = 'NUM_REAL'
                buffer += char
            elif char in 'eE':
                estado = 'EXP'
                buffer += char
            else:
                tokens.append(('NUM_INT', buffer))
                buffer = ''
                estado = 'INICIAL'
                continue  
        
        elif estado == 'NUM_REAL':
            if char.isdigit():
                buffer += char
            elif char in 'eE':
                estado = 'EXP'
                buffer += char
            else:
                tokens.append(('NUM_REAL', buffer))
                buffer = ''
                estado = 'INICIAL'
                continue  
        
        elif estado == 'EXP':
            if char.isdigit() or char in '+-':
                buffer += char
                estado = 'EXP_DIG'
            else:
                tokens.append(('ERRO', buffer))
                erro = True
                buffer = ''
                estado = 'INICIAL'
                continue
        
        elif estado == 'EXP_DIG':
            if char.isdigit():
                buffer += char
            else:
                tokens.append(('NUM_REAL', buffer))
                buffer = ''
                estado = 'INICIAL'
                continue  
        
        i += 1
    
    if buffer:
        if estado in ('NUM_INT', 'NUM_REAL', 'EXP_DIG'):
            tokens.append(('NUM_REAL' if '.' in buffer or 'E' in buffer or 'e' in buffer else 'NUM_INT', buffer))
        else:
            tokens.append(('ERRO', buffer))
            erro = True
    
    if erro:
        print(f"Erro lexico na expressao: {expressao}")
    
    return tokens


expressao = "(10E9i)*6.7+98842942.42342E12" # Coloque a formula aqui
tokens = analisar_lexico(expressao)
for token in tokens:
    print(token)
