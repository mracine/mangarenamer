## Manga Renamer
This Python script is meant to aid in the renaming of directories containing image files meant for a manga or comic archive. It can sanitize any unwanted prefixes and suffixes, as well as re-indexing the image file names. Its general usage is like so:
```
python mangarenamer.py -o <offset> -P <prefix> -S <suffix>
```

For example: a file of the name **MANGA_01_V1.jpg** run with the following command
```
python mangarenamer.py -o -1 -P MANGA_ -S _V1
```
will result in an output file of **000.jpg***
