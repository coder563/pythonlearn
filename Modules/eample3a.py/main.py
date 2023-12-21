#create a module object
#combile a module object
#add it to global namespace 
#execute it 
import types
import sys
import os.path as path

module_name = 'module1'
module_file = 'module1_source.py'
module_path = '.'
module_rel_file_path = path.join(module_path, module_file)
module_abs_filepath = path.join(module_rel_file_path)


#Open a file
with open(module_file) as modefile:
    source = modefile.read()
#Create a module object
mod = types.ModuleType(module_name)
#add the module opbject to 
sys.modules[module_name] = mod

code = compile(source,filename=module_abs_filepath,mode='exec')

exec(code,mod.__dict__)