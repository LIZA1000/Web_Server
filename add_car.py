from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddCarForm(FlaskForm):
    model = StringField('Модель автомобиля', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    dealer = StringField('Дилерский центр', validators=[DataRequired()])
    submit = SubmitField('Добавить')
