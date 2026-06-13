import logging
import sys
from rich import print as rprint
from rich.markdown import Markdown

format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"

# Podemos criar nossos próprios handlers usando as classes que foram mencionadas antes
file_handler = logging.FileHandler(
    filename = '../log.log',
    mode = 'a',
    encoding = 'utf-8',
)

stream_handler = logging.StreamHandler(sys.stdout)

# Nossos Handlers precisam de Formatters
main_formatter = logging.Formatter(fmt=format1)

# A configuração do formatter pode ser reutilizada
file_handler.setFormatter(main_formatter)
stream_handler.setFormatter(main_formatter)

# Configurar o root logger com 2 handlers
logging.basicConfig(handlers=[file_handler, stream_handler])

# Cria o próprio Logger 
logger = logging.getLogger("meuapp")

#define o nivel do meu log
logger.setLevel(logging.DEBUG)

# Saída nos dois handlers
logger.debug("Mensagem para Kauã")

# Renderiza Markdown
md = Markdown ("# Nos Handlers de `A`\n\nEste é um `Markdown`")
rprint(md)
