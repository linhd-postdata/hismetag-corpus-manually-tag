"""Config for hismetag test corpus"""

import os
import sys


# config path
import inspect
here = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
sys.path.append(here)


# used in output file names
batch_name = "selected_2000"

# base dir
bdir = os.path.join(os.path.join(here, os.pardir), "manually_tagged" +
                    os.sep + "all")
bdir_by_genre = bdir + "_by_genre"

# files we're using now
#    fn: nbr of lines expected to yield required nbr of entities
filenames = { 
    "legal": {
        "Vidal_mayor.xml": 65, 
        "TEXT_AMU.xml": 540},
    "history": {
        "Historia_de_los_godos_de_San_Isidoro.xml": 150},
    "poetry": {
        "Libro_Alexandre.xml": 1380,
        "Libro_del_buen_amor.xml": 1175,
        "Mocedades_de_Rodrigo.xml": 125,
        "Poema_del_Mio_Cid.xml": 725},
    "theater": {
        "Comedia_de_Calisto_y_Melibea._Sevilla-_Estanislao_Polono.xml": 600},
    "narrative": {
        "Historia_Troyana.xml": 500,
        "Lazarillo_de_Tormes-_Alcala_de_Henares.xml": 400},
}

genres = {"legal": [], "history": [],
          "lite": ["narrative", "poetry", "theater"]}

# check config
all_genre_keys = genres.keys() + [va for va in genres.values() if va][0]
for ke in filenames:
    assert ke in all_genre_keys

# path to directory for files with geogName rendered as placeName
odir_merged_loc = "{}_LOC_merged"

# tags we consider
tags = ("persName", "placeName", "geogName", "orgName", "name")

# path to script to neutralize placeName vs geogName
locmerger = os.path.join(here, "merge_LOC.sh")

