# -*- coding: UTF-8 -*-
from __future__ import division
import math
import logging
from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException, MissingParameterException
logging.basicConfig()
logger = logging.getLogger("kalliope")
class Calculator(NeuronModule):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)

        self.variable_1 = kwargs.get('variable_1', None)
        self.variable_2 = kwargs.get('variable_2', None)
        self.operator = kwargs.get('operator', None)
        
        if self._is_parameters_ok():
            def calculate(x,y):
                x = float(x)
                y = float(y)
                if "add"==self.operator:
                    solution= x + y
                elif "subtract"==self.operator:
                    solution= x - y     
                elif "multiply"==self.operator:   
                    solution= x * y
                elif "divide"==self.operator:
                    solution=float(x / y)
                elif "power"==self.operator:
                    solution =float(math.pow(x,y))
                elif "square_root"==self.operator:
                    solution=float(math.sqrt(x))
                elif "arc_cosinus"==self.operator:
                    solution=float(math.acos(x))
                elif "arc_sinus"==self.operator:
                    solution=float(math.asin(x))
                elif "arc_tangente"==self.operator:
                    solution=float(math.atan(x))
                elif "cos"==self.operator:
                    solution=float(math.cos(x))
                elif "sin"==self.operator:
                    solution=float(math.sin(x))
                elif "tan"==self.operator:
                    solution=float(math.tan(x))
                elif "common_divisor"==self.operator:
                    solution =float(math.gcd(x,y))

                solution = (("%.1f" % solution)).rstrip('0')
                return solution

            message = {"solution": calculate(self.variable_1,self.variable_2)}        
            self.say(message)
            
    def _is_parameters_ok(self):
        def check_for_integer(parameter): 
            try:
                parameter = float(parameter)
            except ValueError:   
                raise InvalidParameterException("[Calculator] %s is not a valid float" % parameter)
        
        if self.variable_1:
            check_for_integer(self.variable_1)
        else:
            raise MissingParameterException("[Calculator] Variable_1 is missing")
        
        if self.variable_2:
            check_for_integer(self.variable_2)
        else:
            raise MissingParameterException("[Calculator] Variable_2 is missing")
        
        if self.operator:
            operators = ["add", "subtract", "multiply", "divide","power","square_root","arc_cosinus","arc_sinus","arc_tangente","cos","sin","tan","common_divisor"]
            if self.operator not in operators:
                raise MissingParameterException("[Calculator] %s is not a valid operator" % self.operator)
        else:
            raise MissingParameterException("[Calculator] You have to set a valid operator")
        return True
