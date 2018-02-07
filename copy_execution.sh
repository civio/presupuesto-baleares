SOURCE=/Users/David/Box\ Sync/Civio/Proyectos/13\ Transparencia\ Municipal/Ganados/Gobierno\ Islas\ Baleares/02\ Datos

for LANGUAGE in es ca
do
  for YEAR in 2012 2013 2014 2015 2016 2017 2018
  do
    cp "$SOURCE/Códigos/csv/$LANGUAGE/$YEAR/estructura_economica.csv" data/$LANGUAGE/comunidad/$YEAR/estructura_economica.csv
    cp "$SOURCE/Códigos/csv/$LANGUAGE/$YEAR/estructura_organica.csv" data/$LANGUAGE/comunidad/$YEAR/estructura_organica.csv
    cp "$SOURCE/Códigos/csv/$LANGUAGE/$YEAR/estructura_funcional.csv" data/$LANGUAGE/comunidad/$YEAR/estructura_funcional.csv

    cp "$SOURCE/Ejecución/csv/$YEAR/ejecucion_ingresos.csv" data/$LANGUAGE/comunidad/$YEAR/ejecucion_ingresos.csv
    cp "$SOURCE/Ejecución/csv/$YEAR/ejecucion_gastos.csv" data/$LANGUAGE/comunidad/$YEAR/ejecucion_gastos.csv
  done
done