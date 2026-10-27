def render_template(template_name: str) -> str:  
    """Читает HTML-файл и возвращает его содержимое."""  
    with open(f"templates/{template_name}", "r", encoding="utf-8") as file:  
        return file.read() 
