import logging
import sys
from rich import print as rprint
from rich.markdown import Markdown

format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"

# Podemos criar nossos próprios handlers usando as classes que foram mencionadas antes
file_handler = logging.FileHandler(
    filename = '../log.log',
    mode = 'w',
    encoding = 'utf-8',
)

stream_handler = logging.StreamHandler(sys.stdout)

# Nossos Handlers precisam de Formatters
main_formatter = logging.Formatter(fmt=format1)

# A configuração do formatter pode ser reutilizada
file_handler.setFormatter(main_formatter)
stream_handler.setFormatter(main_formatter)


# Configurando o root Logger
stream_handler_root =  logging.StreamHandler(sys.stdout)
stream_handler_root.setFormatter(
    logging.Formatter(fmt='ROOT: [%(filename)s %(message)s]')
)
stream_handler_root.setLevel(logging.INFO)
logging.basicConfig(level=logging.WARNING, handlers=[stream_handler_root])


# Configurar o root logger com 2 handlers
# logging.basicConfig(handlers=[file_handler, stream_handler])

# Cria o próprio Logger 
logger = logging.getLogger('meuapp')

#define o nivel do meu log
logger.setLevel(logging.DEBUG)

# Como desativar a propagação, que nada mais é que não levar esse log para os outros logs pais dele
logger.propagate = False

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Testando retirar a lib externa do root logger - Contudo a melhor solução ainda é criar o proprio logger
# logging.getLogger('markdown_it').setLevel(logging.WARNING)

# Saída nos dois handlers
logger.info("Mensagem de teste para saber se o Just Cria")

# Renderiza Markdown
md = Markdown ("# Nos Handlers de `A`\n\nEste é um `Markdown`")
rprint(md)
