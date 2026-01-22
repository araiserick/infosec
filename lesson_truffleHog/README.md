# Задание truffleHog

по команде

```
trufflehog https://github.com/netology-code/ib-secrets.git | tee -a log.txt
```

Были выявлены следующие чувствительные данные, а именно:

- Приватный RSA-ключ
- Публичный RSA-ключ
- Симметричный ключ service/keys/symmetric.key
- Хэши паролей в SQL-файле
- Файл go.sum - Содержит контрольные суммы зависимостей Go

При повторной проверке

Несмотря на заявления о "очистке", в истории репозитория ib-secrets-fixed.git всё ещё присутствуют bcrypt-хэши паролей из файла 01_data.sql