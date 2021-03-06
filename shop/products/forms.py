from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField, \
    DecimalField
from flask_wtf.file import FileAllowed, FileRequired, FileField


class AddProductForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    discription = TextAreaField('Discription', [validators.DataRequired()])
    colors = TextAreaField('Colors', [validators.DataRequired()])
    image_1 = FileField('Image 1',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('Image 2',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('Image 3',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
