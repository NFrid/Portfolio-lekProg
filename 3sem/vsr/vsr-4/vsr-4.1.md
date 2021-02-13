# ВСР 4.1

Сравнительный анализ библиотек для тестирования

| Название | Преимущества                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Недостатки                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| py.test  | Используется стандартный assert. Подробный отчёт (в т.ч. в JUnitXML для интеграции с Jenkins). Параметризация тестов. Метки (marks), позволяющие пропустить любой тест, пометить тест, как падающий. Независимость от API (no boilerplate). Модульность (отдельный функционал во множестве доп. модулей). Возможность запуска тестов unittest и nose (обратная совместимость). Дополнительные возможности фикстур (возвращаемое значение, финализаторы, область видимости, объект request, автоиспользование, вложенные фикстуры). | Отсутствие дополнительного уровня вложенности: для модулей, классов, методов, функций в тестах есть лишь соответствующий уровень. |
| doctest  | Простота написания. Документация всегда соответствует реальному коду.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Плохо масштабируем, при достаточной сложности кода не подлежит дебаггингу, даже подсветка синтаксиса зачастую перестаёт работать. |
| unittest | Очань прост и лёгок в использовании. Широкий функционал: проверки (assert\*), декораторы, позволяющие пропустить отдельный тест (@skip, @skipIf) или обозначить сломанные тесты (@expectedFailure). ООП стиль тестов (удобно в тестировании классов).                                                                                                                                                                                                                                                                              | Много кода, Java-подобный стиль -> хуже читаемость.                                                                               |
| nose     | Настраиваемый за пользователя unittest, с кучей плагинов, также расширяющих его функционал и предоставляющих больше инструментов для автоматизации самого создания тестов.                                                                                                                                                                                                                                                                                                                                                         | Всё те же, что у unittest (т.к. является его расширением), но в меньшей степени.                                                  |