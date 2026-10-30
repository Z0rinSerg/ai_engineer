# ai-engineer

> MCP-based AI engineering toolkit — проект для разработки инструментов и интеграции по Model Context Protocol.

[![CI Status](https://github.com/Z0rinSerg/ai_engineer_playground/actions/workflows/ci.yml/badge.svg)](https://github.com/Z0rinSerg/ai_engineer_playground/actions)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)]()
[![Python Version](https://img.shields.io/pypi/pyversions/ai-engineer)]()

## О проекте

`ai-engineer` — это стартовый шаблон Python-проекта под задачи AI-инженерии с фокусом на **Model Context Protocol (MCP)**.

**Ключевые особенности:**
- ✅ **100% покрытие тестами** (pytest + coverage)
- ✅ **Статический анализ** (Pylint, без лишнего шума по docstrings)
- ✅ **Современный менеджмент зависимостей** (UV, воспроизводимые сборки)
- ✅ **Структура под MCP**: отдельные модули для инструментов и сервера
- ✅ **CI/CD**: GitHub Actions с фильтрацией по путям (не запускается на правках README)

Проект ориентирован на Linux (Ubuntu 24.04+), но может работать и на других платформах при наличии UV.

---

## Быстрый старт

### Требования
- Python ≥ 3.12
- UV (рекомендуется)
- Git

### Установка и запуск

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/Z0rinSerg/ai_engineer_playground.git
   cd ai_engineer_playground
   ```

Синхронизируй зависимости через UV:

```bash
uv sync
```

Запусти тесты с покрытием:

```bash
uv run coverage run -m pytest tests/
uv run coverage report
```

Запусти линтер:

```bash
uv run pylint src/ai_engineer
```

Запусти точку входа (если есть CLI):

```bash
uv run python src/ai_engineer/main.py
```

## Структура проекта

```text
ai_engineer/
├── .github/
│   └── workflows/          # CI/CD (GitHub Actions)
├── src/
│   └── ai_engineer/
│       ├── __init__.py     # экспорты
│       ├── main.py         # точка входа
│       ├── mcp/            # MCP-сервер и протокол
│       │   ├── server.py
│       │   └── tools.py
│       └── tools/          # инструменты для MCP
├── tests/                  # тесты (pytest, asyncio)
├── pyproject.toml          # зависимости, настройки pytest и pylint
├── uv.lock                 # воспроизводимые версии зависимостей
└── README.md
```

## Разработка под MCP

Проект подготовлен к интеграции MCP-сервера и инструментов:

- Модуль `src/ai_engineer/mcp/` — место для реализации сервера и регистрации инструментов.
- Модуль `src/ai_engineer/tools/` — отдельные инструменты, которые можно регистрировать в MCP.

**Планируемые шаги:**
1. Реализация базового MCP-сервера
2. Регистрация 2–3 тестовых инструментов
3. Интеграция с LLM-клиентом (через отдельный пакет)

## CI/CD

GitHub Actions настроен так, чтобы не запускаться на изменениях документации:

- Запускается только при изменениях в `src/**`, `tests/**`, `pyproject.toml` и самом workflow.
- Проверяет: `pytest` (с `pytest-asyncio`), `coverage`, `pylint`.
- Сохраняет отчёт покрытия как артефакт (`htmlcov/`).

## Вклад в проект (Contributing)

Если хочешь поучаствовать:

1. Создай форк и ветку с фичей.
2. Убедись, что тесты проходят и покрытие не падает.
3. Проверь, что Pylint не выдаёт новых ошибок.
4. Отправь PR.

## Лицензия

MIT