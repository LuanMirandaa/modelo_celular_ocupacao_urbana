---

# 🧠 Simulação de Fluxo de Pessoas com Autômatos Celulares

Este repositório apresenta uma **simulação computacional do fluxo de pessoas em um espaço público**, modelada por meio de **autômatos celulares**, inspirados no *Jogo da Vida* de Conway.
O projeto tem caráter **didático e exploratório**, demonstrando como regras locais simples podem gerar **padrões coletivos emergentes**.

---

## 📌 Descrição do Projeto

A praça pública é representada como uma **grade bidimensional**, onde cada célula pode assumir um dos seguintes estados:

* ⬜ **Espaço vazio**
* 🔴 **Pessoa**
* 🟩 **Obstáculo fixo** (árvores, bancos ou estruturas urbanas)

A dinâmica do sistema é regida por regras adaptadas do *Game of Life*, que representam comportamentos sociais básicos, como:

* dispersão por isolamento,
* evasão por superlotação,
* atração social para formação de grupos.

O resultado da simulação é visualizado por meio de uma **animação em GIF**, permitindo a análise visual da evolução temporal do sistema.

---

## 🎯 Objetivos

* Demonstrar o uso de **autômatos celulares** em simulações sociais;
* Explorar **comportamentos emergentes** em sistemas complexos;
* Servir como **ferramenta educacional** para disciplinas de simulação, sistemas complexos ou computação científica;
* Oferecer uma base para **extensões futuras**, como modelos mais realistas de dinâmica de multidões.

---

## ⚙️ Regras do Modelo

As regras são aplicadas considerando a **vizinhança de Moore** (8 vizinhos):

* **Isolamento:**
  Uma pessoa com menos de dois vizinhos abandona o espaço.
* **Superlotação:**
  Uma pessoa com mais de três vizinhos também abandona o espaço.
* **Atração social:**
  Um espaço vazio com exatamente três vizinhos passa a ser ocupado.
* **Obstáculos:**
  Permanecem fixos e não participam da dinâmica.

---

## 🧪 Tecnologias Utilizadas

* **Python 3**
* **NumPy** — manipulação de matrizes
* **Matplotlib** — visualização e animação
* **Pillow** — exportação do GIF

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/LuanMirandaa/modelo_celular_ocupacao_urbana.git

```

2. Instale as dependências:

```bash
pip install numpy matplotlib pillow
```

3. Execute o script:

```bash
python simulacao.py
```

4. O arquivo `simulacao_ocupacao_praca.gif` será gerado no diretório do projeto.

---

## 📊 Exemplo de Saída

A simulação gera uma animação mostrando:

* surgimento e desaparecimento de grupos,
* influência dos obstáculos na ocupação do espaço,
* padrões estáveis ou oscilatórios ao longo do tempo.

*(GIF gerado automaticamente pelo código)*
