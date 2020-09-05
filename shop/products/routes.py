import secrets

from flask import render_template, request, flash, url_for

from shop import app
from werkzeug.utils import redirect

from .forms import AddProductForm
from .models import Brand, Category
from .. import db, photos


@app.route('/add-brand', methods=['GET', 'POST'])
def add_brand():
    if request.method == 'POST':
        get_brand = request.form['brand']
        brand = Brand(name=get_brand)
        db.session.add(brand)
        db.session.commit()
        flash(f'The brand {get_brand} was added to your database', 'success')
        return redirect(url_for('add_brand'))
    return render_template('products/add_brand.html', brands='brands')


@app.route('/add-category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        get_category = request.form['category']
        category = Category(name=get_category)
        db.session.add(category)
        db.session.commit()
        flash(f'The Category {get_category} was added to your database', 'success')
        return redirect(url_for('add_category'))
    return render_template('products/add_brand.html')


@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    brands = Brand.query.all()
    categories = Category.query.all()
    if request.method == 'POST':
        photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + '.')
        photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + '.')
        photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + '.')
    form = AddProductForm(request.form)
    return render_template('products/add_product.html', form=form, brands=brands, categories=categories)
