# 1️⃣ Faça um Fork do Repositório

Antes de começar a fazer qualquer alteração, você precisa criar um fork do repositório original. Isso criará uma cópia dele na sua conta do GitHub.

- Acesse o repositório
- No canto superior direito, clique no botão "Fork".
- Agora, você terá uma cópia do repositório na sua conta.

# 2️⃣ Clone o Repositório para sua Máquina

Agora, você precisa clonar o repositório forkado para o seu computador. No terminal ou Git Bash, rode o comando:
```ssh
git clone https://github.com/SEU-USUARIO/simulador-rescisao-python.git
```

# 3️⃣ Acesse o Diretório do Projeto

Entre na pasta do projeto clonado:
```ssh
cd simulador-rescisao-python
```

# 4️⃣ Crie uma Nova Branch para sua Modificação

Para manter o histórico do repositório organizado, nunca trabalhe na branch main.
Crie uma nova branch com um nome descritivo:

```ssh
git checkout -b feature/nome-da-sua-mudanca

Exemplo
git checkout -b feature/melhoria-interface
```

# 5️⃣ Instale as Dependências

Antes de rodar a aplicação localmente, instale as dependências:
```ssh
pip install -r requirements.txt
```

Caso ainda não tenha criado um ambiente virtual:
```ssh
python -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate  # No Windows
```

# 6️⃣ Faça as Modificações no Código

Agora, você pode editar o código e adicionar sua contribuição. 
Se estiver corrigindo um bug ou adicionando uma nova funcionalidade, siga boas práticas como:

Escrever código limpo e legível<br>
Testar suas mudanças localmente<br>
Evitar alterações desnecessárias<br>

Para rodar a aplicação localmente:
```ssh
python app.py
```
Acesse no navegador: http://127.0.0.1:5000

# 7️⃣ Confirme suas Alterações

Antes de enviar as mudanças, veja os arquivos modificados:
```ssh
git status
```

Adicione os arquivos alterados:
```ssh
git add .
```
Crie um commit explicando a mudança:
```ssh
git commit -m "feat: melhoria na interface do formulário"
```

# 8️⃣ Envie as Alterações para o Seu Fork

Agora, faça o push para o seu repositório:
```ssh
git push origin feature/nome-da-sua-mudanca
```

# 9️⃣ Crie um Pull Request

Agora que suas mudanças estão no GitHub, você precisa solicitar que elas sejam adicionadas ao repositório original.

Acesse seu repositório no GitHub.<br>
Clique na aba "Pull Requests".<br
Clique em "New Pull Request".
Escolha a branch main do repositório original e sua branch modificada.
Escreva um título e uma descrição explicando suas mudanças.
Clique em "Create Pull Request".
