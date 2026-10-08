# ClimatePulse

Projeto pessoal de portfólio em Engenharia de Dados sobre eventos climáticos extremos nos Estados Unidos.

## Status

Setup inicial do repositório. Nenhuma etapa do pipeline (ingestão, transformação, validação, carga ou análises) foi implementada ainda.

## Ambiente de desenvolvimento

Requer Python 3.12 ou superior.

```bash
python3 -m venv .venv        # apenas se a .venv ainda não existir
source .venv/bin/activate
pip install -r requirements.txt
```

Para sair do ambiente virtual: `deactivate`.

## Estrutura

- `src/climatepulse/` — código do pipeline
- `sql/` — DDL, transformações e consultas analíticas
- `config/` — configuração do pipeline
- `data/` — dados locais (não versionados)
- `docs/` — arquitetura, dicionário de dados e qualidade de dados
- `tests/` — testes
