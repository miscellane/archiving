## Archiving

Transferred over from organisation **discourses**.

<br>
<br>

### Development Notes

The environment is [miscellaneous](https://github.com/briefings/energy#development-notes).  In relation to requirements.txt

```bash
    conda activate miscellaneous
    pip freeze -r docs/filter.txt > requirements.txt
```

whereby filter.txt does not include `python-graphviz`.

<br>
<br>

### References

* [shutil.move](https://docs.python.org/3.8/library/shutil.html#shutil.move)
* [Dask DataFrame API](https://docs.dask.org/en/latest/dataframe-api.html#dask.dataframe.from_pandas)
* [Creating a dask DataFrame](https://docs.dask.org/en/latest/dataframe-create.html)
* [Graphs](https://docs.dask.org/en/latest/graphviz.html)
* [Dask Scheduler](https://docs.dask.org/en/latest/scheduler-overview.html)
* [Managing Packages via Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html)

<br>
<br>
<br>
<br>
