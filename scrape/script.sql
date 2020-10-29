DROP TABLE IF EXISTS public.table;
CREATE TABLE public.table (id SERIAL, date DATE, title varchar (400), source varchar(200), link varchar(300));
COPY public.table FROM '/var/lib/postgresql/data/scrape/f1.csv' WITH CSV HEADER;
SELECT title, source FROM public.table WHERE date='2020-10-29';
