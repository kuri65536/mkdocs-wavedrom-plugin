mkdocs-wavedrom-plugin
=========================================================
A MkDocs plugin,  
render waveform charts in the wavedrom style.



Installation
--------------------------
Install this package with pip.

### from PyPi
```bash
pip install mkdocs-wavedrom-plugin
```

### from github
```bash
pip install git+https://github.com/kuri65536/mkdocs-mkdocs-plugin
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

or see [a sample markdown](https://github.com/kuri65536/mkdocs-wavedrom-plugin/docs/test.md)
for the sample.



### setup mkdocs.yml
change mkdocs.yml to use this plugin.

```
site_name: test
plugins:
    - markdownwavedrom

extra_javascript:
    # - wavedrom.unpkg.js
    # - skin-default.js
    # above, place *.js in docs directory, or below from internet.
    - https://cdn.jsdelivr.net/npm/wavedrom@2.1.2/wavedrom.unpkg.js
    - https://wavedrom.com/skins/default.js
```



Demo
--------------------------
see [sample a test.html result](https://raw.githack.com/kuri65536/mkdocs-wavedrom-plugin/master/test.html)

### image
![test image](https://user-images.githubusercontent.com/11357613/60380894-ad48c280-9a87-11e9-9e0a-e782b1805310.png)

### from local

```shell
$ python -m venv env
$ ./env/bin/python setup.py install
$ ./env/bin/mkdocs build
$ ./env/bin/mkdocs serve &
$ browse http://localhost:8000/test/index.html
```

or `make build` and `browse site/test/index.html`, if you have make binary.

### (optional) download wavedrom
to download javascript files to local

```shell
$ make download
```



Thanks
--------------------------
a lot part of this plugin  
were came from mkdocs-mermaid-plugin



Donations
---------------------
If you are feel to nice for this software, please donation to my

-   Bitcoin **| 1FTBAUaVdeGG9EPsGMD5j2SW8QHNc5HzjT |**
-   or Ether **| 0xd7Dc5cd13BD7636664D6bf0Ee8424CFaF6b2FA8f |** .


