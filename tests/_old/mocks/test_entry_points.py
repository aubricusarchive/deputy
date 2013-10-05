from pkg_resources import iter_entry_points as lsep

entry_points = list(lsep('deputy.filecabinet'))
