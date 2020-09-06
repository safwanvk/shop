import secrets

from flask import render_template, request, flash, url_for

from shop import app
from werkzeug.utils import redirect

from .forms import AddProductForm
from .models import Brand, Category, Product
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
    form = AddProductForm(request.form)
    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.discription.data
        brand = request.form.get('brand')
        category = request.form.get('categories')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + '.')
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + '.')
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + '.')
        addpro = Product(name=name, price=price, discount=discount, stock=stock, colors=colors, desc=desc, brand_id=brand, category_id=category, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addpro)
        flash(f'The product {name} has been added to your database', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/add_product.html', form=form, brands=brands, categories=categories)
