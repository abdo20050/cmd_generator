# cmd_generator
python script for creating cmd file for irsim

## How to use
```bash
cmd_gen.py -n <fileName> -i <inputLabels> -o <outputLabels>
```
### Example
```bash 
python cmd_gen.py -n 'NotGate_2in' -i 'a b' -o 'o'
```
**OR**
```bash 
python3 cmd_gen.py -n 'NotGate_2in' -i 'a b' -o 'o'
```
It will creat a file named `NotGate_2in.cmd` and open it after running the command

example file attatched in [example folder](/examples/NotGate_2in.cmd)
