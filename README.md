# Projekts programmēšanā

Šis ir skolas projekts, kurš veidots ar Python un Flask. Tiek izmantots CSV fails ar datiem, kas tiek apstrādāti un attēloti grafikā. Dati tiek saglabāti arī SQLite datubāzē.

## Tehnoloģijas

- Python
- Flask
- Pandas
- matplotlib
- SQLite

## Funkcionalitāte

- CSV datu augšupielāde un nolasīšana
- Datu vizualizācija (diagrammas un histogrammas)
- Datu saglabāšana SQLite datubāzē
- HTML saskarne ar Flask

## Projekta faili

- `app.py` — galvenā Flask lietotne
- `data.csv` — dati
- `db.py` — datubāzes savienojums
- `README.md` — apraksts

## Kā darbināt

1. Instalēt vajadzīgās bibliotēkas:

```
pip install flask pandas matplotlib
```

2. Palaist programmu:

```
python app.py
```

3. Atvērt pārlūkā:

```
http://127.0.0.1:5000
```
