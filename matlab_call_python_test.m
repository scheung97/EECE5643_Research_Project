pe = pyenv;
if pe.Status == 'Loaded'
    disp('To change Python version, restart MATLAB then call pyenv()');
else
    pyenv('Version', '3.9');
end 

web_path = fileparts(which('webscrape.py')); 
if count(py.sys.path,'') == 0
    insert(py.sys.path,int32(0), web_path);
end 

% hw_path = fileparts(which('helloworld.py')); 
% insert(py.sys.path,int32(0), hw_path); 

x = py.webscrape.main(); 
% py.print('Hello World'); 
