## Archiving

<br>

### Environment

* Channel: [Anaconda](https://anaconda.org)
* Local Environment: _.../miscellaneous_

<br>
<br>


### Filter & Requirements

Notes w.r.t. explicitly installed packages 

* `conda create --prefix J:/Programs/Anaconda3/envs/miscellaneous python=3.7`
* `conda install -c anaconda dask pillow==7.1.2`
* `conda install -c anaconda python-graphviz` (Unable to include in filter.txt)

<br>

hence, the requirements

```
  pip freeze -r docs/filter.txt > requirements.txt 
```

<br>

Upgrades

* `conda update -c anaconda pillow`, which behaved similarly to `conda activate anaconda`
* `conda install -c anaconda pillow==8.1.2`
* `conda install -c anaconda jinja2==2.11.3`
* `conda install -c anaconda dask==2.30.0`

<br>
<br>

### Later

```
  conda install - anaconda pytest coverage pytest-cov pylint
```

<br>
<br>

### References

* [shutil.move](https://docs.python.org/3.8/library/shutil.html#shutil.move)
* [Dask DataFrame API](https://docs.dask.org/en/latest/dataframe-api.html#dask.dataframe.from_pandas)
* [Creating a dask DataFrame](https://docs.dask.org/en/latest/dataframe-create.html)
* [Graphs](https://docs.dask.org/en/latest/graphviz.html)
* [Dask Scheduler](https://docs.dask.org/en/latest/scheduler-overview.html)
* [Managing Packages via Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html)

