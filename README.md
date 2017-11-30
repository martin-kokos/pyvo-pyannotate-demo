
## Pyvo pyannotate demo

https://github.com/dropbox/pyannotate

# Setup pytest for pyannotate profiling
`wget https://raw.githubusercontent.com/dropbox/pyannotate/master/example/example_conftest.py -O conftest.py`

# Run tests
`pytest`
We now have file `type_info.json`

# Insert types into file (pretend)
`pyannotate --type-info type_info.json *.py`
