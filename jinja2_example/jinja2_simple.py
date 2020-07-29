#!/usr/bin/env python
import jinja2

my_dict = {"ip_addr1": "1.1.1.2", "ip_addr2": "2.2.2.2"}

my_template = """
some
text
of
something
{{ ip_addr1 }}
{{ ip_addr2 }}
something
"""

t = jinja2.Template(my_template)
print(t.render(my_dict))
