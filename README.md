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

<a href="bitcoin:39Qx9Nffad7UZVbcLpVpVanvdZEQUanEXd?message=thank-for-pdf-toc-outlines&amount=0.000035">
  <img src="https://github.com/user-attachments/assets/abce4347-bcb3-42c6-a9e8-1cd12f1bd4a5" />
</a>
___
<a href="ethereum:0x9d03b1a8264023c3ad8090b8fc2b75b1ba2b3f0f?value=0.002">
  <img src="https://github.com/user-attachments/assets/d1bdb9a8-9c6f-4e74-bc19-0d0bfa041eb2" />
</a>

- bitcoin:39Qx9Nffad7UZVbcLpVpVanvdZEQUanEXd
- ethereum:0x9d03b1a8264023c3ad8090b8fc2b75b1ba2b3f0f
- or librapay.
