# 🪵 learning_logging

Repositório de estudos sobre o módulo `logging` do Python — do básico ao avançado, com exemplos práticos organizados por aula.

---

## 📋 Sobre o projeto

Em vez de usar `print()` para depurar e monitorar código, este projeto explora o módulo nativo `logging` do Python de forma progressiva. Cada arquivo em `src/` corresponde a uma aula ou conceito específico, tornando o aprendizado simples de acompanhar e revisar.

---

## 🛠️ Tecnologias

- **Python** 3.13+
- **[uv](https://github.com/astral-sh/uv)** — gerenciador de pacotes e ambiente virtual
- **[rich](https://github.com/Textualize/rich)** — saída colorida e formatada no terminal
- **[just](https://github.com/casey/just)** — atalhos de comandos via `justfile`

---

## 📁 Estrutura do projeto

```
learning_logging/
│
├── src/
│   ├── lesson01.py   # Introdução ao logging
│   ├── lesson02.py   # Níveis de log
│   ├── ...
│   └── lesson06.py   # (aula atual)
│
├── main.py
├── justfile          # Atalhos de execução
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## 🚀 Como usar

**Pré-requisitos:** ter o [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado.

```bash
# Clone o repositório
git clone https://github.com/devkaua13/learning_logging.git
cd learning_logging

# Instale as dependências
uv sync
```

Para rodar uma aula específica:

```bash
# Diretamente com uv
uv run python3 src/lesson06.py

# Ou usando o justfile (para a aula configurada)
just lesson06
```

---

## 📌 Exemplo rápido

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)

logger.debug("Iniciando processamento...")
logger.info("Operação concluída com sucesso.")
logger.warning("Atenção: uso de memória elevado.")
logger.error("Falha ao conectar ao banco de dados.")
logger.critical("Sistema indisponível.")
```

---

## 📚 Referências

- [Documentação oficial — módulo `logging`](https://docs.python.org/3/library/logging.html)
- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
- [Documentação do uv](https://docs.astral.sh/uv/)
- [Documentação do rich](https://rich.readthedocs.io/)
