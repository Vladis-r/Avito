# Avito (service with ads)
 - use "docker-compose up --build -d" in ./market_postgres/ for start PostgreSQL and frontend_react (backend: localhost:8000, frontend: localhost:3000)
 - use django server to launch the application

---

### Используемые технологии:
Django, django_rest_framework, djoser, django_filter


### Задача: 
Написать backend под готовый react_front:
- авторизация и аутентификация пользователей
- распределение ролей
- CRUD для объявлений и комментариев, permissions
- поиск по объявлениям