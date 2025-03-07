### **1. Convenções da Linguagem**

### **Aceita espaços entre operandos e operadores?**

**Sim**, espaços em branco devem ser ignorados, pois não afetam a interpretação dos tokens.

Exemplo:

- `"10 + 5"` deve ser tratado da mesma forma que `"10+5"`

### **Qual o alfabeto?**

O conjunto de caracteres aceitos inclui:

- **Dígitos**: `0-9` (para números inteiros e reais)
- **Ponto decimal**: `.` (para números reais, como `3.14`)
- **Expoente**: `E` ou `e` (para notação científica, como `10E4`)
- **Operadores matemáticos**: `+`, `-`, `*`, `/`
- **Parênteses**: `(` e `)`
- **Espaços em branco**: Devem ser ignorados
- **Qualquer outro caractere será um erro**

---

### **2. Erros possíveis**

Os erros ocorrem quando encontramos caracteres ou combinações inválidas:

#### **Caracteres desconhecidos**

- Exemplo: `10 + 5A` → O `A` é inválido

#### **Números malformados**

- Exemplo: `10..5` → Ponto decimal duplicado
- Exemplo: `5E` → Falta um número após o `E`

#### **Sequências inválidas**

- Exemplo: `++5` → Dois operadores seguidos sem um número

Quando um erro é encontrado, a expressão completa é exibida para facilitar a depuração.

