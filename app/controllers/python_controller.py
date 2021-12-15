from app.controllers.controller import ControllerBase
from flask import render_template


class PythonController(ControllerBase):
    @staticmethod
    def get():
        return render_template('python.html')