from app.controllers.controller import ControllerBase
from flask import render_template


class SOLIDController(ControllerBase):
    @staticmethod
    def get():
        return render_template('SOLID.html')