INSERT INTO call_log_topic (id,title) VALUES
(1,'01 СНИЛС'),
(2,'02 Пенсии'),
(3,'03 Социальные выплаты'),
(4,'04 Материнский капитал'),
(5,'05 Пенсионные накопления'),
(6,'06 Регистрация в ЕСИА'),
(7,'07 Выплаты по смерти'),
(8,'08 Предварительный заказ документов'),
(9,'09 Запись на прием'),
(10,'10 Выездной прием'),
(11,'11 Общие вопросы'),
(12,'12 Отчетность ПУ');

SELECT setval('public.call_log_topic_id_seq', 29, true);

INSERT INTO call_log_topic (parent_id, title) VALUES
(1,'01.1. Регистрация, обмен, дубликат'),
(1,'01.2. Выписка из ИЛС'),
(2,'02.1. Назначение, перевод на другой вид пенсии'),
(2,'02.2. Перерасчет, корректировка'),
(2,'02.3. Выплата и доставка'),
(2,'02.4. Заблаговременное обращение за пенсией'),
(2,'02.5. Предпенсионный возраст'),
(2,'02.6 Удержания пенсии'),
(3,'03.1. Ежемесячная денежная выплата'),
(3,'03.2. Набор социальных услуг'),
(3,'03.3. Федеральная социальная доплата к пенсии'),
(3,'03.4. Дополнительное ежемесячное материальное обеспечение'),
(3,'03.5. Дополнительное социальное обеспечение (летчики, угольщики)'),
(3,'03.6. Ежемесячные компенсационные выплаты'),
(3,'03.7. Компенсация проезда РКС и МКС'),
(4,'04.1. Сертификат'),
(4,'04.2. Распоряжение'),
(4,'04.3. Единовременная выплата'),
(4,'04.4. Ежемесячная выплата'),
(5,'05.1. Выбор УК, смена страховщика'),
(5,'05.2. Правопреемники'),
(5,'05.3. Распределение пенсионных накоплений'),
(6,'06.1 Регистрация, восстановление учетной записи'),
(7,'07.1. Пособие, недополученная пенсия'),
(8,'08.1. Выписка из индивидуального лицевого счета'),
(8,'08.2. Справка о размере пенсии и иных социальных выплат'),
(8,'08.3. Справка о сумме материнского (семейного) капитала'),
(8,'08.4. Справка о сумме выплаченных пенсий и социальных выплат'),
(8,'08.5. Справка, что не являетесь получателем пенсии'),
(8,'08.6. Справка о праве на получение набора социальных услуг'),
(8,'08.7. Справка о недополученной сумме пенсии и социальных выплат в связи со смертью'),
(9,'09.1 Запись на прием'),
(11,'11.1 Общие вопросы'),
(12,'12.1 Соглашения по ЭДО'),
(12,'12.2 Регистрация страхователя в ПФР'),
(12,'12.3 Корректировка отчетности'),
(12,'12.4 Штрафные санкции');


