#!/bin/bash

echo "🚀 Запускаю Django Ninja магазин..."
echo ""

source .venv/bin/activate

echo "✅ Виртуальное окружение активировано"
echo "✅ Запускаю сервер на http://127.0.0.1:8080"
echo ""
echo "📋 Доступные URL:"
echo "   - API Документация: http://127.0.0.1:8080/api/docs"
echo "   - Админка: http://127.0.0.1:8080/admin/"
echo "   - API Товары: http://127.0.0.1:8080/api/shop/products"
echo ""

python manage.py runserver 8080
