from flask import Blueprint, render_template, redirect, url_for, flash
from app import mongo
from utils.request_api import character_total


home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/add_character')
def add_character():
    character_len = len(character_total)
    for i in range(0,character_len):
        mongo.db.demo_personajes.insert_one(character_total[i])
    flash('Added characters')
    return redirect(url_for('home.index'))


@home.route('/list_characters')
def list_characters():
    list_query = mongo.db.demo_personajes.find()
    # lista_json = list(lista)
    return render_template('characters.html', lista = list_query)


@home.route('/delete_characters')
def delete_characters():
    mongo.db.demo_personajes.drop()
    flash('Deleted characters')
    return redirect(url_for('home.index'))


@home.route('/detail_character/<int:id>/')
def detail_character(id):
    unique = mongo.db.demo_personajes.find_one({"id": id})
    return render_template('/detail.html', character_unique=unique)


# @home.route('/siguiente_pagina')
# def siguiente_pagina():
#     contador = 2

#     lista_nueva= next_page(contador)
#     contador+=1
#     return render_template('personajes.html', lista = lista_nueva)


