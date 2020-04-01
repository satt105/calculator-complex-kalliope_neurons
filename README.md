## Synopsis
-Calculate simple and complexe operations
-Calculator neuron for Kalliope 0.5<0.6
## require
- python 3 or python 2.7
- kalliope core installed

## Installation
```bash
cd (your kalliope)
kalliope install --git-url https://github.com/satt105/calculator-complex-kalliope_neurons.git
```

## Options

| Parameter   | Required | Choices                          |
|-------------|----------|---------------------------------|
| variable_1  | yes      | float                |
| variable_2  | yes      | float                |
| operator    | yes      | add, subtract, multiply, divide, power, square_root, arc_cosinus, arc_sinus , arc_tangente, cos, sin, tan |


## Return values

| Name         | Description                                  | Type   | Sample |
|--------------|----------------------------------------------|--------|--------|
| solution     | Returns the solution of the given operation  | (default) float| 5      |

## Notes
- The module is a beta version under development, it is possible that the production of errors
- The module is developed by the community for the kalliope project. It can be modified and updated
- for the square root calculation function, you still had to specify a variable 2. The solution is to use a numeric variable that will not be taken into account in the calculation but in the verification

## Notes for the numbers float
- Numbers that have a comma, must undergo a stt correction that will transform the comma into a point.

## example:
```
  - name: "calculate-multiply"
    signals:
      - order: 
          text: "calculate {{ var1 }} x {{ var2 }}"
          stt-correction:
          - input: ","
            output: "."
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "multiply"
          say_template: "The solution is {{ solution }}"
```
## Synapses example configuration
```
  - name: "calculate-add"
    signals:
      - order: "calculate {{ var1 }} + {{ var2 }}"
      - order: "calculate {{ var1 }} add {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "add"
          say_template: "The solution is {{ solution }}"

  - name: "calculate-subtract"
    signals:
      - order: "calculate {{ var1 }} - {{ var2 }}"
      - order: "calculate {{ var1 }} subtract with {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "subtract"
          say_template: "The solution is {{ solution }}"
  
  - name: "calculate-multiply"
    signals:
      - order: "calculate {{ var1 }} x {{ var2 }}"
      - order: "calculate {{ var1 }} multiply by {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "multiply"
          say_template: "The solution is {{ solution }}"
  
  - name: "calculate-divide"
    signals:
      - order: "calculate {{ var1 }} / {{ var2 }}"
      - order: "calculate {{ var1 }} divide by {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "divide"
          say_template: "The solution is {{ solution }}"
          
  - name: "calculate-power"
    signals:
      - order: "calculate {{ var1 }} power {{ var2 }}"
      - order: "calculate {{ var1 }} ** {{ var2 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "power"
          say_template: "The solution is {{ solution }}"
          
  - name: "calculate-square_root"
    signals:
      - order: "calculate the square root of {{ var1 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "square_root"
          say_template: "The solution is {{ solution }}"
         
  - name: "calculate-arc_cosinus"
    signals:
      - order: "calculate the arccos of {{ var1 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "arc_cosinus"
          say_template: "The solution is {{ solution }}"
          
  - name: "calculate-arc_sinus"
    signals:
      - order: "calculate the arcsinus of {{ var1 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "arc_sinus"
          say_template: "The solution is {{ solution }}"
          
  - name: "calculate-arc_tangente"
    signals:
      - order: "calculate the arctangente of {{ var1 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "arc_tangente"
          say_template: "The solution is {{ solution }}"
          
  - name: "calculate-cos"
    signals:
      - order: "calculate the cos of {{ var1 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "cos"
          say_template: "The solution is {{ solution }}"
          
  - name: "calculate-sin"
    signals:
      - order: "calculate the sin of {{ var1 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "sin"
          say_template: "The solution is {{ solution }}"
          
  - name: "calculate-tan"
    signals:
      - order: "calculate the arctangente of {{ var1 }}"
    neurons:
      - calculator:
          variable_1: "{{ var1 }}"
          variable_2: "{{ var2 }}"
          operator: "tan"
          say_template: "The solution is {{ solution }}"

```




