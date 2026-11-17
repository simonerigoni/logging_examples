import importlib.util
import logging
import sqlite3
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "example_3" / "SQLiteHandler.py"


def _load_sqlite_handler_module():
    spec = importlib.util.spec_from_file_location("SQLiteHandler", MODULE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sqlite_handler_creates_table_and_persists_records(tmp_path):
    module = _load_sqlite_handler_module()
    database = tmp_path / "test_log.db"
    table = "log"
    handler = module.SQLiteHandler(
        database=str(database),
        table=table,
        attributes_list=module.DEFAULT_ATTRIBUTES_LIST,
    )
    handler.setLevel(logging.DEBUG)
    # emit() reads record.asctime, so the formatter must populate it.
    fmt = (
        "%("
        + ((")s" + module.DEFAULT_SEPARATOR + "%(").join(module.DEFAULT_ATTRIBUTES_LIST))
        + ")s"
    )
    handler.setFormatter(logging.Formatter(fmt))

    logger = logging.getLogger("test_sqlite_handler")
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    logger.addHandler(handler)

    logger.info("hello sqlite")
    logger.error("something failed")

    columns = ", ".join(module.DEFAULT_ATTRIBUTES_LIST)
    conn = sqlite3.connect(database)
    try:
        rows = conn.execute(f"SELECT {columns} FROM {table} ORDER BY levelname").fetchall()
    finally:
        conn.close()
        logger.removeHandler(handler)
        handler.close()

    assert database.is_file()
    message_index = module.DEFAULT_ATTRIBUTES_LIST.index("message")
    level_index = module.DEFAULT_ATTRIBUTES_LIST.index("levelname")
    messages = {row[message_index] for row in rows}
    levels = {row[level_index] for row in rows}
    assert messages == {"hello sqlite", "something failed"}
    assert levels == {"INFO", "ERROR"}
