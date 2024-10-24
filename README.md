# Django，Celeryのサンプルプロジェクト

## 概要

DjangoとCeleryを使ったサンプルプロジェクトです。

Zennの記事は[こちら](https://zenn.dev/enken/articles/enken-django-celery)

## 使い方

Dockerの使える環境を前提としています．

### 起動
以下のコマンドで立ち上がります．

```bash
make dev
```

### 停止，削除

以下のコマンドで停止と削除ができます．

```bash
make down
```

### ポート
- Django: http://localhost:8000/
- RabbitMQ: http://localhost:15672/
  - Username: sample_user
  - Password: sample_password
