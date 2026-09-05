import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def read_excel_file(file_path: str):
    """Заглушка для совместимости со старыми тестами."""
    # Для второй курсовой работы эта функция не нужна
    return None


def get_date_range(date_str: str):
    """Заглушка для совместимости со старыми тестами."""
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return dt.replace(day=1), dt


def format_date(date_obj):
    """Заглушка для совместимости со старыми тестами."""
    return date_obj.strftime('%d.%m.%Y')