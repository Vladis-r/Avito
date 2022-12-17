# Avito (service with ads)
 - use "docker-compose up --build -d" in ./market_postgres/ for start PostgreSQL and frontend_react (backend: localhost:8000, frontend: localhost:3000)
 - use django server to launch the application
   - /api/docs for swagger,  /api/redoc-tasks/ for redoc
   - /api/token for JWT
   - test user: 
{
    "email": "test@skypro.ru",
    "password": 111
}

---

### Используемые технологии:
Django, django_rest_framework, djoser, django_filter, swagger, PostgreSQL, JWT


### Задача: 
Написать backend под готовый react_front:
- авторизация и аутентификация пользователей
- распределение ролей
- CRUD для объявлений и комментариев, permissions
- поиск по объявлениям