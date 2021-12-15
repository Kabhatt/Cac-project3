from app.controllers.controller import ControllerBase
from flask import render_template


class OOPControler(ControllerBase):
    @staticmethod
    def get():
        return render_template('OOP.html')
