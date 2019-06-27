mkdocs-wavedrom-plugin
=========================================================
A MkDocs plugin,  
render waveform charts in the wavedrom style.



Installation
--------------------------

Install the package with pip (under progress):

```bash
pip install git+https://github.com/mkdocs-mkdocs-plugin
```



How to use
--------------------------
More information about plugins in the [MkDocs documentation][mkdocs-plugins]

[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/


### write markdown/wavedrom code
embed your wavedrom code in markdown documents.

<pre>
```wavedrom
{ signal: [{ name: 'Alfa', wave: '01.zx=ud.23.45' }] }
```
</pre>

or see [a sample markdown](docs/test.md) for the sample.



### setup mkdocs.yml
change mkdocs.yml to use this plugin.

```
site_name: test
plugins:
    - markdownwavedrom

extra_javascript:
    - wavedrom.unpkg.js
    - skin-default.js
    # above, place *.js in docs directory, or below from internet.
    # - https://cdn.jsdelivr.net/npm/wavedrom@2.1.2/wavedrom.unpkg.js
    # - https://wavedrom.com/skins/default.js
```



Demo
--------------------------
see [sample a test.html result](http://htmlpreview.github.io/?https://github.com/kuri65536/mkdocs-wavedrom-plugin/test.html)

### local

```shell
$ python -m venv env
$ ./env/bin/python setup.py install
$ ./env/bin/mkdocs build
$ ./env/bin/mkdocs serve &
$ browse http://localhost:8000/test/index.html
```

or `make build` and `browse site/test/index.html`, if you have make binary.



Thanks
--------------------------
a lot part of this plugin  
were came from mkdocs-mermaid-plugin

